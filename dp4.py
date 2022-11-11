import os
from PyPDF2 import PdfFileMerger
from tika import parser

#if we want to merge all pdf files in a directory using PdfFileMerger
pdf_files = [file for file in os.listdir() if file.endswith(".pdf")]

#create an object
merger = PdfFileMerger()

#combine all pdf files
for pdf_file in pdf_files:
    merger.append(pdf_file)
    
#write it to one file 
merger.write("combined.pdf")

#clean up the mess: temp files created over the course of the project
merger.close()