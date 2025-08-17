import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/USS19850410327/USS19850410327_NS.ASK4.00.SHZ.mseed")
st += read("../NNSN_archive/USS19850410327/USS19850410327_NS.HYA.00.SHZ.mseed")
st += read("../NNSN_archive/USS19850410327/USS19850410327_NS.KMY.00.SHZ.mseed")
st += read("../NNSN_archive/USS19850410327/USS19850410327_NS.ODD.00.SHZ.mseed")
st += read("../NNSN_archive/USS19850410327/USS19850410327_NS.SUE.00.SHZ.mseed")
t1  = UTCDateTime("1985-02-10T03:31:00")
t2  = UTCDateTime("1985-02-10T03:36:00")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
#st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 45.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "USS19850410327.png" )
exit(0)
