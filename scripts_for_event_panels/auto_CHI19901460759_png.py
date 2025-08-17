import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/CHI19901460759/CHI19901460759_NS.KTK1.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19901460759/CHI19901460759_NS.KTK2.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19901460759/CHI19901460759_NS.KTK3.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19901460759/CHI19901460759_NS.KTK4.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19901460759/CHI19901460759_NS.KTK5.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19901460759/CHI19901460759_NS.KTK6.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19901460759/CHI19901460759_NS.LOF.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19901460759/CHI19901460759_NS.LOF.00.SHE.mseed")
st += read("../NNSN_archive/CHI19901460759/CHI19901460759_NS.LOF.00.SHN.mseed")
st += read("../NNSN_archive/CHI19901460759/CHI19901460759_NS.MOL.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19901460759/CHI19901460759_NS.MOR7.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19901460759/CHI19901460759_NS.NSS.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19901460759/CHI19901460759_NS.TRO.00.SHZ.mseed")
t1  = UTCDateTime("1990-05-26T08:06:00")
t2  = UTCDateTime("1990-05-26T08:11:00")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
# st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 45.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "CHI19901460759.png" )
exit(0)
