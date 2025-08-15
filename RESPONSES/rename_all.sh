#!/bin/sh
for file in *_XML.txt
do
  station=`basename $file _XML.txt`
  outfile=${station}.xml
  mv $file $outfile
done
