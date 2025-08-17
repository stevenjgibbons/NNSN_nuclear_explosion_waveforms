import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/USS19873470321/USS19873470321_NS.ASK1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873470321/USS19873470321_NS.ASK2.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873470321/USS19873470321_NS.ASK3.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873470321/USS19873470321_NS.ASK4.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873470321/USS19873470321_NS.BER.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873470321/USS19873470321_NS.BLS1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873470321/USS19873470321_NS.BLS2.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873470321/USS19873470321_NS.HYA.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873470321/USS19873470321_NS.KMY.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873470321/USS19873470321_NS.ODD.00.SHZ.mseed")
st += read("../NNSN_archive/USS19873470321/USS19873470321_NS.SUE.00.SHZ.mseed")
t1  = UTCDateTime("1987-12-13T03:27:00")
t2  = UTCDateTime("1987-12-13T03:32:00")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
# st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 45.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "USS19873470321.png" )
exit(0)
