from tika import parser

raw_text = parser.from_file('Park.pdf')
pdf_text = raw_text['content']

with open('park2017.txt','w') as file2:
    file2.write(pdf_text)