sed 's/\./ /g' allfiles.txt | awk '{print $2}' | sort | uniq > stations_only.txt
