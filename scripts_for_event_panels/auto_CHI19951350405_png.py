import obspy
from obspy import read
from obspy import UTCDateTime
# from obspy import read_inventory
st  = obspy.Stream()
st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.BLS5.00.SHE.mseed")
st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.BLS5.00.SHN.mseed")
st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.BLS5.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.FOO.00.SHE.mseed")
st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.FOO.00.SHN.mseed")
st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.FOO.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.HYA.00.SHE.mseed")
st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.HYA.00.SHN.mseed")
# st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.HYA.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.KMY.00.SHE.mseed")
# st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.KMY.00.SHN.mseed")
st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.KMY.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.KONO.00.BVE.mseed")
st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.KONO.00.BVN.mseed")
st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.KONO.00.BVZ.mseed")
st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.KONO.00.LN.mseed")
st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.LOF.00.SHE.mseed")
st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.LOF.00.SHN.mseed")
st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.LOF.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.MOL.00.SHE.mseed")
st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.MOL.00.SHN.mseed")
st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.MOL.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.MOR8.00.SHE.mseed")
st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.MOR8.00.SHN.mseed")
st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.MOR8.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.NSS.00.SHE.mseed")
st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.NSS.00.SHN.mseed")
st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.NSS.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.SUE.00.SHE.mseed")
st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.SUE.00.SHN.mseed")
st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.SUE.00.SHZ.mseed")
st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.TRO.00.SHE.mseed")
st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.TRO.00.SHN.mseed")
st += read("../NNSN_archive/CHI19951350405/CHI19951350405_NS.TRO.00.SHZ.mseed")
#
# We need to fix the first sample on a number of the traces
#
numchan = len( st )
for ichan in range(0,numchan):
    st[ichan].data[0] = st[ichan].data[1]
#
t1  = UTCDateTime("1995-05-15T04:13:00")
t2  = UTCDateTime("1995-05-15T04:18:00")
st.plot( equal_scale = False, size = [900, 800],
         starttime = t1, endtime = t2 )
#st.plot( equal_scale = False, size = [900, 800] )
numchan = len( st )
yaxlen  = 45.0 * numchan
st.plot( equal_scale = False, size = [900, yaxlen],
         starttime = t1, endtime = t2, outfile = "CHI19951350405.png" )
exit(0)
