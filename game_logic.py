import game_display

class Logic():

	def __init__(self,n,playerchoice):
		self.n=n
		self.player1_choice=playerchoice
		self.cells=[["  "]*(n) for j in range(n)]
		self.player2_choice="XO".replace(playerchoice,"")
		

	def single_player(self):
		obj1=game_display.Game(self.n)
		choice=input("Do you want to play first?(y/n)").lower()
		while(True):
			if choice==y:
				i,j=obj1.cell_choice(self.cells)
				self.cells[i][j]=self.player1_choice+" "
				obj1.display_cells(self.cells,"Player")
				choice=n
			else:
				i,j=self.AI_choice()
				self.cells[i][j]=self.player2_choice+" "
				obj1.display_cells(self.cells,"AI")
				choice=y 			
			result=self.game_checker()
			if result==self.player1_choice:
				print("Congrats!You win\n")
			elif result==self.player2_choice:
				print("Oh my!AI wins\n")
			elif result=="TIE":
				prints("Its a TIE!")
			else:
				continue
			break

	def double_player(self):
		obj1=game_display.Game(self.n)
		while(True):
			i,j=obj1.cell_choice(self.cells)
			self.cells[i][j]=self.player1_choice+" "
			obj1.display_cells(self.cells,"Player 2")
			
			i,j=obj1.cell_choice(self.cells)
			self.cells[i][j]=self.player2_choice+" "
			obj1.display_cells(self.cells,"Player 1")
			
			result=self.game_checker()
			if result==self.player1_choice:
				print("Congrats!Player 1 wins\n")
			elif result==self.player2_choice:
				print("Congrats!Player 2 wins\n")
			elif result=="TIE":
				prints("Its a TIE!")
			else:
				continue
			break
	def game_checker(self):
		return 0
	def AI_choice(self):
		pass
			