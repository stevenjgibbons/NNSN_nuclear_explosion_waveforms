import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/USS19902971457/USS19902971457_NS.ASK.00.SHE.mseed")
st += read("../NNSN_archive/USS19902971457/USS19902971457_NS.ASK.00.SHN.mseed")
st += read("../NNSN_archive/USS19902971457/USS19902971457_NS.ASK.00.SHZ.mseed")
st += read("../NNSN_archive/USS19902971457/USS19902971457_NS.BER.00.SHZ.mseed")
st += read("../NNSN_archive/USS19902971457/USS19902971457_NS.BLS1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19902971457/USS19902971457_NS.BLS2.00.SHZ.mseed")
st += read("../NNSN_archive/USS19902971457/USS19902971457_NS.HYA.00.SHZ.mseed")
st += read("../NNSN_archive/USS19902971457/USS19902971457_NS.KTK1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19902971457/USS19902971457_NS.KTK2.00.SHZ.mseed")
st += read("../NNSN_archive/USS19902971457/USS19902971457_NS.KTK3.00.SHZ.mseed")
st += read("../NNSN_archive/USS19902971457/USS19902971457_NS.KTK4.00.SHZ.mseed")
st += read("../NNSN_archive/USS19902971457/USS19902971457_NS.KTK5.00.SHZ.mseed")
st += read("../NNSN_archive/USS19902971457/USS19902971457_NS.KTK6.00.SHZ.mseed")
st += read("../NNSN_archive/USS19902971457/USS19902971457_NS.LOF.00.SHE.mseed")
st += read("../NNSN_archive/USS19902971457/USS19902971457_NS.LOF.00.SHN.mseed")
st += read("../NNSN_archive/USS19902971457/USS19902971457_NS.LOF.00.SHZ.mseed")
st += read("../NNSN_archive/USS19902971457/USS19902971457_NS.MOR7.00.SHE.mseed")
st += read("../NNSN_archive/USS19902971457/USS19902971457_NS.MOR7.00.SHN.mseed")
st += read("../NNSN_archive/USS19902971457/USS19902971457_NS.MOR7.00.SHZ.mseed")
st += read("../NNSN_archive/USS19902971457/USS19902971457_NS.SUE.00.SHZ.mseed")
t1  = UTCDateTime("1990-10-24T14:59:30")
t2  = UTCDateTime("1990-10-24T15:04:30")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
#st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 45.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "USS19902971457.png" )
exit(0)
