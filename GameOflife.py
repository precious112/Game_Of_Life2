import random
class board:
	def __init__(self,x):
		self.L1=[x,x,x,x,x,x,x,x,x,x]
		self.L2=[x,x,x,x,x,x,x,x,x,x]
		self.L3=[x,x,x,x,x,x,x,x,x,x]
		self.L4=[x,x,x,x,x,x,x,x,x,x]
		self.L5=[x,x,x,x,x,x,x,x,x,x]
		self.L6=[x,x,x,x,x,x,x,x,x,x]
		self.L7=[x,x,x,x,x,x,x,x,x,x]
		self.L8=[x,x,x,x,x,x,x,x,x,x]
		self.L9=[x,x,x,x,x,x,x,x,x,x]
		self.L10=[x,x,x,x,x,x,x,x,x,x]
		self.theRows=[self.L1,self.L2,self.L3,self.L4,self.L5,self.L6,self.L7,self.L8,self.L9,self.L10]
		self.BoundaryList=[self.L1,self.L10,self.L2[0],self.L3[0],self.L4[0],self.L5[0],self.L6[0],self.L7[0],self.L8[0],self.L9[0],self.L2[9],self.L3[9],self.L4[9],self.L5[9],self.L6[9],self.L7[9],self.L8[9],self.L9[9]]
		for i in self.theRows:
			print(*i)
	def setLiveCells(self):
		for i in range(3):
			for j in range(3):
				i = random.randint(4,6)
				j= random.randint(3,5)
				self.theRows[i][j]=1
		for i in self.theRows:
			print(*i)
	def playGame(self):
		
		
		
		
		
		for i in range(9):
			for j in range(9):
				k= self.theRows[i][j]
				self.Neighbor1=self.theRows[i-1][j-1]
				self.Neighbor2=self.theRows[i-1][j]
				self.Neighbor3=self.theRows[i-1][j+1]
				self.Neighbor4=self.theRows[i+1][j-1]
				self.Neighbor5=self.theRows[i+1][j+1]
				self.Neighbor6=self.theRows[i+1][j]
				self.Neighbor7=self.theRows[i][j-1]
				self.Neighbor8=self.theRows[i][j+1]
				if self.Neighbor1+self.Neighbor2+self.Neighbor3+self.Neighbor4+self.Neighbor5+self.Neighbor6+self.Neighbor7+self.Neighbor8==2:
					self.theRows[i][j]=1
				elif self.Neighbor1+self.Neighbor2+self.Neighbor3+self.Neighbor4+self.Neighbor5+self.Neighbor6+self.Neighbor7+self.Neighbor8==3:
					self.theRows[i][j]=1
				else:
					self.theRows[i][j]=0
				
				for n in self.theRows:
					print(*n)
				print("--------------------")	
					
							
						
					
				
		
			
		
def main():
		y=board(0)
		print("---------------------")
		y.setLiveCells()
		print("---------------------")
		y.playGame()
		print("---------------------")
if __name__=="__main__":
	main()	