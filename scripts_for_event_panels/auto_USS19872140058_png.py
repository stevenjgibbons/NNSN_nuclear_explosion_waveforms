import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/USS19872140058/USS19872140058_NS.ASK1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19872140058/USS19872140058_NS.BLS1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19872140058/USS19872140058_NS.HYA.00.SHZ.mseed")
st += read("../NNSN_archive/USS19872140058/USS19872140058_NS.KMY.00.SHZ.mseed")
st += read("../NNSN_archive/USS19872140058/USS19872140058_NS.KTK1.00.SZL.mseed")
st += read("../NNSN_archive/USS19872140058/USS19872140058_NS.LOF.00.SZL.mseed")
st += read("../NNSN_archive/USS19872140058/USS19872140058_NS.MOL.00.SZL.mseed")
st += read("../NNSN_archive/USS19872140058/USS19872140058_NS.MOR1.00.SZL.mseed")
st += read("../NNSN_archive/USS19872140058/USS19872140058_NS.NSS.00.SZL.mseed")
st += read("../NNSN_archive/USS19872140058/USS19872140058_NS.ODD.00.SHZ.mseed")
st += read("../NNSN_archive/USS19872140058/USS19872140058_NS.SUE.00.SHZ.mseed")
st += read("../NNSN_archive/USS19872140058/USS19872140058_NS.TRO.00.SZL.mseed")
t1  = UTCDateTime("1987-08-02T01:03:30")
t2  = UTCDateTime("1987-08-02T01:08:30")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
# st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 45.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "USS19872140058.png" )
exit(0)
