import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/USS19880940133/USS19880940133_NS.ASK1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19880940133/USS19880940133_NS.ASK2.00.SHZ.mseed")
st += read("../NNSN_archive/USS19880940133/USS19880940133_NS.ASK3.00.SHZ.mseed")
st += read("../NNSN_archive/USS19880940133/USS19880940133_NS.ASK4.00.SHZ.mseed")
st += read("../NNSN_archive/USS19880940133/USS19880940133_NS.BER.00.SHZ.mseed")
st += read("../NNSN_archive/USS19880940133/USS19880940133_NS.BLS1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19880940133/USS19880940133_NS.BLS2.00.SHZ.mseed")
st += read("../NNSN_archive/USS19880940133/USS19880940133_NS.KMY.00.SHZ.mseed")
st += read("../NNSN_archive/USS19880940133/USS19880940133_NS.ODD1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19880940133/USS19880940133_NS.SUE.00.SHZ.mseed")
t1  = UTCDateTime("1988-04-03T01:39:00")
t2  = UTCDateTime("1988-04-03T01:44:00")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
#st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 45.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "USS19880940133.png" )
exit(0)
