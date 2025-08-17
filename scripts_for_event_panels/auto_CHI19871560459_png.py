import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/CHI19871560459/CHI19871560459_NS.ASK3.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19871560459/CHI19871560459_NS.BER.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19871560459/CHI19871560459_NS.HYA.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19871560459/CHI19871560459_NS.KMY.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19871560459/CHI19871560459_NS.LOF.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19871560459/CHI19871560459_NS.MOL.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19871560459/CHI19871560459_NS.NSS.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19871560459/CHI19871560459_NS.ODD.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19871560459/CHI19871560459_NS.SUE.00.SHZ.mseed")
t1  = UTCDateTime("1987-06-05T05:07:00")
t2  = UTCDateTime("1987-06-05T05:12:00")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
#st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 45.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "CHI19871560459.png" )
exit(0)
