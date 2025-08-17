import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/USS19872050200/USS19872050200_NS.LOF.00.SHZ.mseed")
st += read("../NNSN_archive/USS19872050200/USS19872050200_NS.MOL.00.SHZ.mseed")
st += read("../NNSN_archive/USS19872050200/USS19872050200_NS.TRO.00.SHZ.mseed")
t1  = UTCDateTime("1987-07-24T02:06:00")
t2  = UTCDateTime("1987-07-24T02:11:00")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
# st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 90.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "USS19872050200.png" )
exit(0)
