import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/USS19872140200/USS19872140200_NS.ASK1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19872140200/USS19872140200_NS.BLS1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19872140200/USS19872140200_NS.HYA.00.SHZ.mseed")
st += read("../NNSN_archive/USS19872140200/USS19872140200_NS.KMY.00.SHZ.mseed")
st += read("../NNSN_archive/USS19872140200/USS19872140200_NS.KTK1.00.SZL.mseed")
st += read("../NNSN_archive/USS19872140200/USS19872140200_NS.LOF.00.SZL.mseed")
st += read("../NNSN_archive/USS19872140200/USS19872140200_NS.MOL.00.SZL.mseed")
st += read("../NNSN_archive/USS19872140200/USS19872140200_NS.MOR1.00.SZL.mseed")
st += read("../NNSN_archive/USS19872140200/USS19872140200_NS.NSS.00.SZL.mseed")
st += read("../NNSN_archive/USS19872140200/USS19872140200_NS.ODD.00.SHZ.mseed")
st += read("../NNSN_archive/USS19872140200/USS19872140200_NS.SUE.00.SHZ.mseed")
st += read("../NNSN_archive/USS19872140200/USS19872140200_NS.TRO.00.SZL.mseed")
# st.plot( equal_scale = False, size = [900, 800] )
t1  = UTCDateTime("1987-08-02T02:01:30")
t2  = UTCDateTime("1987-08-02T02:06:30")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
#st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 45.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "USS19872140200.png" )
exit(0)
