import game_display
import game_logic
obj=game_display.Game()

while(True):
	mainmenu_choice=obj.display_menu()
	while(True):
		game_display.clear()
		n=int(input("Enter Board Size\n"))
		obj2=game_display.Game(n)
		obj2.display_board()
		choice=obj.character_choice()
		ob=game_logic.Logic(n,choice)
		if mainmenu_choice==1:
			ob.single_player()
		elif mainmenu_choice==2:
			ob.double_player()
		else:
			print("Wrong Choice")
			continue
		break

	choice=obj.display_continue()
	if choice=='Y':
		continue
	else:
		print("Thanks for playing the game!")
		break





