import requests
from bs4 import BeautifulSoup
import csv



def write_to_csv(data):
    with open('data.csv', 'a')as file:
        write = csv.writer(file)
        write.writerow([data['title'], data['price'],data['image']])

def get_html(url):
    response = requests.get(url)
    return response.text 


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_ = 'pager-wrap').find('ul',class_ = 'pagination').find_all('li')
    # print(pages)
    last_page = pages[-1].text
    return int(last_page)


get_total_pages(get_html('https://www.kivano.kg/mobilnye-telefony'))    

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    telefony = soup.find('div', class_ = "list-view").find_all('div', class_= "item")
    for telefon in telefony:
        title = telefon.find('div', class_= 'listbox_title oh').find('strong').text
        price = telefon.find('div', class_ = 'listbox_price').find('strong').text
        image = 'https://www.kivano.kg/' + telefon.find('img').get('src')
        

        dict_ ={'title':title, 'price':price, 'image': image} 
        write_to_csv(dict_) 

with open('data.csv', 'w')as file:
    write = csv.writer(file)
    write.writerow(['     title     ', '           price             ','             image           '])


def main():
    url = 'https://www.kivano.kg/mobilnye-telefony'  
    html = get_html(url)
    get_data(html)
    pages = '?page' 
    number = get_total_pages(html)
    i = 1
    while i <= number:
        url_page = url + pages + str(i)
        i += 1
        html = get_html(url_page)
        get_data(html)
        print(i)

  


main()    


     
   



      
                
           


                      