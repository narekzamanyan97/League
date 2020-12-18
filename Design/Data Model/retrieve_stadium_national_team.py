# COMPLETE

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time


#4) stadium name
#	https://en.wikipedia.org/wiki/List_of_national_stadiums
#	stadium_image_url
#	https://en.wikipedia.org/wiki/Estadio_Monumental_Antonio_Vespucio_Liberti

CITY = 3
STADIUM_NAME = 4 #CLICKABLE
CAPACITY = 5
BUILT_DATE = 6

opts = Options()
opts.set_headless = True
driver = webdriver.Firefox(options=opts)
driver.get('http://www.worldstadiums.com/')

time.sleep(3)

#click on the continent
continent_buttons = driver.find_elements_by_xpath("//td[@bgcolor='#e6e6ff']/a")
continent_buttons[3].click()

time.sleep(5)

#driver_1 = driver_1.page_source
#latest_window = driver.window_handles[1]
#driver.switch_to(window(latest_window))
#source_code = driver.page_source

country_buttons = driver.find_elements_by_xpath("//td[@class='text']/a")
num_of_countries = len(country_buttons)


for i in range(0, num_of_countries):
	name_of_country = country_buttons[i].get_attribute('innerHTML');
	
	#also update
	# belarus - Dinamo Stadion
	# czech republick - Sinobo Stadium
	# poland - pge narodowy
	# portugal - estadio do sport lisboa e benfika 
	# sweden - friends arena
	# switzerland - st. jakob-arena


	if name_of_country != 'Iceland' and name_of_country != 'Lithuania' and name_of_country != 'Moldova' and name_of_country != 'Monaco':

		print(name_of_country)
		

		country_buttons[i].click()


		time.sleep(3)

		#determine whether the stadium is for football or not
		#'/world_stadiums/images/icons/soccer.gif'
		# or
		# '/world_stadiums/images/icons/multi.gif'
		stadium_type_row = driver.find_elements_by_xpath("//table[@width='650']/tbody/tr/td/img")

		
		#there is one more img, which is the heading, so the number of stadiums
		#is 1 less than the number of images
		num_of_stadiums = len(stadium_type_row)
		#print(len(stadium_type_row))

		for j in range(1, num_of_stadiums):
			stadium_type = stadium_type_row[j].get_attribute('alt')
			continue_ = False
			if stadium_type == 'Football' or stadium_type == 'Multi-use' or stadium_type == 'Rugby' or stadium_type == 'Gaelic Football/Hurling':
				index = j
				
				parent_row = stadium_type_row[index].find_elements_by_xpath('../..')[0]

			#	#######################################################################
			#							get the stadium name
			#	#######################################################################	
				stadium_name_col = parent_row.find_elements_by_tag_name('td')[STADIUM_NAME]
				#print("*** " + str(stadium_name_col.find_elements_by_tag_name('a')[0].get_attribute('innerHTML')))																					 	
				#if str(stadium_name_col.find_elements_by_tag_name('a')[0].get_attribute('innerHTML')) != 'Iceland':
				#if name_of_country != 'Iceland' and name_of_country != 'Lithuania':
				print("name: " + str(stadium_name_col.find_elements_by_tag_name('a')[0].get_attribute('innerHTML')))

				stadium_name_col.click()


				try:
					stadium_name_col.click()
					stadium_name_col.click()
					#	should have thrown an error. If does not, skip the iteration, looking
					#   for the next stadium that we can click
					print("continue is executed")
					continue_ = True 
					#continue

				finally:
					if(continue_ == False):
						time.sleep(3)
					
					#	#######################################################################
						#		get the image url
					#	#######################################################################
					
						stadium_image_url = driver.find_elements_by_xpath("//img")
						#print(driver.current_url)
						#base_url = driver.current_url[0:driver.current_url.rindex('/')]
						#print(base_url)
						#stadium_image_url = base_url + 
						#print(stadium_image_url[5].get_attribute('outerHTML'))
						
						stadium_image_url_1 = stadium_image_url[5].get_attribute('src') 
						print(stadium_image_url_1)

						stadium_image_url_2 = stadium_image_url[6].get_attribute('src') 
						print(stadium_image_url_2)						


						#image_name = stadium_image_url[6]['src']
						#print(image_name)
						#print(stadium_image_url[6]['src'])
						driver.back()

						time.sleep(3)

						stadium_type_row = driver.find_elements_by_xpath("//table[@width='650']/tbody/tr/td/img")

						parent_row = stadium_type_row[index].find_elements_by_xpath('../..')[0]

					#	#######################################################################
					#							get the city
					#	#######################################################################	
						print("city: " + str(parent_row.find_elements_by_tag_name('td')[CITY].get_attribute('innerHTML')))


						
					#	#######################################################################
					#							get the capacity
					#	#######################################################################	
						print("capacity: " + str(parent_row.find_elements_by_tag_name('td')[CAPACITY].get_attribute('innerHTML')))


					#	#######################################################################
					#							get the built date
					#	#######################################################################	
						print("built: " + str(parent_row.find_elements_by_tag_name('td')[BUILT_DATE].get_attribute('innerHTML')))



						driver.back()

						time.sleep(3)

						print("***************************************************************")

						country_buttons = driver.find_elements_by_xpath("//td[@class='text']/a")
						break
