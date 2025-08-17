import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/USS19892920949/USS19892920949_NS.LOF.00.SHE.mseed")
st += read("../NNSN_archive/USS19892920949/USS19892920949_NS.LOF.00.SHN.mseed")
st += read("../NNSN_archive/USS19892920949/USS19892920949_NS.LOF.00.SHZ.mseed")
st += read("../NNSN_archive/USS19892920949/USS19892920949_NS.MOL.00.SHZ.mseed")
st += read("../NNSN_archive/USS19892920949/USS19892920949_NS.MOR1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19892920949/USS19892920949_NS.MOR2.00.SHZ.mseed")
st += read("../NNSN_archive/USS19892920949/USS19892920949_NS.MOR3.00.SHZ.mseed")
st += read("../NNSN_archive/USS19892920949/USS19892920949_NS.MOR4.00.SHZ.mseed")
st += read("../NNSN_archive/USS19892920949/USS19892920949_NS.MOR5.00.SHZ.mseed")
st += read("../NNSN_archive/USS19892920949/USS19892920949_NS.MOR6.00.SHZ.mseed")
st += read("../NNSN_archive/USS19892920949/USS19892920949_NS.NSS.00.SHZ.mseed")
st += read("../NNSN_archive/USS19892920949/USS19892920949_NS.TRO.00.SHZ.mseed")
t1  = UTCDateTime("1989-10-19T09:55:00")
t2  = UTCDateTime("1989-10-19T10:00:00")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
#st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 45.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "USS19892920949.png" )
exit(0)
