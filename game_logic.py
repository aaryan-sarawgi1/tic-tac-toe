import game_display
import time
class Logic():

	def __init__(self,n,playerchoice):
		self.n=n
		self.player1_choice=playerchoice
		self.cells=[["  "]*(n) for j in range(n)]
		self.player2_choice="XO".replace(playerchoice,"")
		self.obj1=game_display.Game(self.n)
		self.flag=True

	def single_player(self):
		
		
		choice=input("Do you want to play first?(y/n)").lower()
		while(True):
			if choice=='y':
				self.player_move(1,True)
				result=self.game_checker()
				if result!='0':#a tie or winning
					self.display_result(result)
					break
				choice='n'
			else:
				self.player_move(0)
				choice='y' 			
				result=self.game_checker()
				if result=='0':
					continue
				else:
					self.display_result(result)
					break

	def double_player(self):
		while(True):
			self.player_move(1,False)
			result=self.game_checker()
			if result!='0':#not a tie or winning
				self.display_result(result)
				break
			

			self.player_move(2)
			result=self.game_checker()
			if result=='0':
				continue
			else:
				self.display_result(result,True)
				break
	
	def player_move(self,num,check_single=True):
		evaltime=0
		if num==1:
			if not check_single:
				player_name="Player 2"
			else:
				player_name="AI"

			i,j=self.obj1.cell_choice(self.cells)
			choice=self.player1_choice+" "

		elif num==2:
			i,j=self.obj1.cell_choice(self.cells)
			choice=self.player2_choice+" "
			player_name="Player 1"
			
		else:
			choice=self.player2_choice+" "
			player_name="Player"
			i,j=self.isEmptyCorners(self.flag)
			if (i,j)==(-1,-1):
				start=time.time()
				garbage,i,j=self.AI_choice(True,0)
				end=time.time()
				evaltime=end-start
		self.cells[i][j]=choice
		self.obj1.display_cells(self.cells,player_name)
		if check_single==True and evaltime!=0:
			print("Evaluation time:{:6f} s".format(evaltime))
	
	def game_checker(self):
		for i in range(self.n):#check rows
			counter=0
			for j in range(self.n-1):
				if self.cells[i][j]!="  " and self.cells[i][j]==self.cells[i][j+1]:
					counter+=1
					character=self.cells[i][j].replace(" ","")
				else:
					break
			if counter==self.n-1:
				return character

		#returns whatever piece is winning

		for j in range(self.n):#check columns
			counter=0
			for i in range(self.n-1):
				if self.cells[i][j]!="  " and self.cells[i][j]==self.cells[i+1][j]:
					counter+=1
					character=self.cells[i][j].replace(" ","")
				else:
					break
			if counter==self.n-1:
				return character
		
		counter=0#check diagonal
		for j in range(self.n-1):#0,1
			if self.cells[j][j]!="  " and self.cells[j][j]==self.cells[j+1][j+1]:
				counter+=1
				character=self.cells[j][j].replace(" ","")
			else:
				break
		if counter==self.n-1:
			return character

		i,counter=0,0 #check other diagonal
		for j in range(self.n-1,0,-1):
			if self.cells[i][j]!="  " and self.cells[i][j]==self.cells[i+1][j-1]:
				counter+=1
				character=self.cells[i][j].replace(" ","")
				i+=1
			else:
				break
		if counter==self.n-1:
			return character
		
		if self.isFull(self.cells):
			return "TIE"

		return "0"
	
	def display_result(self,result,AI=False):
		if result==self.player1_choice:
			print("Congrats!Player 1 wins\n")
		elif result==self.player2_choice:
			if not AI:
				print("Congrats!Player 2 wins\n")
			else:
				print("Oh My!AI wins\n")
		elif result=="TIE":
			print("Its a TIE!")

	
	def isFull(self,cells):
		counter=0
		for row in cells:
			for cell in row:
				if cell!="  ":
					counter+=1
		if counter==pow(self.n,2):
			return True
		else:
			return False

	def isEmptyCorners(self,flag):
		if flag:
			mid=self.n//2
			if self.cells[mid][mid]=="  ":
				return (mid,mid)
			for i in [0,self.n-1]:
				for j in[0,self.n-1]:
					if self.cells[i][j]=="  ":
						self.flag=False
						return (i,j)
		return (-1,-1)
					
		

			
	def AI_choice(self,maximizing_player,depth,alpha=-9999,beta=9999):

		score=self.Evaluate(depth)
		if score!=-99999:
			return (score,0,0)
		

		best_i,best_j=-1,-1
        	

		if maximizing_player:#for AI
			best_value=-9999
			for i in range(self.n):
				for j in range(self.n):
					if self.cells[i][j]=="  ":
						#print("Max Position:",i,j)
						self.cells[i][j]=self.player2_choice+" "
						board_score,x,y=self.AI_choice(not maximizing_player,depth+1,alpha,beta)#forscorevalue
						alpha=max(alpha,board_score)
						#print(f"Alpha,beta,best_val,board_score={alpha,beta,best_value,board_score}")
						self.cells[i][j]="  "
						
						if board_score>best_value:
							best_i=i
							best_j=j
							best_value=board_score
							#print("the  max player position is",(best_i,best_j))
						if alpha>=beta:
							return(board_score,0,0)

						
	    	
	    				
		else:
			best_value=9999
			for i in range(self.n):
				for j in range(self.n):
					if self.cells[i][j]=="  ":
						#print("Min Position:",i,j)
						self.cells[i][j]=self.player1_choice+" "
						board_score,x,y=self.AI_choice(not maximizing_player,depth+1,alpha,beta)
						beta=min(beta,board_score)
						#print(f"Alpha,beta,best_val,board_score={alpha,beta,best_value,board_score}")
						self.cells[i][j]="  "
						
						if board_score<best_value:
								best_value=board_score
						if alpha>=beta:
							return(board_score,0,0)
		#print("final values are",best_i,best_j)				
		return (best_value,best_i,best_j)

		
	def Evaluate(self,depth):
		result=self.game_checker()
		if result==self.player2_choice:
			return 1000-depth
		if result==self.player1_choice:
			return -1000-depth
		if result=="TIE":
			return 0-depth
		return -99999



	
