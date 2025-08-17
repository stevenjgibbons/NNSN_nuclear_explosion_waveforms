import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/IND19981311013/IND19981311013_NS.KBS.00.BVE.mseed")
st += read("../NNSN_archive/IND19981311013/IND19981311013_NS.KBS.00.BVN.mseed")
st += read("../NNSN_archive/IND19981311013/IND19981311013_NS.KBS.00.BVZ.mseed")
st += read("../NNSN_archive/IND19981311013/IND19981311013_NS.KONO.00.BVE.mseed")
st += read("../NNSN_archive/IND19981311013/IND19981311013_NS.KONO.00.BVN.mseed")
st += read("../NNSN_archive/IND19981311013/IND19981311013_NS.KONO.00.BVZ.mseed")
st += read("../NNSN_archive/IND19981311013/IND19981311013_NS.KTK1.00.SHE.mseed")
st += read("../NNSN_archive/IND19981311013/IND19981311013_NS.KTK1.00.SHN.mseed")
st += read("../NNSN_archive/IND19981311013/IND19981311013_NS.KTK1.00.SHZ.mseed")
st += read("../NNSN_archive/IND19981311013/IND19981311013_NS.MOR8.00.SHE.mseed")
st += read("../NNSN_archive/IND19981311013/IND19981311013_NS.MOR8.00.SHN.mseed")
st += read("../NNSN_archive/IND19981311013/IND19981311013_NS.MOR8.00.SHZ.mseed")
t1  = UTCDateTime("1998-05-11T10:21:00")
t2  = UTCDateTime("1998-05-11T10:26:00")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
#st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 45.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "IND19981311013.png" )
exit(0)
