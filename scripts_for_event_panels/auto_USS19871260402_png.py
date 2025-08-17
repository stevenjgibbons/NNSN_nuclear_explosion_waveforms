import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/USS19871260402/USS19871260402_NS.ASK3.00.SHZ.mseed")
st += read("../NNSN_archive/USS19871260402/USS19871260402_NS.BER.00.SHZ.mseed")
st += read("../NNSN_archive/USS19871260402/USS19871260402_NS.HYA.00.SHZ.mseed")
st += read("../NNSN_archive/USS19871260402/USS19871260402_NS.KMY.00.SHZ.mseed")
st += read("../NNSN_archive/USS19871260402/USS19871260402_NS.LOF.00.SHZ.mseed")
st += read("../NNSN_archive/USS19871260402/USS19871260402_NS.NSS.00.SHZ.mseed")
st += read("../NNSN_archive/USS19871260402/USS19871260402_NS.ODD.00.SHZ.mseed")
t1  = UTCDateTime("1987-05-06T04:15:00")
t2  = UTCDateTime("1987-05-06T04:20:00")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
#st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 45.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "USS19871260402.png" )
exit(0)
