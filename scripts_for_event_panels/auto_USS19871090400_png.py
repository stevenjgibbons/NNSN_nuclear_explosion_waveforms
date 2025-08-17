import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/USS19871090400/USS19871090400_NS.KTK1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19871090400/USS19871090400_NS.MOL.00.SHZ.mseed")
st += read("../NNSN_archive/USS19871090400/USS19871090400_NS.MOR.00.SHZ.mseed")
st += read("../NNSN_archive/USS19871090400/USS19871090400_NS.NSS.00.SHZ.mseed")
t1  = UTCDateTime("1987-04-19T04:03:00")
t2  = UTCDateTime("1987-04-19T04:08:00")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
#st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 70.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "USS19871090400.png" )
exit(0)
