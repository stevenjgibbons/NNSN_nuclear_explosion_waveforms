import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/USS19870930117/USS19870930117_NS.ASK1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19870930117/USS19870930117_NS.ASK2.00.SHZ.mseed")
st += read("../NNSN_archive/USS19870930117/USS19870930117_NS.ASK4.00.SHZ.mseed")
st += read("../NNSN_archive/USS19870930117/USS19870930117_NS.ASK5.00.SHZ.mseed")
st += read("../NNSN_archive/USS19870930117/USS19870930117_NS.BER.00.SHZ.mseed")
st += read("../NNSN_archive/USS19870930117/USS19870930117_NS.BLS1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19870930117/USS19870930117_NS.HYA.00.SHZ.mseed")
st += read("../NNSN_archive/USS19870930117/USS19870930117_NS.LOF.00.SHZ.mseed")
st += read("../NNSN_archive/USS19870930117/USS19870930117_NS.MOL.00.SHZ.mseed")
st += read("../NNSN_archive/USS19870930117/USS19870930117_NS.MOR.00.SHZ.mseed")
st += read("../NNSN_archive/USS19870930117/USS19870930117_NS.ODD.00.SHZ.mseed")
st += read("../NNSN_archive/USS19870930117/USS19870930117_NS.SUE.00.SHZ.mseed")
t1  = UTCDateTime("1987-04-03T01:23:00")
t2  = UTCDateTime("1987-04-03T01:28:00")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
# st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 45.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "USS19870930117.png" )
exit(0)
