import constants  
import pdf_scrape

nc_test_text = pdf_scrape.convert_pdf_to_txt(constants.NORTH_CAROLINA_PDF, constants.NC_PAGE_NOS)

def split_text_by_place(txt):
  lines = txt.splitlines()
  
text_to_dct(nc_test_text) 
