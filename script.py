import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Make a GET request
url = 'https://www.classcentral.com/'
response = requests.get(url)

# Parsing
soup = BeautifulSoup(response.content, 'html.parser')

# Extracting Data
course_titles = [course.find('h2').text for course in soup.find_all(
    'div', {'class': 'search-result'})]

# Translating using Google Translate
translator = Translator(service_urls=['translate.google.com'])
hindi_titles = [translator.translate(
    title, dest='hi').text for title in course_titles]

# Modifying and replacing
for i, title in enumerate(hindi_titles):
    course_title_div = soup.find_all(
        'div', {'class': 'search-result'})[i].find('h2')
    course_title_div.string.replace_with(title)

# saving the new translated webpage
with open('classcentral_hindi.html', 'w', encoding='utf-8') as f:
    f.write(str(soup.prettify()))
