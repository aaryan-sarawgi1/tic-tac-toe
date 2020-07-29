n=3
cells=[["  "]*(n) for j in range(n)]
print(cells)
while(True):
	choice=5
	choice-=1
	i,j=divmod(choice,n)
	if choice>=pow(n,2) or choice<0 :
		print("Wrong Choice!Try again")
		continue
	elif cells[i][j]!="  ":
		print("Already Occupied!Try again")
		continue
	else:
		cells[i][j]="X"
		print(cells)
		break