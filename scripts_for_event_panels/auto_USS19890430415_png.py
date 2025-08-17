import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/USS19890430415/USS19890430415_NS.ASK1.00.SHE.mseed")
st += read("../NNSN_archive/USS19890430415/USS19890430415_NS.ASK1.00.SHN.mseed")
st += read("../NNSN_archive/USS19890430415/USS19890430415_NS.ASK1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19890430415/USS19890430415_NS.ASK4.00.SHZ.mseed")
st += read("../NNSN_archive/USS19890430415/USS19890430415_NS.BER.00.SHZ.mseed")
st += read("../NNSN_archive/USS19890430415/USS19890430415_NS.BLS1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19890430415/USS19890430415_NS.BLS3.00.SHZ.mseed")
st += read("../NNSN_archive/USS19890430415/USS19890430415_NS.BLS4.00.SHZ.mseed")
st += read("../NNSN_archive/USS19890430415/USS19890430415_NS.HYA.00.SHZ.mseed")
st += read("../NNSN_archive/USS19890430415/USS19890430415_NS.KMY.00.SHZ.mseed")
st += read("../NNSN_archive/USS19890430415/USS19890430415_NS.KTK1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19890430415/USS19890430415_NS.KTK2.00.SHZ.mseed")
st += read("../NNSN_archive/USS19890430415/USS19890430415_NS.KTK3.00.SHZ.mseed")
st += read("../NNSN_archive/USS19890430415/USS19890430415_NS.KTK4.00.SHZ.mseed")
st += read("../NNSN_archive/USS19890430415/USS19890430415_NS.KTK5.00.SHZ.mseed")
st += read("../NNSN_archive/USS19890430415/USS19890430415_NS.KTK6.00.SHZ.mseed")
st += read("../NNSN_archive/USS19890430415/USS19890430415_NS.LOF.00.SHE.mseed")
st += read("../NNSN_archive/USS19890430415/USS19890430415_NS.LOF.00.SHN.mseed")
st += read("../NNSN_archive/USS19890430415/USS19890430415_NS.LOF.00.SHZ.mseed")
st += read("../NNSN_archive/USS19890430415/USS19890430415_NS.MOL.00.SHZ.mseed")
st += read("../NNSN_archive/USS19890430415/USS19890430415_NS.MOR1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19890430415/USS19890430415_NS.MOR2.00.SHZ.mseed")
st += read("../NNSN_archive/USS19890430415/USS19890430415_NS.MOR3.00.SHZ.mseed")
st += read("../NNSN_archive/USS19890430415/USS19890430415_NS.MOR5.00.SHZ.mseed")
st += read("../NNSN_archive/USS19890430415/USS19890430415_NS.MOR6.00.SHZ.mseed")
st += read("../NNSN_archive/USS19890430415/USS19890430415_NS.ODD1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19890430415/USS19890430415_NS.SUE.00.SHZ.mseed")
st += read("../NNSN_archive/USS19890430415/USS19890430415_NS.TRO.00.SHZ.mseed")
#
# KTK is sadly cut
#
t1  = UTCDateTime("1989-02-12T04:20:00")
t2  = UTCDateTime("1989-02-12T04:25:00")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
#st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 45.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "USS19890430415.png" )
exit(0)
