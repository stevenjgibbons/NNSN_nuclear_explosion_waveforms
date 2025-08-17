import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/CHI19921420459/CHI19921420459_NS.BJO.00.SHE.mseed")
st += read("../NNSN_archive/CHI19921420459/CHI19921420459_NS.BJO.00.SHN.mseed")
st += read("../NNSN_archive/CHI19921420459/CHI19921420459_NS.BJO.00.SHZ.mseed")
# st += read("../NNSN_archive/CHI19921420459/CHI19921420459_NS.FOO.00.SHE.mseed")
st += read("../NNSN_archive/CHI19921420459/CHI19921420459_NS.FOO.00.SHN.mseed")
st += read("../NNSN_archive/CHI19921420459/CHI19921420459_NS.FOO.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19921420459/CHI19921420459_NS.FRO.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19921420459/CHI19921420459_NS.HYA.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19921420459/CHI19921420459_NS.JMI.00.SHE.mseed")
st += read("../NNSN_archive/CHI19921420459/CHI19921420459_NS.JMI.00.SHN.mseed")
st += read("../NNSN_archive/CHI19921420459/CHI19921420459_NS.JMI.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19921420459/CHI19921420459_NS.JMI.00.SLZ.mseed")
st += read("../NNSN_archive/CHI19921420459/CHI19921420459_NS.JNE.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19921420459/CHI19921420459_NS.JNW.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19921420459/CHI19921420459_NS.KMY.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19921420459/CHI19921420459_NS.KTK1.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19921420459/CHI19921420459_NS.KTK4.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19921420459/CHI19921420459_NS.KTK5.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19921420459/CHI19921420459_NS.KTK6.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19921420459/CHI19921420459_NS.LOF.00.SHE.mseed")
st += read("../NNSN_archive/CHI19921420459/CHI19921420459_NS.LOF.00.SHN.mseed")
st += read("../NNSN_archive/CHI19921420459/CHI19921420459_NS.LOF.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19921420459/CHI19921420459_NS.MOL.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19921420459/CHI19921420459_NS.NSS.00.SHZ.mseed")
t1  = UTCDateTime("1992-05-21T05:07:00")
t2  = UTCDateTime("1992-05-21T05:12:00")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
#st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 45.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "CHI19921420459.png" )
exit(0)
