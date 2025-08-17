import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/USS19883390519/USS19883390519_NS.KTK1.00.SLZ.mseed")
st += read("../NNSN_archive/USS19883390519/USS19883390519_NS.KTK2.00.SLZ.mseed")
st += read("../NNSN_archive/USS19883390519/USS19883390519_NS.KTK3.00.SLZ.mseed")
st += read("../NNSN_archive/USS19883390519/USS19883390519_NS.KTK4.00.SLZ.mseed")
st += read("../NNSN_archive/USS19883390519/USS19883390519_NS.KTK5.00.SLZ.mseed")
st += read("../NNSN_archive/USS19883390519/USS19883390519_NS.KTK6.00.SLZ.mseed")
st += read("../NNSN_archive/USS19883390519/USS19883390519_NS.LOF.00.SLE.mseed")
st += read("../NNSN_archive/USS19883390519/USS19883390519_NS.LOF.00.SLN.mseed")
st += read("../NNSN_archive/USS19883390519/USS19883390519_NS.LOF.00.SLZ.mseed")
st += read("../NNSN_archive/USS19883390519/USS19883390519_NS.MOL.00.SLZ.mseed")
st += read("../NNSN_archive/USS19883390519/USS19883390519_NS.MOR1.00.SLZ.mseed")
st += read("../NNSN_archive/USS19883390519/USS19883390519_NS.MOR2.00.SLZ.mseed")
st += read("../NNSN_archive/USS19883390519/USS19883390519_NS.MOR3.00.SLZ.mseed")
st += read("../NNSN_archive/USS19883390519/USS19883390519_NS.MOR4.00.SLZ.mseed")
st += read("../NNSN_archive/USS19883390519/USS19883390519_NS.MOR5.00.SLZ.mseed")
st += read("../NNSN_archive/USS19883390519/USS19883390519_NS.MOR6.00.SLZ.mseed")
st += read("../NNSN_archive/USS19883390519/USS19883390519_NS.NSS.00.SLZ.mseed")
st += read("../NNSN_archive/USS19883390519/USS19883390519_NS.TRO.00.SLZ.mseed")
t1  = UTCDateTime("1988-12-04T05:21:30")
t2  = UTCDateTime("1988-12-04T05:26:30")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
#st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 45.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "USS19883390519.png" )
exit(0)
