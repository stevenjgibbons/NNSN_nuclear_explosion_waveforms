import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/USS19882580400/USS19882580400_NS.ASK1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19882580400/USS19882580400_NS.ASK2.00.SHZ.mseed")
st += read("../NNSN_archive/USS19882580400/USS19882580400_NS.ASK3.00.SHZ.mseed")
st += read("../NNSN_archive/USS19882580400/USS19882580400_NS.ASK4.00.SHZ.mseed")
st += read("../NNSN_archive/USS19882580400/USS19882580400_NS.ASK5.00.SHZ.mseed")
st += read("../NNSN_archive/USS19882580400/USS19882580400_NS.BER.00.SHZ.mseed")
st += read("../NNSN_archive/USS19882580400/USS19882580400_NS.BLS1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19882580400/USS19882580400_NS.BLS2.00.SHZ.mseed")
st += read("../NNSN_archive/USS19882580400/USS19882580400_NS.BLS3.00.SHZ.mseed")
st += read("../NNSN_archive/USS19882580400/USS19882580400_NS.HYA.00.SHZ.mseed")
st += read("../NNSN_archive/USS19882580400/USS19882580400_NS.KMY.00.SHZ.mseed")
st += read("../NNSN_archive/USS19882580400/USS19882580400_NS.KTK1.00.SLZ.mseed")
st += read("../NNSN_archive/USS19882580400/USS19882580400_NS.MOL.00.SLZ.mseed")
st += read("../NNSN_archive/USS19882580400/USS19882580400_NS.NSS.00.SLZ.mseed")
st += read("../NNSN_archive/USS19882580400/USS19882580400_NS.ODD1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19882580400/USS19882580400_NS.SUE.00.SHZ.mseed")
st += read("../NNSN_archive/USS19882580400/USS19882580400_NS.TRO.00.SLZ.mseed")
t1  = UTCDateTime("1988-09-14T04:05:00")
t2  = UTCDateTime("1988-09-14T04:10:00")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
#st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 45.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "USS19882580400.png" )
exit(0)
