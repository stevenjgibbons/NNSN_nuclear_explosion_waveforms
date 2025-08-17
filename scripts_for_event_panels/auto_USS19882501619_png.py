import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/USS19882501619/USS19882501619_NS.ASK1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19882501619/USS19882501619_NS.ASK2.00.SHZ.mseed")
st += read("../NNSN_archive/USS19882501619/USS19882501619_NS.ASK3.00.SHZ.mseed")
st += read("../NNSN_archive/USS19882501619/USS19882501619_NS.ASK4.00.SHZ.mseed")
st += read("../NNSN_archive/USS19882501619/USS19882501619_NS.ASK5.00.SHZ.mseed")
st += read("../NNSN_archive/USS19882501619/USS19882501619_NS.BER.00.SHZ.mseed")
st += read("../NNSN_archive/USS19882501619/USS19882501619_NS.BLS1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19882501619/USS19882501619_NS.BLS2.00.SHZ.mseed")
st += read("../NNSN_archive/USS19882501619/USS19882501619_NS.HYA.00.SHZ.mseed")
st += read("../NNSN_archive/USS19882501619/USS19882501619_NS.KMY.00.SHZ.mseed")
st += read("../NNSN_archive/USS19882501619/USS19882501619_NS.ODD1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19882501619/USS19882501619_NS.SUE.00.SHZ.mseed")
# Note that you see good PcP on ASK for this event
# but it comes after 5 minutes
t1  = UTCDateTime("1988-09-06T16:23:00")
t2  = UTCDateTime("1988-09-06T16:28:00")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
#st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 45.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "USS19882501619.png" )
exit(0)
