import requests
import PyPDF2
import re

# Ask user for citation to fetch
requested_cite = input("Enter the citation of the case to fetch: \n")
cite_split = requested_cite.split()
print(cite_split)

year = cite_split[0]
court = cite_split[1]
juris = court[0:2]
case_no = cite_split[2]
citation = ''.join(cite_split)

print(requested_cite)
print(juris)
print(citation)

# Construct the url from user input and download
url = 'https://www.canlii.org/en/' + juris + '/' + court + '/doc/2021/' + citation + '/' + citation + '.pdf'
# CanLII url format: https://www.canlii.org/en/bc/bcsc/doc/2021/2021bcsc32/2021bcsc32.pdf
r = requests.get(url, stream=True)

print(url)

# Rename and save pdf
filename = citation + '.pdf'

with open(filename, 'wb') as f:
    f.write(r.content)
        
# Create pdf file object
#pdf_file_object = open(filename, 'rb')
    
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
