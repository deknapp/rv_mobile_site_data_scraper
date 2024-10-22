import rv_property
import write_csv_file
import constants
import pdf_scrape
import process_pdf_text

def scrape_pdf(pdf_name, output_csv):
  print("getting text")
  txt = pdf_scrape.convert_pdf_to_txt(pdf_name)
  print("printing property list")
  prop_lst = process_pdf_text.property_lst(txt)
  print("writing csv file: " + output_csv)
  write_csv_file.write_property_csv(output_csv, prop_lst)

# for testing
#scrape_pdf(constants.NORTH_CAROLINA_PDF, '/Users/nknapp/Desktop/Scraping_Contract_Upwork/nc_test.csv') 
  
