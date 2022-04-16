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
