import constants  
import pdf_scrape
import rv_property

def split_text_by_place(txt):
  pg_lst = []
  lines = txt.splitlines()
  current_lst = [lines[0]]
  for line in lines[1:]: 
    if constants.PG_SEP in line:
      pg_lst.append(current_lst)
      current_lst = []
    current_lst.append(line)  
  pg_lst.append(current_lst)
  return pg_lst[1:]

def amenities(pg_lst):
  lst = []
  for amen in rv_property.AMENITIES_LIST:
    if amen in pg_lst:
      lst.append(amen)
  return ' '.join(lst) 

def index_from_key(pg_lst, key, name =''):
  val = pg_lst[0]
  i = 0
  while key not in val and key != val:
    i += 1         
    if i > len(pg_lst) - 1:
      print("ERROR: key not found: " + key + name)
      return -1
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

def process_val(val):
  if len(val.split()) > 1:
    return val.split()[0]
  return val
 
def util_from_index(pg_lst, base_i):
  included_in_rent = pg_lst[base_i+8]
  return rv_property.Utility(included_in_rent, '', '')

def add_util_value(pg_lst, utils):
  vals = get_util_values(pg_lst)
  i = 0  
  if i+1 > len(vals):
    return utils
  if 'Yes' in utils.water.included_in_rent:
    utils.water.value = vals[i]
    i = i + 1   
  if i+1 > len(vals):
    return utils
  if 'Yes' in utils.sewer.included_in_rent:
    utils.sewer.value = vals[i]
    i = i + 1   
  if i+1 > len(vals):
    return utils
  if 'Yes' in utils.trash.included_in_rent:
    utils.trash.value = vals[i]
    i = i + 1   
  if i+1 > len(vals):
    return utils
  if 'Yes' in utils.cable.included_in_rent:
    utils.cable.value = vals[i]
    i = i + 1   
  if i+1 > len(vals):
    return utils
  if 'Yes' in utils.lawn.included_in_rent:
    utils.lawn.value = vals[i]
  return utils

def get_util_descr(pg_lst):
  descrs = []
  for itm in pg_lst:
    for d in constants.UTIL_DESCRS:
      if d in itm:
        descrs.append(d)
  return descrs            

def add_util_descr(pg_lst, utils):
  vals = get_util_descr(pg_lst)
  print(vals)
  if len(vals) > 0: 
    utils.water.description = vals[0]
  if len(vals) > 1: 
    utils.sewer.description = vals[1]
  if len(vals) > 2: 
    utils.trash.description = vals[2]
  return utils

def get_between(pg_lst, start, end):
  if start == '' or end == '':
    return ''
  start_i = index_from_key(pg_lst, start) 
  end_i = index_from_key(pg_lst, end) 
  if start_i == -1 or end_i == -1:
    return ''
  between = ''
  for i in range(start_i+1, end_i):
    between = between + pg_lst[i]
  return between

def get_notes(pg_lst):
  notes = []
  for itm in pg_lst: 
    for key in constants.NOTES_KEYS:
      if key in itm:
        notes.append(itm)
        break
  return " ".join(notes)

def get_util_values(pg_lst):
  between = get_between(pg_lst, 'Description', 'Site Type')
  if '$' not in between:
    return []
  dollar_split_between = between.split('$')
  vals = [itm.split()[0] for itm in dollar_split_between[1:]]
  return [''.join(c for c in item if c.isdigit()) for item in vals] 

def utilities(pg_lst): 
  base_index = index_from_key(pg_lst, 'Service')
  water = util_from_index(pg_lst, base_index+1)
  sewer = util_from_index(pg_lst, base_index+2)
  trash = util_from_index(pg_lst, base_index+3)
  cable = util_from_index(pg_lst, base_index+4)
  lawn = util_from_index(pg_lst, base_index+5)
  utils = rv_property.Utilities(water, sewer, trash, cable, lawn)
  utils = add_util_value(pg_lst, utils)
  utils = add_util_descr(pg_lst, utils)
  return utils

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
  management = ''
  for item in pg_lst:
    if '.com' in item:
      email = item
    if 'Owned by' in item:
      ownership = ' '.join(item.split()[2:])
    if 'Managed by' in item:
      management = ' '.join(item.split()[2:])
  
  if ownership == '' and management == '':
    ownership = ''
  else:
    ownership = ownership + ' / ' + management    

  jlt_notes = get_notes(pg_lst) 

  try:
    number_of_units = val_from_previous(pg_lst, 'Multiple Section', distance=5)
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

  try: 
    prop = rv_property.Property(name, address, city, state, zp, phone, email, age_range, ownership, jlt_notes, number_of_units, amens, utils, rents)
  except:
    print("prop constructor failed")
    exit()
  
  if 'Meadowbrook' in name:
    for itm in pg_lst:
      print(itm)
  return prop
  
def property_lst(txt):
  prop_lst = []
  pg_lst = split_text_by_place(txt)
  for pg in pg_lst:
    try:
      prop = property_from_page(pg)
      prop_lst.append(prop)
    except:
      continue
  return prop_lst

