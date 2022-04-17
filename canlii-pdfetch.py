#!/usr/bin/python3

import csv
import re
import requests

# Field names
fields = ['citation', 'year', 'forum', 'decision']

# Name csv file
case_list = "case_list.csv"

p = re.compile(r'\b[0-9]{4}\s[a-zA-Z]{,8}\s[0-9]+\b')

with open('target.txt') as f:
    iterator = p.findall(f.read())

with open(case_list, 'w') as csvfile:

    # Creating csv writer object
    csvwriter = csv.writer(csvfile)
              
    # Write fields
    csvwriter.writerow(fields)
    
    # Write matches to csv and download pdfs
    for hit in iterator:

        # Create list elements
        row = [hit]
        cite_parts = hit.split()
        row += cite_parts
        csvwriter.writerow(row)

        # Variables for constructing url
        citation = row[0].lower()
        citation_joined = ''.join(citation.split()).lower()
        year = row[1].lower()
        forum = row[2].lower()

        # Create variables for forum special cases
        if forum == 'scc' or forum == 'fc' or forum == 'fca':
            juris = 'ca'
        else:
            juris = forum[0:2]

        if forum == 'fc':
            forum = 'fct'

        # Download from url
        url = f'https://www.canlii.org/en/{juris}/{forum}/doc/{year}/{citation_joined}/{citation_joined}.pdf'.lower()
        url_content = requests.get(url, stream=True)
        print(f'Downloading {citation} ...')
        print(url)

        # Save downloaded pdfs
        filename = citation_joined + '.pdf'
        with open(filename, 'wb') as f:
            f.write(url_content.content)
