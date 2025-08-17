import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/USS19870570458/USS19870570458_NS.LOF.00.SHZ.mseed")
st += read("../NNSN_archive/USS19870570458/USS19870570458_NS.MOL.00.SHZ.mseed")
st += read("../NNSN_archive/USS19870570458/USS19870570458_NS.NSS.00.SHZ.mseed")
t1  = UTCDateTime("1987-02-26T05:04:00")
t2  = UTCDateTime("1987-02-26T05:09:00")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
#st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 70.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "USS19870570458.png" )
exit(0)
