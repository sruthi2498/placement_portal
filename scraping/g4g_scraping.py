import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

driver = webdriver.Firefox()
driver.get("https://www.geeksforgeeks.org/")

interview=driver.find_element_by_xpath("//li[@id='menu-item-142017']/a")
hover = ActionChains(driver).move_to_element(interview)
hover.perform()
interview_exp=driver.find_element_by_xpath("//li[@id='menu-item-137173']/a")
interview.click()


delay=1
try:
	all_companies = driver.find_elements_by_xpath("//li[@class='sLiClass']/a")
	all_companies_page=driver.current_url
	print("all companies")
	j=0
	while(j<len(all_companies)):
		all_companies = driver.find_elements_by_xpath("//li[@class='sLiClass']/a")
		comp=all_companies[j]
		name=comp.text.strip()[:len(comp.text)-6]
		print("company ",j,comp.text)
		comp.click()
		try:
			found_all=0
			page=1
			while(found_all==0):
				questions=driver.find_elements_by_xpath("//h2[@class='entry-title']/a")
				i=0
				while(i<len(questions)):
					questions=driver.find_elements_by_xpath("//h2[@class='entry-title']/a")
					print("\tpage ",page,"Q ",i,questions[i].text)
					questions[i].click()
					i=i+1
					driver.back()
				next_page=driver.find_elements_by_xpath("//a[@class='nextpostslink']")
				if(len(next_page)>0):
					page=page+1
					next_page[0].click()

				else:
					found_all=1
					
		except Exception as e:
			print(e)
		j=j+1
		driver.get(all_companies_page)
except Exception as e:
	print(e)



