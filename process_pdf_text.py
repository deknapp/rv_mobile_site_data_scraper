import constants  
import pdf_scrape
import rv_property

nc_test_text = pdf_scrape.convert_pdf_to_txt(constants.NORTH_CAROLINA_PDF)

def split_text_by_place(txt):
  pg_lst = []
  lines = txt.splitlines()
  current_lst = [lines[0]]
  for line in lines[1:]: 
    if constants.PG_SEP in line:
      pg_lst.append(current_lst)
      current_lst = []
    current_lst.append(line)  
  return pg_lst[1:]

def amenities(pg_lst):
  lst = []
  for amen in rv_property.AMENITIES_LIST:
    if amen in pg_lst:
      lst.append(amen)
  return ' '.join(lst) 

def index_from_key(pg_lst, key):
  val = pg_lst[0]
  i = 0
  while key not in val:
    i += 1         
    if i > len(pg_lst) - 1:
      print("ERROR: key not found: " + key )
    val = pg_lst[i]
  return i

def val_from_previous(pg_lst, key, distance=1):
  i = 0
  for item in pg_lst:
    if key == item:
      return pg_lst[i+distance] 
    i=i+1
  print("ERROR: cannot find key " + key + "in list")

def yn_to_bool(val):
  if val == 'Yes':
    return True
  elif val == 'No':
    return False
  else:
    print("ERROR: invalid Yes/No")

def util_from_index(pg_lst, base_i):
  return rv_property.Utility(pg_lst[base_i], pg_lst[base_i+8], pg_lst[base_i+16])

def utilities(pg_lst): 
  base_index = index_from_key(pg_lst, 'Service')
  water = util_from_index(pg_lst, base_index+1)
  sewer = util_from_index(pg_lst, base_index+2)
  trash = util_from_index(pg_lst, base_index+3)
  cable = util_from_index(pg_lst, base_index+4)
  lawn = util_from_index(pg_lst, base_index+5)
  return rv_property.Utilities(water, sewer, trash, cable, lawn)

def property_from_page(pg_lst):

  try:
    community_info_index = index_from_key(pg_lst, 'Community Information')
  except:
    exit() 
  name = pg_lst[community_info_index + 1]
  print(name)
  address = pg_lst[community_info_index + 2]
  city_state_zip = pg_lst[community_info_index + 3].split()
  
  if len(city_state_zip) < 3:
    print("city state zip failed for : " + name)
    city = ''
    state = ''
    zp = ''
  else:
    city = city_state_zip[0] 
    state = city_state_zip[1]
    zp = city_state_zip[2]
  
  phone = pg_lst[community_info_index + 4]
  age_range = pg_lst[community_info_index + 6]

  # TODO  
  email = '' 
  ownership = ''

  notes_index = index_from_key(pg_lst, 'Notes')
  notes = ''
  i = notes_index + 1
  while 'Community Amenities' not in pg_lst[i]:
    notes = notes + pg_lst[i]
    i += 1
  jlt_notes = notes 

  try:
    number_of_units = val_from_previous(pg_lst, 'Multiple Section', distance=7)
  except:
    number_of_units = ''
    print("number of units failed for " + name)

  try:
    amens = amenities(pg_lst)
  except:
    print("amenities failed for " + name)

  try:
    utils = utilities(pg_lst)
  except:
    utils = ''
    print("utils failed for " + name) 

  try:
    market_rent = val_from_previous(pg_lst, 'Market Rent') 
  except:
    market_rent = ''
    print("market rent failed for " + name) 

  try:
    adjusted_rent = val_from_previous(pg_lst, 'Adjusted', distance=2)
  except:
    adjusted_rent = ''
    print("market rent failed for " + name) 

  # TODO: make this work for rents more generally 
  rents = [rv_property.Rent(market_rent, adjusted_rent, '')] 
 
  return rv_property.Property(name, address, city, state, zp, phone, email, age_range, ownership, jlt_notes, number_of_units, amens, utils, rents)

def property_lst(txt):
  pg_lst = split_text_by_place(txt)
  prop_lst = []
  for pg in pg_lst:
    print("=====================")
    try:
      prop = property_from_page(pg)
    except:
      continue
    prop_lst.append(prop)
    for line in pg:
      print(line)
  return prop_lst

