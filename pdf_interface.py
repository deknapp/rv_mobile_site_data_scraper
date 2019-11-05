from tkinter import filedialog, messagebox
import tkinter as tk 
import main_pdf

FILE_MSG = 'Choose a file or list of files to process'
CSV_FILE_FOLDER = 'Choose a folder for output files to be stored'

class PdfScrapeGUI:

  def __init__(self, parent):
    self.parent = parent
    self.file_list = None
    self.output_folder = None
    parent.title("Scrape Market Report PDF")

    self.select_file_button = tk.Button(parent, text="Select PDF File(s) To Scrape", command=lambda: self.select_input_files())
    self.select_file_button.pack()

    self.select_folder_button = tk.Button(parent, text="Select Output Folder", command=lambda: self.select_output_folder())
    self.select_folder_button.pack()
    
    self.scrape_button = tk.Button(parent, text="Scrape PDFs", command=lambda: self.scrape())
    self.scrape_button.pack()
    
    self.close_button = tk.Button(parent, text="Close", command= parent.quit)
    self.close_button.pack()    

  def select_input_files(self):
    filez = filedialog.askopenfilenames(title=FILE_MSG)
    self.file_list = root.tk.splitlist(filez)
  
  def select_output_folder(self):
    self.output_folder = filedialog.askdirectory(title=CSV_FILE_FOLDER)
  
  def scrape(self):
    print("starting to scrape")

    if self.output_folder is None:
      print("ERROR: no output folder")
      messagebox.showinfo("Error", "You must select an output folder")        
      return

    if self.file_list is None:
      print("ERROR: file list is None")
      messagebox.showinfo("Error", "You must select input PDF file(s)")        
      return

    if len(self.file_list) == 0:
      print("ERROR: no files in file list")
      return

    for fle in self.file_list:
      output_file_name = self.output_folder + '/' + (fle.split('/')[-1]).split('.pdf')[0] + '.csv'
    try:
      main_pdf.scrape_pdf(fle, output_file_name)
    except:
      pass
    
    print("done scraping")

if __name__ == "__main__":  
  root = tk.Tk()
  my_gui = PdfScrapeGUI(root)
  root.mainloop()




 
