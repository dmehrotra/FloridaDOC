# Prison Population in Florida 

Scripts to retrieve prison population from the web archive and to parse them into a csv.  (( Broken down by county. ))

### Requirements
  - python 3, csv, os, bs4
### Installation
```sh
$ git clone https://github.com/dmehrotra/FloridaDOC.git # clones the repo
$ cd FloridaDOC
$ chmod +x get_data.sh # makes the get data script runnable
$ pip3 install bs4 
$ python3 parse.py # this will write a csv file called prisonpop-by-county
```
