from selenium import webdriver
from lxml import html
import csv
from selenium.webdriver.chrome.service import Service
s = Service(r'C:\Users\Dream\PycharmProjects\Projects\Drivers\chromedriver.exe') #Path of chromedriver.exe
driver = webdriver.Chrome(service=s)
for page_nb in range(1, 60): #range of the pages for the searched products in AliExpress.com
    url ='https://www.aliexpress.com/premium/camera.html?trafficChannel=ppc&d=y&CatId=0&SearchText=camera&ltype=premium&SortType=default&page={}'.format(page_nb) #Url used with the page number range
    driver.get(url) #calling the url
    driver.implicitly_wait(2) #wait
    elements = html.fromstring(driver.page_source)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') #function to scroll to the end of the page to load all products
    driver.implicitly_wait(2) #wait
    for element in elements.xpath('.//a[@class="_3KNwG _2f4Ho"]'): #Defining the search blocks using the xpath
        title = element.xpath('.//h1[@class="_3eC3x"]/text()') #xpath to get the title of each product
        price = element.xpath('.//div[contains(@class ,"_13_ga _37W_B")]/text()') #xpath to get the price of each product
        sold = element.xpath('.//span[@class="_2tU1w"]/text()') #xpath to get how many unit was sold of each product
        review = element.xpath('.//span[@class="ZwoRt"]/text()') #xpath to get the reviews of each product
        shipping = element.xpath('.//span[@class="_1XYdp"]/text()') #xpath to get the shipping cost of each product
        f = open('products.csv', 'a', newline='', encoding='utf-8') #opening the products.csv file to put our extracted information into it
        writer = csv.writer(f)
        writer.writerow(["title:"]) #writing title in the file
        writer.writerow(title) #writing the information extracted using the xpath of the titles
        writer.writerow(["review:"]) #writing review in the file
        writer.writerow(review) #writing the information extracted using the xpath of the reviews
        writer.writerow(["sales:"]) #writing sales in the file
        writer.writerow(sold) #writing the information extracted using the xpath of the units sold
        writer.writerow(["price:"]) #writing price in the file
        writer.writerow(price) #writing the information extracted using the xpath of the prices
        writer.writerow(["shipping:"]) #writing shipping in the file
        writer.writerow(shipping) #writing the information extracted using the xpath of the shipping cost


