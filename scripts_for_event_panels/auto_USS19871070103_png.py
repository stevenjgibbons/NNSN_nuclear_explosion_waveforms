import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/USS19871070103/USS19871070103_NS.MOL.00.SHZ.mseed")
st += read("../NNSN_archive/USS19871070103/USS19871070103_NS.MOR.00.SHZ.mseed")
st += read("../NNSN_archive/USS19871070103/USS19871070103_NS.NSS.00.SHZ.mseed")
t1  = UTCDateTime("1987-04-17T01:09:00")
t2  = UTCDateTime("1987-04-17T01:14:00")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
#st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 75.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "USS19871070103.png" )
exit(0)
