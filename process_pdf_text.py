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
  amenitites = pg_lst[0]
  utilities = pg_lst[0]

  market_rent = pg_list[-12]
  adjusted_rent = pg_lst[-9]
  
  return rv_property.Property(name, address, ity, state, zp, phone, email, age_range, ownership, jlt_notes, number_of_units, amenities, utilities, market_rent, adjusted_rent)

def process_text(txt):
  pg_lst = split_text_by_place(txt)
  print(pg_lst[0])

process_text(nc_test_text)
