import os
from bs4 import BeautifulSoup
from row import Row
import csv

folder = "data"
csv_rows=[]

def ninety_six(f):
  """
    Straight forward parsing of 1995-1996.html file
  """
  soup = BeautifulSoup(open(os.path.join(folder, f)), "html.parser")
  table = soup.findAll("table")[1]
  rows = table.findChildren(['tr'])
  
  for data in rows:
    # skip table headers
    if len(data.findChildren(["th"])) < 1:
      csv_rows.append(Row("1996", data, 0, 7))

def twenty_six(f):
  """
  The file I scraped for 2005-2006 data breaks correctional facilities into four categories
  with four corresponding tables. This loops through the four tables, retrieves the data, and tallys
  the incarcerated population of a given county 
  """
  soup = BeautifulSoup(open(os.path.join(folder, f)), "html.parser")
  
  for t in [8,12,14,15]:
    table = soup.findAll("table")[t]
    rows = table.findChildren(['tr'])
    handle_irregular(rows)

def twenty_fifteen(f):
  soup = BeautifulSoup(open(os.path.join(folder, f)), "html.parser")
  table = soup.findAll("table")[1]
  rows = table.findChildren(['tr'])
  
  for data in rows:
    # skip table headers
    if len(data.findChildren(["th"])) < 1:
      csv_rows.append(Row("2015", data, 0, 1))

def handle_irregular(rows):
  """
    Some ugly logic to handle 2005-2006 data.
  """
  
  for data in rows:
    if len(data.findChildren(["th"])) < 1:
      row = Row("2006", data, 6, 7)
      if any(r.year == "2006" and r.county == row.county for r in csv_rows) and row.county is not None:
        matching_row = next((match for match in csv_rows if match.year == "2006" and match.county == row.county ), None)
        matching_row.population = matching_row.population + row.population
      else:
        csv_rows.append(row)

def parse(filename):
  """
  Map the filename to a function and call the function. 
    1. The idea here is that if we want to add more counties later we can do so here
    2. also the assumption here is any scraped html can't be parsed the same way. 
  """
  file_map = {
      '1995-1996.html': ninety_six,
      '2005-2006.html': twenty_six,
      '2014-2015.html': twenty_fifteen
  }
  func = file_map.get(filename, lambda: "Invalid File")
  func(filename)

for filename in os.listdir(folder):
  """
  Loop through files in the data directory and parse them. 
  """
  parse(filename)

with open("prisonpop-by-county.csv", 'w') as csv_file:
    """ 
    classic csv writer
    """
    wr = csv.writer(csv_file, delimiter=',')
    wr.writerow(["Year", "County", "Population"])
    for cdr in csv_rows:
      if cdr.county is not None:
        wr.writerow([cdr.year,cdr.county,cdr.population])

