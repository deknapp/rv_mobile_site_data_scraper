import rv_property
import os

HEADER = ['Property Name', 'Property Address', 'Property City', 'Property State','Property Zip', 'Phone Number', 'Email', 'All Age / 55+', 'Ownership / Management', 'JLT Notes', 'Number of Units', 'Amenities', 'Utilities (Incl Val Des)', 'Rents (mkt adj)']

DELIMITER = ','

def rent_string(rent_lst):
  cell_lst = []
  for rent in rent_lst:
    if rent.description is None:
      rent.description = ''
    if rent.market is None:
      rent.market = ''
    if rent.adjusted is None:
      rent.adjusted = ''
    strng = rent.description + " " + rent.market + " " + rent.adjusted
    cell_lst.append(strng)
  return " ".join(cell_lst)
 
def util_string(name, util):
  return name + " " + util.included_in_rent + " " + util.value + " " + util.description

def utils_string(utils):
  if not isinstance(utils, rv_property.Utilities):
    return '' 
  util_list = []
  util_list.append(util_string("Water", utils.water))
  util_list.append(util_string("Sewer", utils.sewer))
  util_list.append(util_string("Trash", utils.trash))
  util_list.append(util_string("Cable", utils.cable))
  util_list.append(util_string("Lawn", utils.cable))
  return " ".join(util_list)

def clean_commas(prop):
  return prop.replace(',', '   ')

def write_property(handle, prop):
  line_lst = []
  line_lst.append(prop.name)
  line_lst.append(prop.address)
  line_lst.append(prop.city)
  line_lst.append(prop.state)
  line_lst.append(prop.zip)
  line_lst.append(prop.phone)
  line_lst.append(prop.email)
  line_lst.append(prop.age_range)
  line_lst.append(prop.ownership)
  line_lst.append(prop.jlt_notes)
  line_lst.append(prop.number_of_units)
  line_lst.append(prop.amenities)
  line_lst.append(utils_string(prop.utilities))
  line_lst.append(rent_string(prop.rents))
  line_lst = [clean_commas(item) for item in line_lst] 
  line = DELIMITER.join(line_lst) + '\n'
  handle.write(line)

def write_property_csv(csv_name, property_lst):
  try:
    os.system('rm ' + csv_name)
  except:
    pass    
  handle = open(csv_name, 'w')
  header_line = DELIMITER.join(HEADER) + '\n'
  handle.write(header_line)
  for prop in property_lst:
    write_property(handle, prop)  
  handle.close()


