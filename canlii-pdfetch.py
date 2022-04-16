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


