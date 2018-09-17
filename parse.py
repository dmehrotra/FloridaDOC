import os
from bs4 import BeautifulSoup
from row import Row

folder = "data"

def ninety_six(filename):
  soup = BeautifulSoup(open(os.path.join(folder, filename)), "html.parser")
  table = soup.findAll("table")[1]
  rows = table.findChildren(['tr'])
  for data in rows:
    if len(data.findChildren(["th"])) < 1:
      print(Row("1996",data).county)

def twenty_six(filename):
    return "February"

def twenty_fifteen(filename):
    return "March"

def parse(argument):
    file_map = {
        "1995-1996.html": ninety_six(filename),
        "2005-2006.html": twenty_six(filename),
        "2014-2015.html": twenty_fifteen(filename)
    }
    # Get the function from switcher dictionary
    func = file_map.get(argument, lambda: "Invalid File")
    # Execute the function
    print (func())

for filename in os.listdir(folder):
  parse(filename)








# import code; code.interact(local=dict(globals(), **locals()))
