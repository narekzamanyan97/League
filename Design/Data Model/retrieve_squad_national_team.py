# COMPLETE (with few things to be added)

# import requests
# from bs4 import BeautifulSoup


from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time
import re



urls = {
	'url_1': 'https://www.transfermarkt.us/wettbewerbe/fifa/wettbewerbe', #for squads
	'url_2': 'https://www.national-football-teams.com/national.html',  #for uniform			  
}

def retrieve_squad_national_team(confederation):
	if confederation == 'UEFA':

		opts = Options()
		opts.set_headless = True
		driver = webdriver.Firefox(options=opts)
		driver.get(urls['url_1'])

		#	vereinprofil_tooltip tooltipstered
		POSITION_TEAM = 0
		NAME_TEAM = 1
		TOTAL_VALUE_TEAM = 4
		CONFEDERATION_TEAM = 5

		#country_buttons = driver.find_elements_by_xpath("//a[@class='vereinprofil_tooltip tooltipstered']")
		#country_buttons = driver.find_elements_by_xpath("//td[@class='hauptlink']")

		#26-50

		pager = driver.find_elements_by_xpath("//div[@class='pager']/ul[@id='yw2']/li/a")

		time.sleep(3)
		#pager[PAGE_2].click()

		for page_number in range (0, 9):
			#if page_number == 0 or page_number == 1:
			driver.execute_script("arguments[0].click();", pager[page_number])
			#else:
			#	driver.execute_script("arguments[0].click();", pager[page_number + 2])

			time.sleep(3)

			pager = driver.find_elements_by_xpath("//div[@class='pager']/ul[@id='yw2']/li/a")
			#print(pager[page_number].get_attribute('outerHTML'))




			table_teams = driver.find_elements_by_xpath("//tbody/tr")

			# PAGE 1: 1-25
			#print('len:' + str(len(table_teams)))
			number_of_teams_on_the_page = len(table_teams)

			for k in range(number_of_teams_on_the_page - 1, number_of_teams_on_the_page):
			
				#print('table_teams = ' + str(table_teams[k].get_attribute('innerHTML')))
				team = table_teams[k].find_elements_by_tag_name('td')
				
				#print(team[NAME].get_attribute('innerHTML'))

				#print('position = ' + str(rows[POSITION].get_attribute('innerHTML')))
				print('position = ' + str(team[POSITION_TEAM].text))
				print('-')

				#print('******' + str(team[POSITION].get_attribute('outerHTML')))
				name = team[NAME_TEAM].find_elements_by_tag_name('a')
				#print('name = ' + str(name))
				#print('************** ' + str(name[0].get_attribute('innerHTML')))
				#print('name = ' + str(rows[NAME].get_attribute('innerHTML')))
				print('name = ' + str(name[1].get_attribute('innerHTML')))
				print('-')

				print('total_value = ' + str(team[TOTAL_VALUE_TEAM].get_attribute('innerHTML')))
				print('-')

				print('confederation = ' + str(team[CONFEDERATION_TEAM].get_attribute('innerHTML')))

				#click on team's name
				driver.execute_script("arguments[0].click();", name[1])

				time.sleep(3)

				#######################################################################
				#							squad data
				#######################################################################

			

				#market_value = driver.find_elements_by_xpath("//div[@class='dataMarktwert']/a/span[@class='waehrung']")
				# market_value = driver.find_elements_by_xpath("//div[@class='dataMarktwert']/a")
				# print('market_value = ' + str(market_value[0].text))

				# 							formation
				formation_row = driver.find_elements_by_xpath("//div[@class='large-7 aufstellung-vereinsseite columns small-12 unterueberschrift aufstellung-unterueberschrift']")
				#print(formation_row[0])
				formation_row = formation_row[0].get_attribute('innerHTML')
				formation_row = formation_row.rstrip().lstrip()
				#print('formation row: ' + str(formation_row))
				formation = formation_row.split(' ')								#
				# formation = formation[2]
				print('formation: ' + formation[2])

				# 							label substitutes and players
				squad = driver.find_elements_by_xpath("//div[@class='large-7 columns small-12 aufstellung-vereinsseite']/div[@style='position: absolute; top: 0; bottom: 0; left: 0; right: 0;']/div[@class='aufstellung-spieler-container']")
				#squad = driver.find_elements_by_xpath("//div[@class='large-7 columns small-12 aufstellung-vereinsseite']")
				#print("squad: " + squad[0].get_attribute('innerHTML'))
				#squad = 

				

				counter = 0

				name_and_numbers = []
				dictionary = {}

				for s in squad:
					# print(str(counter) + ") " + str(s.text))
					st = s.text
					name_number = st.split('\n')


					number = name_number[0]
					name = name_number[1]

					dictionary = {}
					dictionary['number'] = number
					dictionary['name'] = name
			
					name_and_numbers.append(dictionary)								#



					counter += 1
				
				#print(name_and_numbers)
				#print(name_and_numbers)

				print("************************Squad*******************")
				for name_and_number in name_and_numbers:
					print(str(name_and_number['number']) + "  " + str(name_and_number['name']))	

				#######################################################################

				#######################################################################
				#							substitutes data
				#######################################################################
				substitutes = driver.find_elements_by_xpath("//div[@class='large-5 columns small-12 aufstellung-ersatzbank-box aufstellung-vereinsseite']/table[@class='ersatzbank']/tbody/tr")
				name_and_numbers_sub = []
				dictionary_sub = {}
				print("***************************Substitutes***********************")
				for subs in substitutes:
					sub = subs.find_elements_by_tag_name('td')
					#print(str(sub[0].text) + "  " + str(sub[1].text))
					
					# st = sub.text
					# name_number = st.split('\n')

					sub_number = sub[0].text
					sub_name = sub[1].text
					

					# print(sub_number)
					# print(sub_name)

					dictionary_sub = {}
					dictionary_sub['number'] = sub_number
					dictionary_sub['name'] = sub_name
					name_and_numbers_sub.append(dictionary_sub)						#

					# print(sub[0].text)
					# print(sub[1].text)
					# print('-------------------------------')

					#!!! last one is the manager, so don't append it to the dictionary_sub
				#print(name_and_numbers_sub)
				for name_and_number_sub in name_and_numbers_sub:
					number = name_and_number_sub['number']
					name = name_and_number_sub['name']
					print(str(number) + "  " + str(name))
				

				#######################################################################
				#							manager data
				#######################################################################
				#slider-list
				table_managers = driver.find_elements_by_xpath("//div[@class='large-4 columns']/div[@class='box box-slider']/div[@class='clearer']")
				table_managers = driver.find_elements_by_xpath("//div[@class='container-inhalt']/div[@class='container-hauptinfo']/a")

				manager_name = table_managers[0].get_attribute('innerHTML')			#
				print("manager_name: " + str(manager_name))

				driver.execute_script("arguments[0].click();", table_managers[0])

				time.sleep(4)

				manager_info = driver.find_elements_by_xpath("//div[@id='trainer_head']/div[@class='large-12 columns']/div[@class='dataHeader']/div[@class='dataContent']")
				manager_info = manager_info[0].find_elements_by_tag_name('span')
				
				# for info in manager_info:
				# 	print(str(counter) + ") " + str(info.get_attribute('innerHTML')))
				# 	counter += 1

				manager_date_of_birth = manager_info[1].get_attribute('innerHTML')	
				manager_place_of_birth = manager_info[4].get_attribute('innerHTML')
				manager_citizenship = manager_info[7].get_attribute('innerHTML')
				manager_preferred_formation = manager_info[17].get_attribute('innerHTML')



				manager_date_of_birth = re.sub(' +', ' ', manager_date_of_birth)
				m = manager_date_of_birth.split()

				manager_date_of_birth_month = m[0]									#
				manager_date_of_birth_day = m[1].replace(',', '')					#
				manager_date_of_birth_year = m[2]									#
				manager_date_of_birth_age = m[3].replace('(', '').replace(')', '')	#

				
				print("manager_date_of_birth: ")
				print("	month: " + str(manager_date_of_birth_month))
				print("	day: " + str(manager_date_of_birth_day))
				print("	year: " + str(manager_date_of_birth_year))
				print("	age: " + str(manager_date_of_birth_age))

				print("manager_place_of_birth: " + str(manager_place_of_birth))
				print("manager_citizenship: " + str(manager_citizenship))
				print("manager_preferred_formation: " + str(manager_preferred_formation))
				#print('manager_info: ' + manager_info[0].get_attribute('innerHTML'))


				# get manager's photo
				manager_info = driver.find_elements_by_xpath("//div[@id='trainer_head']/div[@class='large-12 columns']/div[@class='dataHeader']/div[@class='dataBild']")
				print('************************Photo')
				manager_photo = manager_info[0].find_elements_by_tag_name('img')[0].get_attribute('src')
				print("manager_photo: " + str(manager_photo))
				#print(manager_info[0].get_attribute('innerHTML'))

				driver.back()

				time.sleep(4)
				######################################################################

				#table_players = driver.find_elements_by_xpath("//div[class='responsive-table']/div[@class='grid-view']/table[@class='items']/tbody/tr")
				table_players = driver.find_elements_by_xpath("//table[@class='items']/tbody/tr")
				squad_size = len(table_players)
				


				#print('***** ' + str(len(table_players)))
				
				######################################################################
				######################################################################

				for i in range(squad_size - 1, squad_size):
					#print(i)
					print('------------------------------------------')
					print('------------------------------------------')
					print('------------------------------------------')

					player = table_players[i].find_elements_by_tag_name('td')

					NATIONAL_TEAM_NUMBER = 0
					POSITION = 4
					NAME = 5
					MARKET_VALUE = 8

					national_team_number = player[NATIONAL_TEAM_NUMBER].text
					position = player[POSITION].get_attribute('innerHTML')
					name = player[NAME].get_attribute('innerHTML')
					market_value = player[MARKET_VALUE].text

					print('number: ' + str(national_team_number))
					print('position: ' + str(position))
					print('name: ' + str(name))
					print('market value: ' + str(market_value))


					player_link = player[1].find_elements_by_xpath("//table[@class='inline-table']/tbody/tr/td[@class='hauptlink']/div/span/a")
					#print('link: ' + str(player_link[0].get_attribute('href')))
					
					#print(player[1].get_attribute('outerHTML'))
					driver.execute_script("arguments[0].click();", player_link[2*i])

					time.sleep(4)


					#######################################################################
					#							player data
					#######################################################################
					player_data = driver.find_elements_by_xpath("//div[@class='row']/div[@class='large-12 columns']/div[@class='dataHeader dataExtended']/div")
					
					#print(player_data[2].get_attribute('outerHTML'))
					#player_data[2].find_elements_by_tag_name('img')

					#					 player image
					player_image = player_data[2].find_elements_by_tag_name('img')[0].get_attribute('src')    #
					#print(player_data[2].find_elements_by_tag_name('img')[0].get_attribute('src'))
					print('player_image: ' + str(player_image))

					#####################################################################
					# 					player date_of_birth
					player_info = player_data[1].find_elements_by_xpath("//div[@class='dataBottom']")
					player_dob = player_info[0].find_elements_by_tag_name('span')
					
					player_date_of_birth = player_dob[1].get_attribute('innerHTML').rstrip().lstrip()
					player_date_of_birth = re.sub(' +', ' ', player_date_of_birth)
					p = player_date_of_birth.split()

					player_date_of_birth_month = p[0]									#
					player_date_of_birth_day = p[1].replace(',', '')					#
					player_date_of_birth_year = p[2]									#
					player_date_of_birth_age = p[3].replace('(', '').replace(')', '')	#
					
					print('month: ' + player_date_of_birth_month)
					print('day: ' + player_date_of_birth_day)
					print('year: ' + player_date_of_birth_year)
					print('age: ' + player_date_of_birth_age)
					#print(player_date_of_birth)
					#print(player_dob[1].get_attribute('innerHTML').rstrip().lstrip())

					#####################################################################
					# 					player place_of_height
					#print(player_info[0].get_attribute('innerHTML'))
					player_height = player_info[0].find_elements_by_tag_name('span')
					
					if player_height[8].get_attribute('innerHTML') == 'Height:':
						height = player_height[9].get_attribute('innerHTML') 				#
						print('height: ' + str(height))
					#print(player_info[0])
					#player_height = player_info[0]

					#####################################################################
					# 					player total value
					# player_info = player_data[4].find_elements_by_tag_name('a')

					# #player_total_value = player_info[0].find_elements_by_tag_name('span')
					# #player_total_value = player_info[0].get_attribute('innerHTML')
					
					# player_total_value = player_info[0].text 						
					# player_tot_val_list = player_total_value.split(' ')
					# player_total_value = player_tot_val_list[0].split('\n')
					# player_total_value = player_total_value[0]						#
					# print('total_value: ' + str(player_total_value))
					#print('*** ' + str(player_total_value[1].get_attribute('innerHTML')))

					#####################################################################
					# 					place of birth
					player_info = player_data[1].find_elements_by_xpath("//div[@class='dataBottom']/div")
					
					player_place_of_birth = player_info[0].find_elements_by_tag_name('span')
					
					#if player_place_of_birth[3]
					if player_place_of_birth[2].get_attribute('innerHTML') == 'Place of birth:':
						player_place_of_birth_city = player_place_of_birth[4].get_attribute('innerHTML')	#
						print('place_of_birth: ' + str(player_place_of_birth_city))
					

					driver.back()

					time.sleep(4)

					table_players = driver.find_elements_by_xpath("//table[@class='items']/tbody/tr")




				print('********************************')

				driver.back()

				time.sleep(4)

	
				#pager = driver.find_elements_by_xpath("//div[@class='pager']/ul[@id='yw2']/li/a")
				#print(pager[page_number].get_attribute('outerHTML'))

				table_teams = driver.find_elements_by_xpath("//tbody/tr")

				#team = table_teams[k + 1].find_elements_by_tag_name('td')
				######################################################################
				######################################################################

			driver.back()

			time.sleep(4)

			pager = driver.find_elements_by_xpath("//div[@class='pager']/ul[@id='yw2']/li/a")

			time.sleep(3)

			#driver.back()

			#time.sleep(3)

			#pager[page_number].click()
			




def main():
	retrieve_squad_national_team('UEFA')





if __name__ == "__main__":
	main()


# GET

##################################################################################
#					 for each national team
##################################################################################
# +++ name
# +++ total_value
# +++ confederation
# +++ formation (most recent)
# +++ squad
# +++ substitutes

##################################################################################
# 					for each manager
##################################################################################
# 	+ 			id_team
#   +++   name 
# 	+   photo_manager
#   +++   date_of_birth
# 	+++   place_of_birth
#   +++   citizenship
#   + 			id_country_place_of_birth
#   +++   preferred_formation

##################################################################################
# 					for each player:
##################################################################################
#   +++   name
# 	+++   photo_player
#   +++   rating    (get the price/1,000,000)
#   +++   market_value
# 	+++   position
#							 	+   club_number
# 	+++   nat_team_number
# 	+++   date_of_birth
# 	+++   height
# 	+++   place_of_birth







#https://www.transfermarkt.us/bardsragujn-chumb/startseite/wettbewerb/ARM1

#https://www.espn.com/soccer/team/squad/_/id/450/league/UEFA.NATIONS

# get the squads of the national teams
# get the picture of each player (after clicking his name)


# squads for national teams
#	https://www.national-football-teams.com/national.html
#  	for each player, there is his club

# squads for clubs 
# 	https://www.national-football-teams.com/clubs.html
# 	for each player, there is his national team
#   some teams have empty squads
#   	the checkmark indicates that the player is a national player. Thus, when a checkmark is encountered,
# 		check the player against the database to see if the player is already in the database


# alternative for squads:
#		https://www.uefa.com/teamsandplayers/teams/club=50064/domestic/index.html

#plan

# since we want to get players for both clubs and national_teams, we 
#  must make sure we don't insert the same player twice (don't want 
#  duplicates)

# !!!
# write down what data we need to retrieve
# if needed, update the database, adding appropriate columns





# for fa cup, use the teams from this link:
# 	https://www.national-football-teams.com/leagues/59/2019_1/England.html