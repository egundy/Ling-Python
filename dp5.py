import os
from docx import Document
from docxcompose.composer import Composer

word_files = [file for file in os.listdir() if file.endswith(".docx")]

master = Document("word_merge.docx")
composer = Composer(master)

for word_file in word_files:
    doc = Document(word_file)
    #appending the source document to the end of the destination document
    composer.append(doc)

composer.save("word_merge.docx")