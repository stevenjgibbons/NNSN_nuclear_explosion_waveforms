import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/USS19873190331/USS19873190331_NS.ASK1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873190331/USS19873190331_NS.ASK2.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873190331/USS19873190331_NS.ASK3.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873190331/USS19873190331_NS.ASK4.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873190331/USS19873190331_NS.BER.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873190331/USS19873190331_NS.BLS1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873190331/USS19873190331_NS.BLS2.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873190331/USS19873190331_NS.BLS3.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873190331/USS19873190331_NS.HYA.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873190331/USS19873190331_NS.KMY.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873190331/USS19873190331_NS.MOL.00.SZL.mseed")
st += read("../NNSN_archive/USS19873190331/USS19873190331_NS.MOR1.00.SZL.mseed")
st += read("../NNSN_archive/USS19873190331/USS19873190331_NS.MOR2.00.SZL.mseed")
st += read("../NNSN_archive/USS19873190331/USS19873190331_NS.MOR3.00.SZL.mseed")
st += read("../NNSN_archive/USS19873190331/USS19873190331_NS.MOR4.00.SZL.mseed")
st += read("../NNSN_archive/USS19873190331/USS19873190331_NS.MOR5.00.SZL.mseed")
st += read("../NNSN_archive/USS19873190331/USS19873190331_NS.MOR6.00.SZL.mseed")
st += read("../NNSN_archive/USS19873190331/USS19873190331_NS.ODD.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873190331/USS19873190331_NS.SUE.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873190331/USS19873190331_NS.TRO.00.SZL.mseed")
t1  = UTCDateTime("1987-11-15T03:37:00")
t2  = UTCDateTime("1987-11-15T03:42:00")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
# st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 45.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "USS19873190331.png" )
exit(0)
