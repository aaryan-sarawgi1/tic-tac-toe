import os
clear=lambda:os.system('cls')
class Game():
	def __init__(self,n=0):
		self.n=n
	def display_menu(self):
		clear()
		print("{:*^30}".format("MAIN MENU"))
		print("1.Single Player")
		print("2.Two Players")
		return int(input("Enter your choice\n"))
	def display_board(self):
		clear()
		print("{:^}\n".format("Welcome Player"))
		for i in range(self.n):
			print("   |"*(self.n-1))
	def display_cells(self,cells,turn):
		clear()
		print(f"{turn:^}'s Turn\n")
		for row in cells:
			for i,cell in enumerate(row):
				if i<self.n-1:
					print(cell+"|",end="")
				else:
					print(cell)
	def character_choice(self):
		while(True):
			choice=input("Enter your character choice(X/O)\n").upper()
			if choice=='X' or choice=='O':
				return choice
			else:
				print("Wrong Choice!Try again\n")
				continue 
	def cell_choice(self,cells):
		while(True):
			choice=int(input(f"Enter cell number you want to enter 1-{pow(self.n,2)}\n"))
			choice-=1
			i,j=divmod(choice,self.n)
			if choice>=pow(self.n,2) or choice<0 :
				print("Wrong Choice!Try again")
				continue
			elif cells[i][j]!="  ":
				print("Already Occupied!Try again")
				continue
			else:
				return i,j

	def display_continue(self):
		clear()
		return input("DO YOU WANT TO CONTINUE?(Y/N)\n").upper()


