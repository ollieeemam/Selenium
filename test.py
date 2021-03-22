import cgi
import os
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import importlib
import array as arr
"""
driver = webdriver.Chrome(executable_path="C://Users/ollie/eclipse-workspace/chromedriver.exe")
url = "https://smartours.com/new-tours/"

driver.get(url)
driver.maximize_window()
time.sleep(2)
print("Title: "+driver.title)

links = driver.find_elements_by_css_selector("a")
# for link in links:
#     if link:
#         print(link.text)
#     else:
#         print("--empty link--")

# print(links)
print("Total Links are: "+str(len(links)))
attributeText = driver.find_element_by_xpath("//span[@class='ubermenu-target-title ubermenu-target-text']").get_attribute("class")
print(attributeText)

time.sleep(2)
driver.quit()
"""


"""
# Reversed printing
for line in reversed(range(10)):
    print(line, end=' ')
print()

    def test_getD_Data(rowindex, colindex):
        tableRow = driver.find_element_by_xpath("<Table tag xpath>").find_element_by_tag_name('tr')
        tabledimention = tableRow[rowindex+1].find_element_by_tag_name('td')
        return tabledimention[colindex].get_attribute('innetText')
    
    actions = ActionChains(driver)
    actions.send_keys_to_element(element, '')
    
    import random
    line=open("").read().splitlines("")
    random.choice(line)
"""

# lists = list(os.chdir("C:/Users/ollie/OneDrive/Desktop/Python-Interviews/address.txt"))
# for line in reversed(10):
#     print(line.rstrip())

a=0
while(a<5):
    val = 0
    while(val<=a):
        val = val +1
        print(str(val), end = '')
    a = a + 1
    print()


# Array
arrs = arr.array('u', ['H','O','E','o','k', '\u2641','Y'])
print(type(arrs))
for c in arrs:
    print(c, end=' ')
print(type(arrs))


ar = arr.array('f', [100,27,33,44,49,76,303])
for a in ar:
    print(a, end=' ')
print(type(ar))

list = [1,'abc',1.20, 'Code', 65.650, None, 'Hi', 879]
for l in list:
    print(l, end=' ')

print(type(list))
print(list[::-1])



class ABC:
    ss='call me'
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname

    def abc(self, fn, ln):
        print(self.fn+" "+self.ln)
        print(self.ss)
    print(ss)


a = ABC("Eeara", "Eemam")
print("Last name: "+a.lname)
print("First name: "+a.fname)
print("Class Level Variable: "+a.ss)



















