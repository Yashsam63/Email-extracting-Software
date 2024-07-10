# what should this software can do 
# 1 in your given data if there are website link , email address both are present then it will print result .
# 2 if in your data there is only email is present and there is no website link  is present  then it will also print result.
# 3 if in your data there is only website link  is present and there is no email is present then it will skip that line .

# this module will give email address to  more prefrence other than website link .

# the  list of modules to run this code and you can directley run this in your terminal one by one :-
# pip install requests
# pip install beautifulsoup4  
# pip install render 
# pip install workbook 
# pip install whois
# pip install re 
# pip install openpyxl
# pip install pandas 
# pip install os


# in case by installing modules you are facing a error then check your pip version and upgraded it by runing this code in terminal
# -m pip install --upgrade pip


import re
from openpyxl import Workbook
import os

# enter yor raw data here
mixed_data = """

"""


# the code will starts here 


email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
website_pattern = r'https?://[^\s]+'

# for creating a new workbook
wb = Workbook()
ws = wb.active
ws.append(["Business Name", "Website", "Email Address"])

sections = mixed_data.strip().split('\n\n')

for section in sections:
    lines = section.strip().split('\n')
    business_name = lines[0].strip()  # First line is business name
    
    website = ''
    email = ''
    
    for line in lines[1:]:
        if re.search(email_pattern, line):
            email = re.search(email_pattern, line).group(0).strip()
        elif re.search(website_pattern, line):
            website = re.search(website_pattern, line).group(0).strip()
    
    #only work if email is present and if email is not present then skip 
    if email:
        ws.append([business_name, website, email])

# permanent file name
base_filename = "business_contacts_yash"

# Generate a unique filename
counter = 1
while True:
    filename = f"{"business_contacts_yash"}_{counter}.xlsx"
    
    # Checking  if the file already exists or not
    if not os.path.exists(filename):
        break
    
    # add number if the file exists
    counter += 1

# Save the workbook with the unique filename
wb.save(filename)

print(f"Excel file saved as: {filename}")
