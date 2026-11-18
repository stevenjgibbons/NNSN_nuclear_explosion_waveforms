#!/bin/sh
scriptname=./resp_remove_one_file.sh
if [ $# != 2 ]
then
  echo
  echo "USAGE: "
  echo "$scriptname  longfile                                             respfile "
  echo "$scriptname  USS19902971457/USS19902971457_NS.MOR7.00.SHZ.mseed  RESPONSES/MOR7.xml"
  echo "$scriptname  USS19902971457/USS19902971457_NS.MOR7.00.SHZ.mseed  RESPONSES/NNSNUNT.xml"
  echo "$scriptname  USS19883390519/USS19883390519_NS.KTK2.00.SLZ.mseed  RESPONSES/KTK2.xml"
  echo "$scriptname  CHI19921420459/CHI19921420459_NS.FRO.00.SHZ.mseed   RESPONSES/FRO.xml"
  echo "$scriptname  USS19902971457/USS19902971457_NS.BLS1.00.SHZ.mseed  RESPONSES/BLS1.xml"
  echo "$scriptname  USS19902971457/USS19902971457_NS.BLS2.00.SHZ.mseed  RESPONSES/BLS2.xml"
  echo "$scriptname  USS19881250057/USS19881250057_NS.BLS3.00.SHZ.mseed  RESPONSES/BLS3.xml"
  echo "$scriptname  USS19890220357/USS19890220357_NS.BLS4.00.SHZ.mseed  RESPONSES/BLS4.xml"
  echo "$scriptname  CHI19932780159/CHI19932780159_NS.BER.00.SLZ.mseed   RESPONSES/BER.xml"
  echo "$scriptname  CHI19932780159/CHI19932780159_NS.BER.00.SHZ.mseed   RESPONSES/BER.xml"
  echo "$scriptname  CHI19921420459/CHI19921420459_NS.JMI.00.SLZ.mseed   RESPONSES/JMI.xml"
  echo "$scriptname  CHI19921420459/CHI19921420459_NS.JMI.00.SHZ.mseed   RESPONSES/JMI.xml"
  echo
  exit 1
fi
#
longfile=../clones/NNSN_nuclear_explosion_waveforms/ARCHIVE/$1
if test ! -r $longfile
then
  echo No file $longfile found ...
  exit 1
fi
respfile=../clones/NNSN_nuclear_explosion_waveforms/$2
if test ! -r $respfile
then
  echo No file $respfile found ...
  exit 1
fi
dir=`dirname $longfile`
line=`awk '$1 == EVID' EVID=$dir all_events_origins.txt | sed 's/ /    /g'`
shortfile=`basename $longfile .mseed`
outfile="png_files"/$dir'_'$shortfile'.png'
cat << EOF > writer.py
import obspy
from obspy import read
from obspy import read_inventory
st = read("${longfile}")
inv = read_inventory("${respfile}")
dt  = st[0].stats.delta
dnyquist = 0.5 / dt
freq3    = dnyquist * 0.8
pre_filt = [0.001, 0.005, freq3, dnyquist]
st.remove_response(inventory=inv, pre_filt=pre_filt, output="DISP",
                   water_level=60, plot=True)
st[0].stats.channel = st[0].stats.channel + "                      $line"
st.plot( )
# st.plot( outfile = "$outfile" )
exit()
EOF
echo $line
python writer.py
