import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/USS19883520418/USS19883520418_NS.ASK1.00.SHE.mseed")
st += read("../NNSN_archive/USS19883520418/USS19883520418_NS.ASK1.00.SHN.mseed")
st += read("../NNSN_archive/USS19883520418/USS19883520418_NS.ASK1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19883520418/USS19883520418_NS.ASK4.00.SHZ.mseed")
st += read("../NNSN_archive/USS19883520418/USS19883520418_NS.BER.00.SHZ.mseed")
st += read("../NNSN_archive/USS19883520418/USS19883520418_NS.BLS3.00.SHZ.mseed")
st += read("../NNSN_archive/USS19883520418/USS19883520418_NS.BLS4.00.SHZ.mseed")
st += read("../NNSN_archive/USS19883520418/USS19883520418_NS.HYA.00.SHZ.mseed")
st += read("../NNSN_archive/USS19883520418/USS19883520418_NS.KMY.00.SHZ.mseed")
st += read("../NNSN_archive/USS19883520418/USS19883520418_NS.ODD1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19883520418/USS19883520418_NS.SUE.00.SHZ.mseed")
st += read("../NNSN_archive/USS19883520418/USS19883520418_NS.TRO.00.SLZ.mseed")
t1  = UTCDateTime("1988-12-17T04:24:00")
t2  = UTCDateTime("1988-12-17T04:29:00")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
#st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 45.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "USS19883520418.png" )
exit(0)
