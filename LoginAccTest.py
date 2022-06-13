#Kotronis Triantafyllos
#Run pip install selenium
#Download selenium driver from https://github.com/mozilla/geckodriver/releases
#And place in " C:\Windows\Temp" and also to project file

from time import sleep                       # add delay in the execution of a program
from selenium import webdriver               #browser automation library
from selenium.webdriver.common.by import By  # attributes which can be used to locate elements

username = "kotronis.dataverse@gmail.com"
password = "D@t@verse2022"
url = "https://gmail.com"

def is_element_present(xpath):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except :
        return False

#8.	Write a method to get the name of the sender and subject of email of your inbox.
def get_name_subject(n):
    name = driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[8]/div/div[1]/div[3]/div/table/tbody/tr["+str(n)+"]/td[4]/div[2]/span/span").text   
    emailSubject = driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[8]/div/div[1]/div[3]/div/table/tbody/tr["+str(n)+"]/td[5]/div/div/div/span/span").text
    return name, emailSubject

# 1.Open a browser of your choice say Mozilla Firefox using Gecko Driver
driver = webdriver.Firefox(executable_path="C:\\Users\\Toa11\\DataverseTest\\geckodriver")
#2.	Navigate to Gmail (https://www.gmail.com)
driver.get(url)
#3.	Login to your Gmail with correct credentials.
driver.find_element(By.ID, "identifierId").send_keys(username)
sleep(3) 
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span").click()
sleep(2)
driver.find_element(By.NAME, "password").send_keys(password)
sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span").click()
sleep(2)

#4.	Verify that by default “Primary” section is selected.
titleTab = driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[5]/table/tbody/tr[1]/td[1]/div/div[5]").text

if titleTab == "Primary":
    print("Login correct and selected Tab is Primary!")
else:
    print("Not in Primery tab")
    driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[5]/table/tbody/tr[1]/td[1]/div/div[5]").click()

# 6.Get the count of the total number of emails in the Primary tab.
i=1
while is_element_present("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[8]/div/div[1]/div[3]/div/table/tbody/tr["+str(i)+"]/td[4]/div[2]/span/span"):
    i +=1
print("Total Emails :", i-1) 

#7.	Get the name of the sender and subject of Nth Email of your inbox.
NthEmail = get_name_subject(5)
print ("Name : "+ NthEmail[0]+"  Subject: "+NthEmail[1])

