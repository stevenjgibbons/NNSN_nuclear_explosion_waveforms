import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/USS19871710053/USS19871710053_NS.ASK1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19871710053/USS19871710053_NS.BLS1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19871710053/USS19871710053_NS.HYA.00.SHZ.mseed")
st += read("../NNSN_archive/USS19871710053/USS19871710053_NS.KMY.00.SHZ.mseed")
st += read("../NNSN_archive/USS19871710053/USS19871710053_NS.LOF.00.SHZ.mseed")
st += read("../NNSN_archive/USS19871710053/USS19871710053_NS.MOR6.00.SHZ.mseed")
st += read("../NNSN_archive/USS19871710053/USS19871710053_NS.NSS.00.SHZ.mseed")
st += read("../NNSN_archive/USS19871710053/USS19871710053_NS.ODD.00.SHZ.mseed")
st += read("../NNSN_archive/USS19871710053/USS19871710053_NS.SUE.00.SHZ.mseed")
t1  = UTCDateTime("1987-06-20T00:59:00")
t2  = UTCDateTime("1987-06-20T01:04:00")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
#st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 45.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "USS19871710053.png" )
exit(0)
