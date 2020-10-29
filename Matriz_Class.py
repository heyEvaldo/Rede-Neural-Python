import random 
import numpy as np
import math


class Matriz:
	__matriz_A = 0
	
	
	def __init__(self, linhas = 0, colunas = 0 ):
		self.linhas = linhas
		self.colunas = colunas
	
	
	
	def Cria_Rd(self):
		__matriz = np.zeros((self.linhas, self.colunas))
		
		
		for i in range(0, self.linhas):
			for j in range(0, self.colunas):
				__matriz[i][j] = random.random()
		
		return __matriz
	
	
	
	def Cria(self):
		__matriz = np.zeros((self.linhas, self.colunas))
		
		return __matriz
	
	
	def Sub(self, matr_A, matr_B):
		self.matr_A = matr_A
		self.matr_B = matr_B
		
		return np.subtract(matr_A, matr_B)
	
	
	
	def Escalar(self, matr_A, escalar):
		self.matr_A = matr_A
		self.escalar = escalar
		
		return np.multiply(matr_A, escalar)
		
	
	
	def Hadamart(self, matr_A, matr_B):
		self.matr_A = matr_A
		self.matr_B = matr_B
		
		return np.multiply(matr_A, matr_B)
	
	
	
	def Mult(self, matr_A, matr_B):
		self.matr_A = matr_A
		self.matr_B = matr_B
		
		
		__matriz = np.dot(matr_A, matr_B)
		
		return __matriz
	
	
	def Soma(self, matr_A, matr_B):
		self.matr_A = matr_A
		self.matr_B = matr_B
		
		
		__matriz = np.add(matr_A, matr_B)
		
		return __matriz
		
		
	
	def Input(self):
		matr_A = np.empty((self.linhas, self.colunas))
		
		
		for i in range(0, self.linhas):
			for j in range(0, self.colunas):
				
				matr_A[i][j] = float (input('Entrada: '))
		
		
		return matr_A
	
	
	
	def Media(self, matr_A):
		self.matr_A = matr_A
		matr_B = np.zeros((self.linhas, self.colunas))
		
		matr_B = matr_A.mean()
		
		return matr_B
	
	
	def Sigmoid(self, matr_A, matr_B = 0):
		self.matr_A = matr_A
		matr_B = np.zeros((self.linhas, self.colunas))
		
		
		def sigmoid(x):
			return 1 / ( 1 + math.exp(-x))
		
		for i in range(0, self.linhas):
			for j in range(0, self.colunas):
				matr_B[i][j] = sigmoid(matr_A[i][j])
		
		return matr_B
		


	def DSigmoid(self, matr_A, matr_B = 0):
		self.matr_A = matr_A
		matr_B = np.zeros((self.linhas, self.colunas))
		
		
		def dsigmoid(x):
			return x * ( 1 - x )
		
		for i in range(0, self.linhas):
			for j in range(0, self.colunas):
				matr_B[i][j] = dsigmoid(matr_A[i][j])
		
		return matr_B
	
	
	
	def Tanh(self, matr_A, matr_B = 0):
		self.matr_A = matr_A
		matr_B = np.zeros((self.linhas, self.colunas))
		
		
		def tanh(x):
			return math.tanh(x)
		
		for i in range(0, self.linhas):
			for j in range(0, self.colunas):
				matr_B[i][j] = tanh(matr_A[i][j])
		
		return matr_B
		


	def DTanh(self, matr_A, matr_B = 0):
		self.matr_A = matr_A
		matr_B = np.zeros((self.linhas, self.colunas))
		
		
		def dtanh(x):
			return 1 - x**2
		
		for i in range(0, self.linhas):
			for j in range(0, self.colunas):
				matr_B[i][j] = dtanh(matr_A[i][j])
		
		return matr_B
	
	
	
	def ReLu(self, matr_A, matr_B = 0):
		self.matr_A = matr_A
		matr_B = np.zeros((self.linhas, self.colunas))
		
		
			
		for i in range(0, self.linhas):
			for j in range(0, self.colunas):
				
				if self.matr_A[i][j] >= 1:
					matr_B[i][j] = self.matr_A[i][j]
				
				else:
					pass
		
		return matr_B
	
	
	def DReLu(self, matr_A, matr_B = 0):
		
		self.matr_A = matr_A
		matr_B = np.zeros((self.linhas, self.colunas))
		
		
		
		for i in range(0, self.linhas):
			for j in range(0, self.colunas):
				
				if self.matr_A > 0:
					matr_B[i][j] = 1
				
				elif self.matr_A[i][j] < 0:
					matr_B[i][j] = -1
					
				else:
					pass
		
		return matr_B
	
	
	
	def Borda(self, matr_A, borda_A):
		
		linhas_2 = self.linhas + borda_A * 2
		colunas_2 = self.colunas + borda_A * 2
		
		self.matr_B = np.zeros((linhas_2, colunas_2))
		
		lin = self.linhas + borda_A
		col = self.colunas + borda_A
		
		self.matr_B[borda_A : lin , borda_A: col ] = matr_A
		
		return self.matr_B
	
	
	
	
	
	
	
	