import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/CHI19902280459/CHI19902280459_NS.ASK.00.SHE.mseed")
st += read("../NNSN_archive/CHI19902280459/CHI19902280459_NS.ASK.00.SHN.mseed")
st += read("../NNSN_archive/CHI19902280459/CHI19902280459_NS.ASK.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19902280459/CHI19902280459_NS.BER.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19902280459/CHI19902280459_NS.BLS1.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19902280459/CHI19902280459_NS.BLS2.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19902280459/CHI19902280459_NS.HYA.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19902280459/CHI19902280459_NS.KMY.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19902280459/CHI19902280459_NS.KTK1.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19902280459/CHI19902280459_NS.KTK2.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19902280459/CHI19902280459_NS.KTK3.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19902280459/CHI19902280459_NS.KTK4.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19902280459/CHI19902280459_NS.KTK5.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19902280459/CHI19902280459_NS.KTK6.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19902280459/CHI19902280459_NS.LOF.00.SHE.mseed")
st += read("../NNSN_archive/CHI19902280459/CHI19902280459_NS.LOF.00.SHN.mseed")
st += read("../NNSN_archive/CHI19902280459/CHI19902280459_NS.LOF.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19902280459/CHI19902280459_NS.MOL.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19902280459/CHI19902280459_NS.MOR7.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19902280459/CHI19902280459_NS.ODD1.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19902280459/CHI19902280459_NS.SUE.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19902280459/CHI19902280459_NS.TRO.00.SHZ.mseed")
t1  = UTCDateTime("1990-08-16T05:07:00")
t2  = UTCDateTime("1990-08-16T05:12:00")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
# st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 45.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "CHI19902280459.png" )
exit(0)
