#!/bin/sh
while read line
do
  outfile=${line}_XML.txt
 wget -O ${outfile} http://eida.geo.uib.no/fdsnws/station/1/query?station=${line}\&starttime=1980-01-01\&endtime=2023-01-01\&level=response
done < stations_only.txt
