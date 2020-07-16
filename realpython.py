import requests
from bs4 import BeautifulSoup
from tutorial import Tutorial
# Scrapper
BASE_URL = 'https://realpython.com'
response = requests.get(BASE_URL) # realpython.com .....
response_content = response.content # click derecho ver código fuente de la página
soup = BeautifulSoup(response_content, features='html.parser')
tutorials = soup.find_all('div', class_='col-12 col-md-6 col-lg-4 mb-5')
tutorials_list = []
for t in tutorials:
    title = t.find('h2', class_='card-title')
    image = t.find('img', class_='card-img-top')
    anchor = t.find('a')
    anchor =  BASE_URL + anchor['href']
    new_tutorial = Tutorial(title.text, anchor, image['src'],"0")
    tutorials_list.append(new_tutorial)
# POO Almancenamos la información obtenida
for t in tutorials_list:
    components_image_url = t.url_image.split('/media/')
    image_file_name = components_image_url[1]
    remote_image_request = requests.get(t.url_image)
    remote_image_content = remote_image_request.content
    #Descargamos las imagenes con el siguiente codigo
    with open(f'temp/{image_file_name}', 'wb') as image_file:
        image_file.write(remote_image_content)
    

for item in tutorials_list:
    second_url=item.url
    response_url_article = requests.get(second_url) # realpython.com .....
    content_url_article = response_url_article.content # click derecho ver código fuente de la página
    soup2 =  BeautifulSoup(content_url_article, features='html.parser')
    articles_content = soup2.find_all('div',class_="article-body")
    text_list_tutorials=[]
    text_content=''
    for p in articles_content:
        text_content = text_content + p.text
    
    item.content=text_content
    print("saving data...")
    print(item.content)
    print("Successfully")