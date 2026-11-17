#
# As USS19902971457_KTKAR_test.py, but the array-processing parameters
# (rel.power, abs.power, baz, slow) are plotted as symbols in panels
# beneath a panel showing the waveforms, all on the same time axis.
#
import numpy as np
from obspy import read, read_inventory
#
from obspy.core.util import AttribDict
from obspy.imaging.cm import obspy_sequential
from obspy.signal.array_analysis import array_processing
#
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
#
NNSN_archive_path = '../clones/NNSN_nuclear_explosion_waveforms/ARCHIVE'
event    = 'USS19902971457'
stations = ['KTK1', 'KTK2', 'KTK3', 'KTK4', 'KTK5', 'KTK6']
#
st  = read( NNSN_archive_path + '/' + event + '/' + event + '_NS.' + stations[0] + '.00.SHZ.mseed' )
inv = read_inventory( NNSN_archive_path + '/../RESPONSES/' + stations[0] + '.xml' )
for sta in stations[1:]:
    st  += read( NNSN_archive_path + '/' + event + '/' + event + '_NS.' + sta + '.00.SHZ.mseed' )
    inv += read_inventory( NNSN_archive_path + '/../RESPONSES/' + sta + '.xml' )
numstat = len( st )
#
# First we add the coordinates to the trace stats
#
for istat in range( 0, numstat ):
    tr_id  = st[istat].stats.network + '.'
    tr_id += st[istat].stats.station + '.'
    tr_id += st[istat].stats.location + '.'
    tr_id += st[istat].stats.channel
    coords = inv.get_coordinates(tr_id)
    st[istat].stats.coordinates = AttribDict({
        'latitude':  coords['latitude'],
        'elevation': coords['elevation'],
        'longitude': coords['longitude']})
    print (istat, tr_id, st[istat].stats.coordinates )
#
START = st[0].stats.starttime
END   = st[0].stats.endtime
#
# Filtering
FMIN = 1.0  # [Hz]
FMAX = 6.0  # [Hz]
# Array processing
WINLEN = 4.0  # [s]
WINOVER = 0.25
#
st.filter('bandpass', freqmin=FMIN, freqmax=FMAX, corners=2, zerophase=True)
st.taper(max_percentage=0.01)
#
kwargs = dict(
    # slowness grid: X min, X max, Y min, Y max, Slow Step
    sll_x=-3.0, slm_x=3.0, sll_y=-3.0, slm_y=3.0, sl_s=0.03,
    # sliding window properties
    win_len=WINLEN, win_frac=WINOVER,
    # frequency properties
    frqlow=FMIN, frqhigh=FMAX, prewhiten=0,
    # restrict output
    semb_thres=-1e9, vel_thres=-1e9, timestamp='mlabday',
    stime=START, etime=END
)
out = array_processing(st, **kwargs)
#
# Plot: waveform panel on top, then the four parameter panels,
# all sharing one time axis.
#
labels = ['rel.power', 'abs.power', 'baz', 'slow']
#
xlocator = mdates.AutoDateLocator()
nparam = len( labels )
fig, axes = plt.subplots( nparam + 1, 1, sharex=True,
                          gridspec_kw={'height_ratios': [2] + [1]*nparam} )
#
# Waveforms: each trace normalised to its own maximum and offset vertically
#
axw = axes[0]
for i, tr in enumerate( st ):
    t    = tr.times('matplotlib')
    data = tr.data / np.abs( tr.data ).max()
    axw.plot( t, data + 2.0*(numstat - 1 - i), 'k', linewidth=0.5 )
axw.set_yticks( [2.0*(numstat - 1 - i) for i in range(numstat)] )
axw.set_yticklabels( [tr.stats.station for tr in st], fontsize=7 )
axw.set_ylim( -1.5, 2.0*(numstat - 1) + 1.5 )
axw.set_ylabel('waveforms')
#
# Parameter symbols
#
for i, lab in enumerate(labels):
    ax = axes[i + 1]
    ax.scatter(out[:, 0], out[:, i + 1], c=out[:, 1], alpha=0.6,
               edgecolors='none', cmap=obspy_sequential)
    ax.set_ylabel(lab)
    if ( i < 3 ):
        ax.set_ylim(out[:, i + 1].min(), out[:, i + 1].max())
    else:
        ax.set_ylim( 0.0, 0.5 )
#
# Common time axis (set once; shared by every panel)
#
axes[0].set_xlim( START.matplotlib_date, END.matplotlib_date )
axes[-1].xaxis.set_major_locator(xlocator)
axes[-1].xaxis.set_major_formatter(mdates.AutoDateFormatter(xlocator))
#
fig.suptitle(' %s.  KTKAR %s' % ( event, START.strftime('%Y-%m-%d') ))
fig.autofmt_xdate()
fig.subplots_adjust(left=0.15, top=0.95, right=0.95, bottom=0.2, hspace=0)
plt.show()

