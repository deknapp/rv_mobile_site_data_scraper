import rv_property

HEADER = ['Property Name', 'Property Address', 'Property City', 'Property State','Property Zip', 'Phone Number', 'Email', 'All Age / 55+', 'Ownership / Management', 'JLT Notes', 'Number of Units', 'Amenities', 'Utilities (Incl, Val, Des)', 'Rents (mkt, adj)']

def rent_string(rent_lst):
  cell_lst = []
  for rent in rent_lst:
    strng = rent.description + " " + rent.market + " " + rent.adjusted
    cell_lst.append(strng)
  return ",".join(cell_lst)
 
def amen_string(amens):
  return ",".join(amens)

def util_string(name, util):
  return name + " " + util.value + " " + description

def util_strings(utils):
  util_list = []
  util_list.append(util_string("Water", utils.water))
  util_list.append(util_string("Sewer", utils.sewer))
  util_list.append(util_string("Trash", utils.trash))
  util_list.append(util_string("Cable", utils.cable))
  util_list.append(util_string("Lawn", utils.cable))
  return ",".join(amens)

def write_property(handle, prop):
  line_lst = []
  line_lst.append(prop.name)
  line_lst.append(prop.adddress)
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
  for prop in property_list:
    write_property(handle, prop)  
  handle.close()


