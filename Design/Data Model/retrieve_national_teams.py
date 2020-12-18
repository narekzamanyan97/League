import requests
from bs4 import BeautifulSoup


urls = {
	'url_1': 'https://www.fifa.com/fifa-world-ranking/associations/#uefa',
	#https://www.fifa.com/fifa-world-ranking/associations/association/ARM/men/
	'suffix': '/men/',
	'url_1_1': 'https://www.fifa.com/fifa-world-ranking/associations/association/',
	'url_2': 'https://www.uefa.com/memberassociations/uefarankings/country/#/yr/2020',
	'url_3': 'https://en.wikipedia.org/wiki/2020\%E2\%80\%9321_UEFA_Nations_League',
	'url_4': 'https://en.wikipedia.org/wiki/List_of_national_stadiums',
}


	# id_ = ''
#	# name = ''
#	# confederation = ''

#	# flag_image_url = ''
#	# logo_image_url = ''

#	# fifa_ranking_points = ''
#	# country_coefficient = ''
	# nations_league_ranking = ''

	# name_stadium = ''
	# stadium_image_url = ''

def retrieve_national_teams_UEFA():
	confederation = 'UEFA'


	page = requests.get(urls['url_1'])
	#print(type(page))

	
	if page.status_code == requests.codes.ok:
		
		soup = BeautifulSoup(page.content, 'html.parser')
		
		uefa = soup.find("div", {"data-tab":"uefa"})

		uefa_national_teams = uefa.find_all('div', class_='fi-association-card col-xs-12 col-sm-4 col-md-3 col-lg-3 col-flex')


		for team in uefa_national_teams:

			team_name_elem = team.find('span', class_='fi-a__nText')
			team_code_elem = team.find('span', class_='fi-a__nTri')

			if None in (team_name_elem, team_code_elem):
				continue
			
			team_name = team_name_elem.text
			team_code = team_code_elem.text

			#get the flag_image_url
			img_class = "fi-" + str(team_code) + " fi-flag--4"
			team_flag_image_url_elem = team.find('img', class_=img_class)
			team_flag_image_url = team_flag_image_url_elem['src']


			

			#getting the fifa_ranking_points and logo_image_url
			url_team = urls['url_1_1'] + str(team_code) + urls['suffix']
			team_logo_image_url = retrieve_logo(url_team)
			team_fifa_ranking = retrieve_fifa_ranking(url_team)

			retrieve_country_coefficient(team_code)
			print(team_name)
			print(team_code)
			print(team_flag_image_url)
			print(team_logo_image_url)
			print(team_fifa_ranking)
			print()


	else: 
		print("Error: " + str(page.status_code))

def retrieve_logo(url_team):
	page = requests.get(url_team)

	if page.status_code == requests.codes.ok:
		#print(url_team)
		soup = BeautifulSoup(page.content, 'html.parser')
		#print(soup)

		#logo_div = soup.find('div', class_='fi-ah__l')
		logo_url_elem = soup.find('img', class_='fi-ah__lImage fi-flag--4')
		logo_url = logo_url_elem['src']
		#print(logo_url)

		return logo_url

def retrieve_fifa_ranking(url_team):
	page = requests.get(url_team)

	if page.status_code == requests.codes.ok:
		soup = BeautifulSoup(page.content, 'html.parser')

		fifa_ranking_points = soup.findAll('td', class_='fi-table__td fi-table__points')

		return fifa_ranking_points[2].text


	else:
		print("Error: " + str(page.status_code))



def retrieve_country_coefficient(team_code):
	page = requests.get(urls['url_2'])

	if page.status_code == requests.codes.ok:
		soup = BeautifulSoup(page.content, 'html.parser')

		country_coefficient = soup.find('div', class_='dataTables_scrollHead')
		
		#print(country_coefficient)



# get the uniform

def main():
	retrieve_national_teams_UEFA()
	#print(results)



# <div class="fi-association-card col-xs-12 col-sm-4 col-md-3 col-lg-3 col-flex">
# <a href="/fifa-world-ranking/associations/association/ARM/men/">
# <div class="fi-a fi-i--4" data-association-id="ARM">
# <div class="fi-a__i">
# <img alt="ARM" class="fi-ARM fi-flag--4" src="https://api.fifa.com/api/v1/picture/flags-sq-4/arm" title="ARM"/>
# </div>
# <div class="fi-a__n">
# <span class="fi-a__nText">Armenia</span>
# <span class="fi-a__nTri">ARM</span>
# </div>
# </div>


	#for logo
#	#7) fifa_ranking_points

#	#13) logo_image_url

	#'https://www.fifa.com/fifa-world-ranking/associations/association/ARM/men/'

	#GIVEN BY SQL
	#2) id_flag

	#3) id_logo


if __name__ == "__main__":
	main()



#*************************************************************************************
		#url_1:
		
			#name
			#confederation
				#UEFA
			#flag_image_url

		#url_1_1
			#logo
			#fifa ranking

#*************************************************************************************
	#url_2
		#6) country_coefficient

		#number of teams that qualify for UCL?
			#https://www.uefa.com/uefachampionsleague/accesslist/listofparticipants/


	#GIVEN BY SQL
		#id_team
		#id_stadium
		

	#id_league_qualifying_to
		# NL_2018
		# UEFA_EURO_2020_Q
		# NL_2020
		# FIFA_2022_Q_UEFA

	#status
		# QUALIFIED
		

	
#*************************************************************************************
	#url_3
	#8) nations_league_ranking

#*************************************************************************************
	#url_4

		#name_stadium
		
		#stadium_image_url
		


	






#############################################################################################
#############################################################################################
# fifa ranking: https://www.fifa.com/fifa-world-ranking/ranking-table/men/




#member associations: https://www.uefa.com/insideuefa/member-associations/




##################################################################################
								# the tables that are affected
##################################################################################

##################################################################################
								# national_teams

#1) id_stadium
	# set this value after adding the stadium into the table stadiums
	
#2) id_flag
	# set after setting flags

#3) id_logo
	
#4) name
		# https://www.fifa.com/fifa-world-ranking/associations/association/ENG/men/
#5) confederation
	# UEFA
#6) country_coefficient
	#https://www.uefa.com/memberassociations/uefarankings/country/#/yr/2020
#7) fifa_ranking_points
	#https://www.fifa.com/fifa-world-ranking/ranking-table/men/#UEFA
#8) nations_league_ranking
	#https://en.wikipedia.org/wiki/2020%E2%80%9321_UEFA_Nations_League	


##################################################################################
								# stadiums
#1) name
#2) id_country
#3) id_club 
	#https://www.fifa.com/fifa-world-ranking/associations/association/ENG/men/
#4) stadium name
#	https://en.wikipedia.org/wiki/List_of_national_stadiums
#	http://www.worldstadiums.com/
#	stadium_image_url
#		http://www.worldstadiums.com/
	
	#https://en.wikipedia.org/wiki/Estadio_Monumental_Antonio_Vespucio_Liberti


##################################################################################
								# flags
#1) image_url
	#https://www.fifa.com/fifa-world-ranking/associations/association/ENG/men/

##################################################################################
								# logos
#1) image_url
	#https://www.fifa.com/fifa-world-ranking/associations/association/ENG/men/

##################################################################################
								# team_league_qualification

#1) id_team
	# get this after inserting the team into the table national_teams
#2) id_league_qualifying_to
	# NL_2018
	# UEFA_EURO_2020_Q
	# NL_2020
	# FIFA_2022_Q_UEFA

#3) status
	# QUALIFIED

#############################################################################################
#############################################################################################
