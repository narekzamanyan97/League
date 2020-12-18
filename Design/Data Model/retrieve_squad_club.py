# IN PROGRESS

# import requests
# from bs4 import BeautifulSoup


from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time
import re



urls = {
	'url_1': 'https://www.transfermarkt.us/wettbewerbe/europa/wettbewerbe?plus=1', #for squads
}

def retrieve_squad_national_team(confederation):
	if confederation == 'UEFA':

		opts = Options()
		opts.set_headless = True
		driver = webdriver.Firefox(options=opts)
		driver.get(urls['url_1'])

		
		pager = driver.find_elements_by_xpath("//div[@class='responsive-table']/div[@id='yw1']/div[@class='pager']/ul[@id='yw2']/li")

		# for page in pager:
		# 	print("****" + str(page.get_attribute('innerHTML')))
		print("****" + str(pager[2].get_attribute('innerHTML')))
		

		#print(str(pager[0].get_attribute('innerHTML')))



		leagues_table = driver.find_elements_by_xpath("//div[@class='responsive-table']/div[@id='yw1']/table[@class='items']/tbody/tr")
		#print('*******' + str(leagues_table[0].get_attribute('innerHTML')))

		for k in range(2, 5):
			pager = driver.find_elements_by_xpath("//div[@class='responsive-table']/div[@id='yw1']/div[@class='pager']/ul[@id='yw2']/li")

			# click on page k
			driver.execute_script("arguments[0].click();", pager[k].find_elements_by_tag_name('a')[0])

			time.sleep(4)


			for i in range(1, 26):
				# click on the leagues on the page
				leagues_table = driver.find_elements_by_xpath("//div[@class='responsive-table']/div[@id='yw1']/table[@class='items']/tbody/tr")
				#print('*******' + str(leagues_table[0].get_attribute('innerHTML')))

				#league = leagues_table[i].find_elements_by_xpath("//a")
				#print("1****" + str(leagues_table[2].get_attribute('innerHTML')))
				
				#league = leagues_table[i].find_elements_by_xpath("//a")
				league = leagues_table[i].find_elements_by_tag_name('a')
				

				#print("2*****" + str(league[1].get_attribute('innerHTML')))

				league_name = league[1].get_attribute('innerHTML')					#

				number_of_teams = leagues_table[i].find_elements_by_tag_name('td')
				
				number_of_teams = number_of_teams[4].get_attribute('innerHTML')		#
				print("league_name = " + str(league_name))
				print("number of teams = " + str(number_of_teams))

				
				########################################################################
				# 							inside league
				########################################################################
				# click on the league
				driver.execute_script("arguments[0].click();", league[1])

				time.sleep(4)


				teams_table = driver.find_elements_by_xpath("//div[@class='responsive-table']/div[@id='yw1']/table[@class='items']/tbody/tr")

				#team = teams_table

				#squad_size
				for team_row in teams_table:
					#team_name = team.find_elements_by_tag_name("//td[@class='zentriert']")
					team_cols = team_row.find_elements_by_tag_name('td')
					team_cols_name = team_cols[1].find_elements_by_tag_name('a')
					team_cols_squad_size = team_cols[3].find_elements_by_tag_name('a')
					team_name = team_cols_name[0].get_attribute('innerHTML')				#
					team_squad_size = team_cols_squad_size[0].get_attribute('innerHTML')	#
					
					print('-------------------------Team Name: ' + str(team_name))
					print('-------------------------Squad Size: ' + str(team_squad_size))
					
					
					

					###########################################################################
					#							inside team
					###########################################################################
					for k in range(0, int(team_squad_size)):

						driver.execute_script("arguments[0].click();", team_cols_name[k])

						time.sleep(10)

						players_table = driver.find_elements_by_xpath("//div[@class='responsive-table']/div[@id='yw1']/table[@class='items']/tbody/tr")
						
						player_cols = players_table[k].find_elements_by_tag_name('td')
						player_button = player_cols[1].find_elements_by_tag_name('td')
						player_position = player_button[2].get_attribute('innerHTML')		#
						print('Position: ' + str(player_position))
						

						player_market_value = player_cols[8].text							#
						
						print('player market value: ' + str(player_market_value))

						button = player_button[1].find_elements_by_tag_name('a')
						#print('*******************' + str(player_button[1].get_attribute('innerHTML')))
						print('Player Name: ' + str(button[0].get_attribute('innerHTML')))
						
						#driver.execute_script("arguments[0].click();", button[0])
						#print('#####################################' + str(player_button[1].find_elements_by_tag_name('a')))
						
						#time.sleep(5)

						#try:
						# element = WebDriverWait(driver, 10).until(
						# 	EC.presence_of_element_located((By.ID, "myDynamicElement"))
						# )
						
						###########################################################################
						#						inside player
						###########################################################################
						# get the club number
						player_info = driver.find_elements_by_xpath("//div[@id='main']/div[@class='row']/div[@class='large-12 columns']/div[@class='dataHeader dataExtended']/div[@class='dataMain']/div[@class='dataTop']/div[@class='dataName']/span[@class='dataRN']")

						if len(player_info) != 0:
							player_number = player_info[0].get_attribute('innerHTML')
							print("player number: " + str(player_number))
						
						# back from the player
						driver.back()
						
						time.sleep(10)

						

						#except:
						#	driver.quit()
				# get the squad size
				#print('OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOout')

				# back from the league
	
				driver.back()

				time.sleep(4)
				########################################################################
				# 							outside league
				########################################################################
				print("********************************************************")
				print("********************************************************")
				print("********************************************************")
				print("********************************************************")











			

		


			#print(str(i) + ') ' + str(leagues_table[i].get_attribute('innerHTML')))



def main():
	retrieve_squad_national_team('UEFA')


if __name__ == "__main__":
	main()


##################################################################################
#					 for each league
##################################################################################
# 	+ name_league 		VARCHAR(80)	 not null,
# 	+ number_of_teams 	int,
# 	+ is_group_stage 	boolean,
# 	+ is_playoff 		boolean,
# 	+ number_of_stages 	int,
#  	+ is_qualification 	boolean,
# 	+ club_or_national_team 	boolean,
# 	+ status 			int,

##################################################################################
#					 for each club
##################################################################################
#	+ name
# 	+ id_stadium  				name_stadium
# 	+ id_logo  					url_logo
# 	+ id_country 				name_country		
# 	+ confederation 		
# 	+ club_coefficient
# 	+ date_founded 	
# 	+ squad_size		
#   + market value


##################################################################################
# 					for each manager
##################################################################################
# 	+ 			id_team
#   +   name 
# 	+   photo_manager
#   +   date_of_birth
# 	+   place_of_birth
#   +   citizenship
#   + 			id_country_place_of_birth
#   +   preferred_formation

##################################################################################
# 					for each player:
##################################################################################
#   +   name
# 	+   photo_player
#   +   rating    (get the price/1,000,000)
#   +++   market_value
# 	+++   position
#							 	+   club_number
# 	+   nat_team_number
# 	+   date_of_birth
# 	+   height
# 	+   place_of_birth


##################################################################################
#					 for each stadium
##################################################################################
# 	+ name
