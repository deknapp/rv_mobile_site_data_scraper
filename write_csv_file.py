import rv_property

HEADER = ['Property Name', 'Property Address', 'Property City', 'Property State','Property Zip', 'Phone Number', 'Email', 'All Age / 55+', 'Ownership / Management', 'JLT Notes', 'Number of Units', 'Amenities', 'Utilities (Incl, Val, Des)', 'Rents (mkt, adj)']

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
 
def amen_string(amens):
  return " ".join(amens)

def util_string(name, util):
  return name + " " + util.value + " " + util.description

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
  line_lst.append(amen_string(prop.amenities))
  line_lst.append(utils_string(prop.utilities))
  line_lst.append(rent_string(prop.rents))
  line = ','.join(line_lst) + '\n'
  handle.write(line)

def write_property_csv(csv_name, property_lst):
  handle = open(csv_name, 'w')
  header_line = ' '.join(HEADER)
  handle.write(header_line)
  for prop in property_lst:
    write_property(handle, prop)  
  handle.close()


