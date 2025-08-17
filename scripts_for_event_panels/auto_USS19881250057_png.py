import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/USS19881250057/USS19881250057_NS.ASK1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19881250057/USS19881250057_NS.ASK2.00.SHZ.mseed")
st += read("../NNSN_archive/USS19881250057/USS19881250057_NS.ASK3.00.SHZ.mseed")
st += read("../NNSN_archive/USS19881250057/USS19881250057_NS.ASK4.00.SHZ.mseed")
st += read("../NNSN_archive/USS19881250057/USS19881250057_NS.ASK5.00.SHZ.mseed")
st += read("../NNSN_archive/USS19881250057/USS19881250057_NS.BER.00.SHZ.mseed")
st += read("../NNSN_archive/USS19881250057/USS19881250057_NS.BLS1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19881250057/USS19881250057_NS.BLS2.00.SHZ.mseed")
st += read("../NNSN_archive/USS19881250057/USS19881250057_NS.BLS3.00.SHZ.mseed")
st += read("../NNSN_archive/USS19881250057/USS19881250057_NS.HYA.00.SHZ.mseed")
st += read("../NNSN_archive/USS19881250057/USS19881250057_NS.KTK1.00.SLZ.mseed")
st += read("../NNSN_archive/USS19881250057/USS19881250057_NS.KTK2.00.SLZ.mseed")
st += read("../NNSN_archive/USS19881250057/USS19881250057_NS.KTK3.00.SLZ.mseed")
st += read("../NNSN_archive/USS19881250057/USS19881250057_NS.KTK5.00.SLZ.mseed")
st += read("../NNSN_archive/USS19881250057/USS19881250057_NS.KTK6.00.SLZ.mseed")
st += read("../NNSN_archive/USS19881250057/USS19881250057_NS.LOF.00.SLE.mseed")
st += read("../NNSN_archive/USS19881250057/USS19881250057_NS.LOF.00.SLN.mseed")
st += read("../NNSN_archive/USS19881250057/USS19881250057_NS.LOF.00.SLZ.mseed")
st += read("../NNSN_archive/USS19881250057/USS19881250057_NS.MOL.00.SLZ.mseed")
st += read("../NNSN_archive/USS19881250057/USS19881250057_NS.ODD1.00.SHZ.mseed")
st += read("../NNSN_archive/USS19881250057/USS19881250057_NS.TRO.00.SLZ.mseed")
t1  = UTCDateTime("1988-05-04T01:02:00")
t2  = UTCDateTime("1988-05-04T01:07:00")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
#st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 45.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "USS19881250057.png" )
exit(0)
