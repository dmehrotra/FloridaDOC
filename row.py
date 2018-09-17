from bs4 import BeautifulSoup

class Row(object):
  """
  """

  def __init__(self, year, row):
    self.year = year
    self.county = self.get_county(row)


  def get_county(self, row):
    if self.year != '2006':
      return row.findAll(["td"])[0]
    
    




