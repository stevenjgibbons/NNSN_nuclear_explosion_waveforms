import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/USS19882351620/USS19882351620_NS.KTK1.00.SLZ.mseed")
st += read("../NNSN_archive/USS19882351620/USS19882351620_NS.KTK2.00.SLZ.mseed")
st += read("../NNSN_archive/USS19882351620/USS19882351620_NS.KTK3.00.SLZ.mseed")
st += read("../NNSN_archive/USS19882351620/USS19882351620_NS.KTK4.00.SLZ.mseed")
st += read("../NNSN_archive/USS19882351620/USS19882351620_NS.KTK5.00.SLZ.mseed")
st += read("../NNSN_archive/USS19882351620/USS19882351620_NS.KTK6.00.SLZ.mseed")
st += read("../NNSN_archive/USS19882351620/USS19882351620_NS.LOF.00.AHE.mseed")
st += read("../NNSN_archive/USS19882351620/USS19882351620_NS.LOF.00.AHN.mseed")
st += read("../NNSN_archive/USS19882351620/USS19882351620_NS.LOF.00.AHZ.mseed")
st += read("../NNSN_archive/USS19882351620/USS19882351620_NS.LOF.00.SLE.mseed")
st += read("../NNSN_archive/USS19882351620/USS19882351620_NS.LOF.00.SLN.mseed")
st += read("../NNSN_archive/USS19882351620/USS19882351620_NS.LOF.00.SLZ.mseed")
st += read("../NNSN_archive/USS19882351620/USS19882351620_NS.MOL.00.SLZ.mseed")
st += read("../NNSN_archive/USS19882351620/USS19882351620_NS.NSS.00.SLZ.mseed")
t1  = UTCDateTime("1988-08-22T16:23:00")
t2  = UTCDateTime("1988-08-22T16:28:00")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
#st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 45.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "USS19882351620.png" )
exit(0)
