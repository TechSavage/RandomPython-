import os
import pyfiglet

marshall = {'name': 'Marshall','points': 12, 'cash': 1000, 'health': 10, 'wit': 0, 'imagination': 0, 'trust': 3, 'respect': 6, 'intimidation': 0, 'description': 'Marshall -- A Hustler familiar with the city  \n\n              Health: 10 Cash: 1000\n              Stat Points:12 Trust:3 Respect:6'}
taylor = {'name': 'Taylor','points': 15, 'cash': 500, 'health': 10, 'wit': 0, 'imagination': 0, 'trust': 4, 'respect': 5, 'intimidation': 0, 'description': 'Taylor -- A Mechanic going through a rough time\n\n              Health: 10 Cash: 500\n              Stat Points:15 Trust:4 Respect:5'}
sullivan = {'name': 'Sullivan','points': 9, 'cash': 1500, 'health': 10, 'wit': 0, 'imagination': 0, 'trust': 6, 'respect': 3, 'intimidation': 0, 'description': 'Sullivan -- A White-collar with nothing to loose\n\n              Health: 10 Cash: 1500\n              Stat Points:9 Trust:6 Respect:3'}
playerList = [marshall,taylor,sullivan]

playerListName = [marshall['description'],taylor['description'],sullivan['description']]
playerMain = ''
days_remaining = 15

def story():
	title1 = pyfiglet.figlet_format("AMERICA!\nFUCK YEA!", font = "small")
	print("========================================")
	print(title1)
	print("========================================")
def intro():
	print(" =========_______________")
	print("/ PLAYERS \\--------------") 
	for n in playerListName:
		print("===============================================================")
		print("/// " + f"({playerListName.index(n) + 1})" +"  ---  " f"{n}")
		print("===============================================================")
	choice = input("\nPlease Choose Player by Number: ")

	if choice.isnumeric() == False:
		os.system('cls' if os.name == 'nt' else 'clear')
		print("----------------------------------------")		
		print("Not a valid choice! Must enter a number!")
		print("----------------------------------------\n")
		intro()
	elif int(choice) >= 1 and int(choice) <= len(playerListName):
		initializePlayer(choice)
	elif int(choice) > len(playerListName) or int(choice) < 1:
		os.system('cls' if os.name == 'nt' else 'clear')
		print("-----------------------------")		
		print("Not a valid character number!")
		print("-----------------------------\n")
		intro()
	else:
		os.system('cls' if os.name == 'nt' else 'clear')
		print("-----------------------------")
		print("Error. Try again")		
		print("-----------------------------\n")
		intro()

#def bs (wit,imagination):
#	if wit >  6:
#	if imagination > 6 :
#def events():
#def card_hustle():
#	title1 = pyfiglet.figlet_format("K", font = "cards")


def initializePlayer(player_choice):
	global playerMain
	playerMain = playerList[(int(player_choice)-1)]
	os.system('cls' if os.name == 'nt' else 'clear')
	print("\n\nYou have choosen: " f"{playerMain['name']}\n\n")
	update_stats()

def update_stats():
	global playerMain
	upgradeable_stats = ['wit', 'imagination','intimidation']
	for stats in upgradeable_stats:
		print("============================")
		print(f"{playerMain['name']}'s Upgradeable Stats:")
		print("============================")
		print(f"Wit: {playerMain['wit']}\nImagingation: {playerMain['imagination']}\nIntimidation: {playerMain['intimidation']}")
		print("============================\n\n")
		print(f"You have {playerMain['points']} points to spend on {playerMain['name']}'s stats\n") 	
		stat_in = input(f"How many points would you like to contribute to {playerMain['name']}'s {stats}: ")
		if stat_in.isnumeric() == False:
			os.system('cls' if os.name == 'nt' else 'clear')
			print("----------------------------------------")		
			print(f"Not a valid choice! Must enter a number from 0 to {playerMain['points']}!")
			print("----------------------------------------\n")
			update_stats()	
		elif int(stat_in) > playerMain['points'] and playerMain['points'] != 0:
			os.system('cls' if os.name == 'nt' else 'clear')
			print("----------------------------------------")		
			print(f"Not a valid choice! Must enter a number from 0 to {playerMain['points']}!")
			print("----------------------------------------\n")
			update_stats()
		elif int(stat_in) < 0:
			os.system('cls' if os.name == 'nt' else 'clear')
			print("----------------------------------------")		
			print(f"Not a valid choice! Must enter a number from 0 to {playerMain['points']}!")
			print("----------------------------------------\n")
			update_stats()
		elif int(stat_in) <= playerMain['points'] and playerMain['points'] != 0:
			os.system('cls' if os.name == 'nt' else 'clear')
			playerMain['points'] = playerMain['points'] - int(stat_in)
			playerMain[f'{stats}'] = playerMain[f'{stats}'] + int(stat_in)
			if playerMain['points'] == 0:
				print("Out of points")
				break
		elif playerMain['points'] == 0:
			os.system('cls' if os.name == 'nt' else 'clear')
			print("Out of points")
			#story()
			return
		else:
			os.system('cls' if os.name == 'nt' else 'clear')
			print("-----------------------------")
			print("Error. Try again")		
			print("-----------------------------\n")
			update_stats()
	if playerMain['points'] > 0:
		print("You have not used all of your points")
		print("Do you want to continue?")
		print("=============")
		print("| (1)  YES  |")
		print("| (2)  NO   |")
		print("=============\n")
		cont_1 = input("Answer: ")
		if cont_1.isnumeric() == False:
			os.system('cls' if os.name == 'nt' else 'clear')
			print("----------------------")		
			print("Not a valid selection!")
			print("----------------------\n")
			update_stats() 
		elif int(cont_1) == 1:
			os.system('cls' if os.name == 'nt' else 'clear')
			#story()
			return
		elif int(cont_1) == 2:
			os.system('cls' if os.name == 'nt' else 'clear')
			update_stats() 

		elif int(cont_1) > 2 or int(cont_1) < 1:
			os.system('cls' if os.name == 'nt' else 'clear')
			print("-----------------------")		
			print("Not a valid selection!")
			print("-----------------------\n")
			update_stats() 
		else:
			os.system('cls' if os.name == 'nt' else 'clear')
			print("-----------------------------")
			print("Error. Try again")		
			print("-----------------------------\n")
			update_stats() 


def main():
	story()

os.system('cls' if os.name == 'nt' else 'clear')
#main()
intro()
main()