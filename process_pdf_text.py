import constants  
import pdf_scrape
import rv_property

nc_test_text = pdf_scrape.convert_pdf_to_txt(constants.NORTH_CAROLINA_PDF, constants.NC_PAGE_NOS)

def split_text_by_place(txt):
  pg_lst = []
  lines = txt.splitlines()
  current_lst = [lines[0]]
  for line in lines[1:]: 
    if constants.PG_SEP in line:
      pg_lst.append(current_lst)
      current_lst = []
    current_lst.append(line)  
  return pg_lst

def amenities(pg_lst):
  lst = []
  for amen in rv_property.AMENITIES_LIST:
    if amen in pg_lst:
      lst.append(amen)
  return lst.join(' ') 

def index_from_key(pg_lst, key):
  val = pg_lst[0]
  i = 0
  while val != key:
    i += 1         
    val = key[i]
  return i

def val_from_previous(pg_lst, key):
  i = 0
  for item in pg_lst:
    if key in item:
      return pg_lst[i+1] 
    i=i+1
  print("ERROR: cannot find key " + key + "in list")
  exit() 

def yn_to_bool(val):
  if val == 'Yes':
    return True
  elif val == 'No':
    return False
  else:
    print("ERROR: invalid Yes/No")
  exit()

def util_from_index(pg_lst, base_i):
  return rv_property.Utility(pg_lst[base_i], pg_lst[base_i+7], pg_lst[base_i+14])

def utilities(pg_lst):
  first_yes_no_index = min(index_from_key(pg_lst, 'Yes'), index_from_key(pg_lst, 'No'))
  water = util_from_index(pg_lst, first_yes_no_index)
  sewer = util_from_index(pg_lst, first_yes_no_index+1)
  trash = util_from_index(pg_lst, first_yes_no_index+2)
  cable = util_from_index(pg_lst, first_yes_no_index+3)
  lawn = util_from_index(pg_lst, first_yes_no_index+4)
  return Utilities(water, sewer, trash, cable, lawn)

def property_from_page(pg_lst):
  name = pg_lst[5]
  address = pg_lst[6]
  
  city_state_zip = pg_lst[7].split()
  city = city_state_zip[0] 
  state = city_state_zip[1]
  zp = city_state_zip[2]
  
  phone = pg_lsts[8]
  age_range = pg_lst[10]
  
  email = pg_lst[0]
  
  ownership = pg_lst[0]
  jlt_notes = pg_lst[15] + pg_lst[16]

  number_of_units = pg_lst[0]
  amenities = amenities(pg_lst)
  utilities = utilities(pg_lst)

  market_rent = val_from_previous('Market Rent') 
  adjusted_rent = val_from_previous('Adjusted Rent')
  
  return rv_property.Property(name, address, ity, state, zp, phone, email, age_range, ownership, jlt_notes, number_of_units, amenities, utilities, market_rent, adjusted_rent)

def property_lst(txt):
  pg_lst = split_text_by_place(txt)
  prop_lst = []
  for pg in pg_lst:
    prop_lst.append(property_from_page(pg))
  return prop_lst

process_text(nc_test_text)
