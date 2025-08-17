import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/USS19851150057/USS19851150057_NS.ASK2.00.SHZ.mseed")
st += read("../NNSN_archive/USS19851150057/USS19851150057_NS.BER.00.SHZ.mseed")
st += read("../NNSN_archive/USS19851150057/USS19851150057_NS.HYA.00.SHZ.mseed")
st += read("../NNSN_archive/USS19851150057/USS19851150057_NS.KMY.00.SHZ.mseed")
st += read("../NNSN_archive/USS19851150057/USS19851150057_NS.ODD.00.SHZ.mseed")
st += read("../NNSN_archive/USS19851150057/USS19851150057_NS.SUE.00.SHZ.mseed")
t1  = UTCDateTime("1985-04-25T01:03:00")
t2  = UTCDateTime("1985-04-25T01:08:00")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
#st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 45.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "USS19851150057.png" )
exit(0)
