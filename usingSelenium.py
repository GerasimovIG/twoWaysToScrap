#Подход через Selenium, рабочий
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
req_proxy = RequestProxy() #you may get different number of proxy when  you run this at each time
proxies = req_proxy.get_proxy_list() #this will create proxy list

from selenium import webdriver

def workingDriver():
    for proxy in proxies:
        PROXY = proxy.get_address()
        webdriver.DesiredCapabilities.CHROME['proxy']={
            "httpProxy":PROXY,
            "ftpProxy":PROXY,
            "sslProxy":PROXY,
            
            "proxyType":"MANUAL",
            
        }
        driver = webdriver.Chrome( executable_path=r"C:\ProgramData\Anaconda3\Lib\site-packages\selenium\webdriver\chromedriver.exe")
        driver.get('https://gilya.ru')
        try:
            resp = driver.find_element_by_tag_name('body').get_attribute('innerHTML')
            print ('Got response successfully')
        except:
            print ('Response exception')
            driver.close()
        if 'Нет подключения к Интернету' in resp or 'Соединение сброшено' in resp:
            print ('Response: could not connect')
            driver.close()
        else:
            print ('Driver is ready for work!')
            return driver


driver = workingDriver()
print (driver.find_element_by_tag_name('head').get_attribute('innerHTML'))
