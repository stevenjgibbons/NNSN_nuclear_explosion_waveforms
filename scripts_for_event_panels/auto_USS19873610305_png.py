import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/USS19873610305/USS19873610305_NS.ASK1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873610305/USS19873610305_NS.ASK2.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873610305/USS19873610305_NS.ASK3.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873610305/USS19873610305_NS.ASK4.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873610305/USS19873610305_NS.BER.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873610305/USS19873610305_NS.BLS1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873610305/USS19873610305_NS.BLS2.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873610305/USS19873610305_NS.BLS3.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873610305/USS19873610305_NS.HYA.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873610305/USS19873610305_NS.KMY.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873610305/USS19873610305_NS.ODD1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873610305/USS19873610305_NS.SUE.00.SHZ.mseed")
print ( st[0].stats.starttime )
t1  = UTCDateTime("1987-12-27T03:11:00")
t2  = UTCDateTime("1987-12-27T03:16:00")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
#st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 45.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "USS19873610305.png" )
exit(0)
