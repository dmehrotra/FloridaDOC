#!/bin/bash

# Trap ctrl-c and call ctrl_c() in case you want to exit the script
trap ctrl_c INT

function ctrl_c() {
  echo "** Exiting **"
  exit 1
}

# simple curl to Data Urls to save the data for later use. 
curl -sS https://web.archive.org/web/20161007124555/http://www.dc.state.fl.us:80/pub/annual/1415/stats/ip_county_commitment.html > data/2014-2015.html

curl -sS https://web.archive.org/web/20070703225954/http://www.dc.state.fl.us:80/pub/annual/0506/facil.html > data/2005-2006.html

curl -sS https://web.archive.org/web/20150905112906/http://www.dc.state.fl.us/pub/annual/9596/stats/ipt2.html > data/1995-1996.html

exit 0
