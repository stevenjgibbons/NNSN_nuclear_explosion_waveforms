import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/USS19881282249/USS19881282249_NS.MOL.00.SLZ.mseed")
st += read("../NNSN_archive/USS19881282249/USS19881282249_NS.TRO.00.SLZ.mseed")
st.plot( equal_scale = False, size = [900, 800] )
t1  = UTCDateTime("1988-05-07T22:52:00")
t2  = UTCDateTime("1988-05-07T22:57:00")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
#st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 120.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "USS19881282249.png" )
exit(0)
