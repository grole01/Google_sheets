import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
from parsel import Selector
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import gspread
import pandas as pd



#chromeOptions=Options()
#chromeOptions.add_argument("--headless")

driver = webdriver.Chrome(ChromeDriverManager().install())#, options=options)
driver.get("https://www.sgdi.gov.sg/ministries/mci/departments/au")

#soup= BeautifulSoup(driver.page_source,"html.parser")
sel = Selector(text=driver.page_source)
info=sel.xpath("/html/body/form/div[6]//ul/li")

data2=[]
for quote in info:
    name=quote.xpath(".//span[1]/div[2]/text()").extract_first()
    #print((quote.xpath(".//span[2]/div[1]/text()").extract_first()).join(quote.xpath(".//span[2]/div[1]/u/text()").extract_first()))
    tel=quote.xpath(".//span[2]/div[1]/u/text()").extract_first().join(quote.xpath(".//span[2]/div[1]/text()").extract_first())
    mail=quote.xpath(".//span[2]/div[2]/text()").extract_first()

    data={
        "Name" : name,
        "Tel" : tel,
        "Email" : mail
    }
    print(data)
    data2.append(data)

    df=pd.DataFrame(data2)

    gc = gspread.service_account(filename="creds.json")
    sh = gc.open("scrapetosheet").sheet1



    #sh.update("A1","test")
    sh.update([df.columns.values.tolist()] + df.values.tolist())
driver.close()


