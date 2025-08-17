import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/CHI19932780159/CHI19932780159_NS.ASK.00.SHE.mseed")
st += read("../NNSN_archive/CHI19932780159/CHI19932780159_NS.ASK.00.SHN.mseed")
st += read("../NNSN_archive/CHI19932780159/CHI19932780159_NS.ASK.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19932780159/CHI19932780159_NS.BER.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19932780159/CHI19932780159_NS.BER.00.SLZ.mseed")
st += read("../NNSN_archive/CHI19932780159/CHI19932780159_NS.EGD.00.SHZ.mseed")
# st += read("../NNSN_archive/CHI19932780159/CHI19932780159_NS.FOO.00.SHE.mseed")
st += read("../NNSN_archive/CHI19932780159/CHI19932780159_NS.FOO.00.SHN.mseed")
st += read("../NNSN_archive/CHI19932780159/CHI19932780159_NS.FOO.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19932780159/CHI19932780159_NS.KMY.00.SHE.mseed")
st += read("../NNSN_archive/CHI19932780159/CHI19932780159_NS.KMY.00.SHN.mseed")
st += read("../NNSN_archive/CHI19932780159/CHI19932780159_NS.KMY.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19932780159/CHI19932780159_NS.LOF.00.SHE.mseed")
st += read("../NNSN_archive/CHI19932780159/CHI19932780159_NS.LOF.00.SHN.mseed")
st += read("../NNSN_archive/CHI19932780159/CHI19932780159_NS.LOF.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19932780159/CHI19932780159_NS.MOL.00.SHE.mseed")
st += read("../NNSN_archive/CHI19932780159/CHI19932780159_NS.MOL.00.SHN.mseed")
st += read("../NNSN_archive/CHI19932780159/CHI19932780159_NS.MOL.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19932780159/CHI19932780159_NS.MOR8.00.SHE.mseed")
st += read("../NNSN_archive/CHI19932780159/CHI19932780159_NS.MOR8.00.SHN.mseed")
st += read("../NNSN_archive/CHI19932780159/CHI19932780159_NS.MOR8.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19932780159/CHI19932780159_NS.NSS.00.SHE.mseed")
st += read("../NNSN_archive/CHI19932780159/CHI19932780159_NS.NSS.00.SHZ.mseed")
t1  = UTCDateTime("1993-10-05T02:07:00")
t2  = UTCDateTime("1993-10-05T02:12:00")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
# st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 45.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "CHI19932780159.png" )
exit(0)
