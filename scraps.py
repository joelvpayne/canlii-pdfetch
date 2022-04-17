# -- -- Code for extracting style of cause from downloaded PDF  
#import PyPDF2
#import re

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

# -- -- Scraps from original pdfetch script
import requests
import os
import subprocess
import webbrowser

# Ask user for citation to fetch
citation = input("Enter the citation of the case to fetch: \n").lower()

print ('Downloading ...')

# Check for and remove spaces
if ' ' in citation:
    citation = citation.replace(' ', '')

# Break citation down into elements for reconstructing url
year = citation[:4]
court = citation[4:8]
juris = court[0:2]

# Construct the url from user input and download
url = f'https://www.canlii.org/en/{juris}/{court}/doc/{year}/{citation}/{citation}.pdf'
# CanLII url format: https://www.canlii.org/en/bc/bcsc/doc/2021/2021bcsc32/2021bcsc32.pdf
url_content = requests.get(url, stream=True)

# Print variables for troubleshooting
print(url)
print(citation)

# Rename and save pdf
filename = citation + '.pdf'

with open(filename, 'wb') as f:
    f.write(url_content.content)

open_or_exit = input('Fetch complete. Open it now? \n'
'Type "B" to open in your web browser \n'
'Type "P" to open in your PDF viewer \n'
'Type "N" to exit: \n').lower()

if open_or_exit == 'b':
    webbrowser.open_new(filename)
elif open_or_exit == 'p':
    #subprocess.Popen([filename], shell=True)
    subprocess.call(["xdg-open", filename])
elif open_or_exit == 'n':
    exit()
else:
    exit()


# -- -- Scraps from citation_regex
import re

p = re.compile(r'((\b[0-9]{4})(\s)([a-zA-Z]{,8})(\s)([0-9]+\b))')
m = p.search('hello:2021 bcsc 2, the dogs ran away')

if m:
    print('Match found: ', m.group())
    year = m.group(2)
    forum = m.group(4)
    decision = m.group(6)
    citation = m.group(0)
    juris = forum[0:2]
    print(m)
    print(year, forum, decision, citation)
    print(juris)
    
else:
    print('No match')



