from tkinter import Tk, Label, Button, messagebox
import main_pdf

FILE_MSG = 'Choose a file or list of files to process'
CSV_FILE_FOLDER = 'Choose a folder for output files to be stored'

class PdfScrapeGUI:
  def __init__(self, master):
    self.master = master
    self.file_list = None
    self.output_folder = None
    master.title("Scrape Market Report PDF")

    self.label = Label(master, text="This is our first GUI!")
    self.label.pack()

    self.select_file_button = Button(master, text="Select PDF File(s) To Scrape", command=self.select_input_files)
    self.select_file_button.pack()

    self.select_folder_button = Button(master, text="Select Output Folder", command=self.select_output_folder)
    self.select_folder_button.pack()
    
    self.close_button = Button(master, text="Close", command=master.quit)
    self.close_button.pack()    

    def select_input_files(self):
      root = tk.Tk()
      filez = tk.filedialog.askopenfilenames(parent=root,title=FILE_MSG)
      self.file_list = root.tk.splitlist(filez)
    
    def select_output_folder(self):
      root = tk.Tk()
      self.output_folder = tk.filedialog.askdirectory(parent=root,title=CSV_FILE_FOLDER)
    
    def scrape(self):
      if self.output_folder is None:
        messagebox.showinfo("Error", "You must select an output folder")        
        return

      if self.file_list is None:
        messagebox.showinfo("Error", "You must select input PDF file(s)")        
        return

      for fle in self.file_list:
        output_file_name = self.output_folder + '/' + fle.split('.pdf')[0] + '.csv'
      try:
        main_pdf.scrape_pdf(fle, output_file_name)
      except:
        pass
  
root = Tk()
my_gui = PdfScrapeGUI(root)
root.mainloop()




 
