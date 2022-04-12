import requests
import PyPDF2
import re

# Ask user for citation to fetch
citation = input("Enter the citation of the case to fetch: \n")

# Construct the url from user input and download
url = 'https://www.canlii.org/en/bc/bcsc/doc/2021/' + citation + '/' + citation + '.pdf'
# CanLII url format: https://www.canlii.org/en/bc/bcsc/doc/2021/2021bcsc32/2021bcsc32.pdf
r = requests.get(url, stream=True)

# Rename and save pdf
#temp_filename = 'temp_' + citation + '.pdf'
temp_filename = citation + '.pdf'

with open(temp_filename, 'wb') as f:
    f.write(r.content)
        
# Create pdf file object
#pdf_file_object = open(temp_filename, 'rb')
    
# Create pdf reader object
#pdf_reader_object = PyPDF2.PdfFileReader(pdf_file_object)
        
# Create page object
#page_object = pdf_reader_object.getPage(0)
                
# Extract text from page
#first_page_text = page_object.extractText()
#file = open('first_page_text.txt', 'a')
#file.write(first_page_text)
#file.close

# Search extracted text for first name in style of cause
#s = first_page_text
#party_name_regex = re.search(r'Citation:( [a-zA-Z]+ )v.', s).group(1)
#party_name_regex = re.search(r'Citation:\s+(.+\n)', s).group(1)



#print(party_name_regex)

# closing the pdf file object
#pdf_file_object.close()
