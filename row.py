from bs4 import BeautifulSoup

class Row(object):
  """
  This is a class to build each row of data.  
    1. The idea behind the class is that its an easy way to extend 
       the row if we want more data in the future
  """

  def __init__(self, year, row, county, pop):
    self.year = year
    self.data = row
    self.county = self.get_county(county)
    self.population = self.get_population(pop)

  def get_county(self, county):
    """
      retrieves the county from the table row.  
        1. It includes an exception for 2006, whose table differs from other years.
    """
    if self.year == '2006':
      if len(self.data.findAll(["td"])) == 8:
        return self.data.findAll(["td"])[county].text.lstrip()
    else:
      return self.data.findAll(["td"])[county].text.lstrip()
  
  def get_population(self, pop):
    if self.year == '2006':
      if len(self.data.findAll(["td"])) == 8:
        clean = self.data.findAll(["td"])[pop].text.lstrip().replace(',', '')
        return int(clean)
    else:
      clean = self.data.findAll(["td"])[pop].text.lstrip().replace(',', '')
      return int(clean)

