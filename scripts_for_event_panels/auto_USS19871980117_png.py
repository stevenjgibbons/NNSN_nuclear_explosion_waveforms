import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/USS19871980117/USS19871980117_NS.ASK1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19871980117/USS19871980117_NS.BLS1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19871980117/USS19871980117_NS.HYA.00.SHZ.mseed")
st += read("../NNSN_archive/USS19871980117/USS19871980117_NS.KMY.00.SHZ.mseed")
st += read("../NNSN_archive/USS19871980117/USS19871980117_NS.LOF.00.SHZ.mseed")
st += read("../NNSN_archive/USS19871980117/USS19871980117_NS.MOL.00.SHZ.mseed")
st += read("../NNSN_archive/USS19871980117/USS19871980117_NS.NSS.00.SHZ.mseed")
st += read("../NNSN_archive/USS19871980117/USS19871980117_NS.ODD.00.SHZ.mseed")
st += read("../NNSN_archive/USS19871980117/USS19871980117_NS.SUE.00.SHZ.mseed")
st += read("../NNSN_archive/USS19871980117/USS19871980117_NS.TRO.00.SHZ.mseed")
t1  = UTCDateTime("1987-07-17T01:23:00")
t2  = UTCDateTime("1987-07-17T01:28:00")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
#st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 45.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "USS19871980117.png" )
exit(0)
