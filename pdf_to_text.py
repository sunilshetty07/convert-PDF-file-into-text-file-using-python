# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 17:40:39 2018

@author: Sunil
"""

import tkinter as tk
import PyPDF2
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo
import pathlib


window=tk.Tk()
window.title("PDF to text converter")

def openfile():
    file=askopenfile(filetypes=[('PDF Files','*.pdf')])
    pdf_file=open(file.name,'rb')
    read_pdf=PyPDF2.PdfFileReader(pdf_file)
    no_of_pages=read_pdf.getNumPages()
    page=read_pdf.getPage(0)
    page_content=page.extractText()
    pathlib.Path('context.txt').write_text(page_content)
    showinfo("Done","Successfully Converted")
    
label=tk.Label(window,text="choose file: ")
label.grid(row=0,column=0,padx=5,pady=5)

button=ttk.Button(window,text="Select",width=30,command=openfile)
button.grid(row=0,column=1,padx=5,pady=5)

window.mainloop()
