import rv_property
import csv_file
import constants

def scrape_pdf(pdf_name, page_nos, output_csv):
  txt = pdf_scrape.convert_pdf_to_txt(pdf_name, page_nos)
  prop_lst = process_pdf_text.property_lst(txt)
  csv_file.write_csv_file(output_csv, prop_lst)

scrape_pdf(constants.NORTH_CAROLINA_PDF, constants.NC_PAGE_NOS, '/Users/nknapp/Desktop/Scraping_Contract_Upwork/nc_test.csv') 
  
