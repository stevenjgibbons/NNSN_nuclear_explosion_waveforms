#
# Broadband delay-and-sum f-k analysis of the NNSN KTK array data for event
# USS19902971457.  Waveforms and coordinates are read exactly as in
# USS19902971457_KTKAR_test_scan.py; the f-k analysis and the plots follow
# fk_broadband_windows.py (one PNG + PDF per time window and frequency band).
#
import warnings
from pathlib import Path
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#
from obspy import read, read_inventory, UTCDateTime
from obspy.core.util import AttribDict
from obspy.geodetics.base import gps2dist_azimuth
#
# =======================
# User parameters
# =======================
NNSN_archive_path = '../clones/NNSN_nuclear_explosion_waveforms/ARCHIVE'
EVENT    = 'USS19902971457'
STATIONS = ['KTK1', 'KTK2', 'KTK3', 'KTK4', 'KTK5', 'KTK6']
#
# Centres of the analysis windows and the window length (seconds).
# Default: one window covering 15:00:34 - 15:00:40 as in the scan script.
TIMEPOINTS = [
    UTCDateTime("1990-10-24 15:00:37"),
]
WIN_LEN = 6.0
#
# Frequency bands (Hz)
BANDS = [
    (1.0, 3.0),
    (1.0, 4.0),
    (2.0, 4.0),
    (2.0, 5.0),
]
#
# Slowness grid (s/km), x = east, y = north
SLOW_MAX  = 0.4
SLOW_STEP = 0.01
#
FILTER_CORNERS   = 4
NORMALIZE_TRACES = True   # weight each station equally
#
OUT_DIR = Path("fk_out_KTK")
DPI     = 160
#
matplotlib.use("Agg", force=True)   # save figures to file; remove to show interactively
#
# =======================
# Reading waveforms and coordinates (as in the scan script)
# =======================
def read_data():
    st  = None
    inv = None
    for sta in STATIONS:
        f = NNSN_archive_path + '/' + EVENT + '/' + EVENT + '_NS.' + sta + '.00.SHZ.mseed'
        r = NNSN_archive_path + '/../RESPONSES/' + sta + '.xml'
        if st is None:
            st, inv = read(f), read_inventory(r)
        else:
            st  += read(f)
            inv += read_inventory(r)
    for tr in st:
        coords = inv.get_coordinates(tr.id)
        tr.stats.coordinates = AttribDict({
            'latitude':  coords['latitude'],
            'elevation': coords['elevation'],
            'longitude': coords['longitude']})
        print(tr.id, tr.stats.coordinates)
    return st, inv
#
# =======================
# Helpers
# =======================
def _fmt_iso(utct):
    dt = utct.datetime
    if dt.microsecond:
        return dt.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    return dt.strftime("%Y-%m-%dT%H:%M:%S") + "Z"
#
def station_offsets(st):
    """East/north offsets (km) of each trace from the median array position,
    taken from tr.stats.coordinates."""
    lats = np.array([tr.stats.coordinates.latitude  for tr in st])
    lons = np.array([tr.stats.coordinates.longitude for tr in st])
    ref_lat, ref_lon = np.median(lats), np.median(lons)
    east, north = [], []
    for la, lo in zip(lats, lons):
        d, az, _ = gps2dist_azimuth(ref_lat, ref_lon, la, lo)
        east.append(d * np.sin(np.deg2rad(az)) / 1000.0)
        north.append(d * np.cos(np.deg2rad(az)) / 1000.0)
    return np.array(east), np.array(north)
#
def fk_map_delay_and_sum(st, t_center, win_len, fmin, fmax,
                         slow_max=0.4, slow_step=0.01, normalize_traces=True):
    """Broadband delay-and-sum power on a 2-D slowness grid for one window.
    Same sign convention as fk_broadband_windows.py (+tau shift)."""
    st2 = st.copy()
    t0 = t_center - win_len / 2.0
    t1 = t_center + win_len / 2.0
    st2.trim(t0, t1, pad=True, fill_value=0.0)
    st2.detrend("linear")
    st2.taper(max_percentage=0.05, type="hann")
    st2.filter("bandpass", freqmin=fmin, freqmax=fmax,
               corners=FILTER_CORNERS, zerophase=True)
    #
    fs = float(np.max([tr.stats.sampling_rate for tr in st2]))
    st2.interpolate(sampling_rate=fs, method="lanczos", a=8)
    npts = min(tr.stats.npts for tr in st2)
    #
    east, north = station_offsets(st2)
    traces = []
    for tr in st2:
        y = tr.data[:npts].astype(np.float64)
        if normalize_traces:
            y = y / (np.max(np.abs(y)) or 1.0)
        traces.append(y)
    traces = np.vstack(traces)                      # (M, npts)
    M = traces.shape[0]
    #
    X     = np.fft.rfft(traces, axis=1)             # (M, nf)
    freqs = np.fft.rfftfreq(npts, d=1.0 / fs)       # (nf,)
    #
    sx_vals = np.arange(-slow_max, slow_max + 1e-9, slow_step)
    sy_vals = np.arange(-slow_max, slow_max + 1e-9, slow_step)
    SX, SY  = np.meshgrid(sx_vals, sy_vals)
    P = np.zeros_like(SX, dtype=np.float64)
    #
    for iy, sy in enumerate(sy_vals):
        tau   = np.outer(sx_vals, east) + sy * north            # (nsx, M)
        phase = np.exp(-2j * np.pi * freqs[None, None, :] * tau[:, :, None])
        stack = np.fft.irfft((X[None, :, :] * phase).sum(axis=1), n=npts, axis=1) / M
        P[iy, :] = np.mean(stack * stack, axis=1)
    #
    pmax = np.max(P) or 1.0
    Pn   = P / pmax
    imax = np.unravel_index(np.argmax(Pn), Pn.shape)
    sy_best, sx_best = sy_vals[imax[0]], sx_vals[imax[1]]
    slow_abs = np.hypot(sx_best, sy_best)
    best = {
        'sx': float(sx_best), 'sy': float(sy_best),
        'baz_deg': float((np.degrees(np.arctan2(sx_best, sy_best)) + 360.0) % 360.0),
        'va_km_s': float(1.0 / slow_abs) if slow_abs > 0 else float('inf'),
        'pmax': float(pmax)}
    return SX, SY, Pn, best
#
def plot_fk(SX, SY, Pn, best, t_center, win_len, band, out_dir):
    fmin, fmax = band
    fig, ax = plt.subplots(1, 1, figsize=(7, 6))
    im = ax.pcolormesh(SX, SY, Pn, shading='auto', cmap='viridis', edgecolors="face", linewidth=0.5, antialiased=True )
    # im = ax.pcolormesh(SX, SY, Pn, shading='nearest', cmap='viridis')
    cb = fig.colorbar(im, ax=ax, shrink=0.9)
    cb.set_label('Normalized beam power')
    ax.plot(best['sx'], best['sy'], 'r+', ms=12, mew=2, label='Max')
    ax.set_xlabel('Slowness east, s/km')
    ax.set_ylabel('Slowness north, s/km')
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True, alpha=0.3)
    ax.set_title(
        f"{EVENT} KTKAR  broadband FK (delay-sum)  band {fmin:.1f}-{fmax:.1f} Hz\n"
        f"Window: {_fmt_iso(t_center - win_len/2)} to {_fmt_iso(t_center + win_len/2)}  ({win_len:.1f} s)\n"
        f"Peak: BAZ={best['baz_deg']:.1f}°, v_app={best['va_km_s']:.2f} km/s, "
        f"(sx,sy)=({best['sx']:.2f},{best['sy']:.2f}) s/km", fontsize=9)
    safe_t = _fmt_iso(t_center).replace(':', '').replace('-', '')
    base = f"FK_{EVENT}_{safe_t}_{fmin:.1f}-{fmax:.1f}Hz"
    fig.tight_layout()
    fig.savefig(out_dir / f"{base}.png", dpi=DPI)
    fig.savefig(out_dir / f"{base}.pdf")
    plt.close(fig)
    return out_dir / f"{base}.png"
#
# =======================
# Main
# =======================
def main():
    warnings.filterwarnings("ignore", message="`alltrue` is deprecated")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    st, inv = read_data()
    for t_center in TIMEPOINTS:
        for band in BANDS:
            print(f"Computing FK: t={_fmt_iso(t_center)}, band={band[0]:.1f}-{band[1]:.1f} Hz")
            SX, SY, Pn, best = fk_map_delay_and_sum(
                st, t_center, WIN_LEN, band[0], band[1],
                slow_max=SLOW_MAX, slow_step=SLOW_STEP,
                normalize_traces=NORMALIZE_TRACES)
            out = plot_fk(SX, SY, Pn, best, t_center, WIN_LEN, band, OUT_DIR)
            print(f"  Saved: {out}")
            print(f"  Peak -> BAZ={best['baz_deg']:.1f} deg, v_app={best['va_km_s']:.2f} km/s, "
                  f"sx={best['sx']:.3f}, sy={best['sy']:.3f} s/km")
#
if __name__ == "__main__":
    main()

