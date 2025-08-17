import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/CHI19941610625/CHI19941610625_NS.BJO.00.SHE.mseed")
st += read("../NNSN_archive/CHI19941610625/CHI19941610625_NS.BJO.00.SHN.mseed")
st += read("../NNSN_archive/CHI19941610625/CHI19941610625_NS.BJO.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19941610625/CHI19941610625_NS.HYA.00.SHE.mseed")
st += read("../NNSN_archive/CHI19941610625/CHI19941610625_NS.HYA.00.SHN.mseed")
st += read("../NNSN_archive/CHI19941610625/CHI19941610625_NS.HYA.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19941610625/CHI19941610625_NS.KONO.00.BVZ.mseed")
st += read("../NNSN_archive/CHI19941610625/CHI19941610625_NS.LOF.00.SHE.mseed")
st += read("../NNSN_archive/CHI19941610625/CHI19941610625_NS.LOF.00.SHN.mseed")
st += read("../NNSN_archive/CHI19941610625/CHI19941610625_NS.LOF.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19941610625/CHI19941610625_NS.MOR8.00.SHE.mseed")
st += read("../NNSN_archive/CHI19941610625/CHI19941610625_NS.MOR8.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19941610625/CHI19941610625_NS.NSS.00.SHE.mseed")
st += read("../NNSN_archive/CHI19941610625/CHI19941610625_NS.NSS.00.SHN.mseed")
st += read("../NNSN_archive/CHI19941610625/CHI19941610625_NS.NSS.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19941610625/CHI19941610625_NS.SUE.00.SHE.mseed")
st += read("../NNSN_archive/CHI19941610625/CHI19941610625_NS.SUE.00.SHN.mseed")
st += read("../NNSN_archive/CHI19941610625/CHI19941610625_NS.SUE.00.SHZ.mseed")
t1  = UTCDateTime("1994-06-10T06:33:00")
t2  = UTCDateTime("1994-06-10T06:38:00")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
#st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 45.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "CHI19941610625.png" )
exit(0)
