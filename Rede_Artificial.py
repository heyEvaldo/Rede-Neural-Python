from Matriz_Class import Matriz
import numpy as np


class Rede:
	
	
	def __init__(self, neuronio_e, neuronio_o, neuronio_s):
		self.neuronio_e = neuronio_e
		self.neuronio_o = neuronio_o
		self.neuronio_s = neuronio_s
		
		
		#Pesos da entrada para oculta.
		peso_eo = Matriz(self.neuronio_e, self.neuronio_o)
		self.pesos_eo = peso_eo.Cria_Rd()
		
		#Pesos da oculta para entrada.
		peso_os = Matriz(self.neuronio_o, self.neuronio_s)
		self.pesos_os = peso_os.Cria_Rd()
		
		#Bias da entrada para oculta.
		bias_eo = Matriz(1, neuronio_o)
		self.bias_o = bias_eo.Cria_Rd()
		
		#Bias da oculta para saida.
		bias_os = Matriz(1, neuronio_s)
		self.bias_s = bias_os.Cria_Rd()
		
		
	
	
	def FeedFoward(self, Entradas = 0, Experadas = 0):
		self.Taxa = 0.1
		self.Experadas = Experadas
		self.Entradas = Entradas
		
		
		#FeedForward
		entrada = Matriz(1, self.neuronio_e)
		
		
		oculta = Matriz(1, self.neuronio_o)
		self.Ocultas = oculta.Cria_Rd()
		
		saida = Matriz(1, self.neuronio_s)
		self.Saidas = saida.Cria()
		
		self.Ocultas = oculta.Sigmoid(oculta.Soma(oculta.Mult(self.Entradas, self.pesos_eo), self.bias_o))
		
		self.Saidas = saida.Sigmoid(saida.Soma(saida.Mult(self.Ocultas, self.pesos_os), self.bias_s))
		
		
		#Backpropagation
		self.Erros_S = saida.Sub(self.Saidas, self.Experadas)
		
		self.Saidas_D = saida.DSigmoid(self.Saidas)
		
		self.Erros_O = entrada.Mult(self.Erros_S, self.pesos_os.T)
		
		self.D_Ocultas = oculta.DSigmoid(self.Ocultas)
		
		
		#Saida/Oculta
		self.Gradient_S = saida.Escalar(saida.Hadamart(self.Erros_S, self.Saidas_D), self.Taxa)
		
		self.D_pesos_os = oculta.Mult(self.Ocultas.T, self.Gradient_S)
		
		self.bias_s = saida.Sub(self.Gradient_S, self.bias_s)
		
		self.pesos_os = saida.Sub(self.pesos_os, self.D_pesos_os)
		
		
		#Oculta/Entrada
		self.Gradient_O = oculta.Escalar(oculta.Hadamart(self.Erros_O, self.D_Ocultas), self.Taxa)
		
		self.D_pesos_eo = entrada.Mult(self.Entradas.T, self.Gradient_O)
		
		self.bias_o= entrada.Sub(self.Gradient_O, self.bias_o)
		
		self.pesos_eo = entrada.Sub(self.pesos_eo, self.D_pesos_eo)
		
		self.ErrosMedia = saida.Media(self.Erros_S)
		

		
		return self.Saidas
	
	
	
	def Predizer(self, Dados = 0):
		self.Dados = Dados
		
		
		#FeedForward
		entrada = Matriz(1, self.neuronio_e)
		self.Entradas = entrada.Input()
		
		oculta = Matriz(1, self.neuronio_o)
		self.Ocultas = oculta.Cria_Rd()
		
		saida = Matriz(1, self.neuronio_s)
		self.Saidas = saida.Cria()
		
		self.Ocultas = oculta.Sigmoid(oculta.Soma(oculta.Mult(self.Entradas, self.pesos_eo), self.bias_o))
		
		self.Saidas = saida.Sigmoid(saida.Soma(saida.Mult(self.Ocultas, self.pesos_os), self.bias_s))
		
		
		#Salvando Dados (Tire Das Aspas Para Salvar Depois Do Treinamento E Mudei Os Nomes Pra Nao Sobrepor Os Dados Ja Treinados Da Pasta).
		
		'''np.save('Pesos_Entr', self.pesos_eo)
		
		np.save('Bias_Entr', self.bias_o)
		
		np.save('Pesos_Sai', self.pesos_os)
		
		np.save('Bias_Sai', self.bias_s)'''
		
		
		return self.Saidas
	
	
	
	#Print fos valores
	def Experada(self):
		return print(self.Experadas)
	
	def Entrada(self):
		return print(self.Entradas)
	
	def DPeso_E(self):
		return print(self.D_pesos_eo)
	
	def Peso_E(self):
		return print(self.pesos_eo)
	
	def Oculta(self):
		return print(self.Ocultas.T)
	
	def Gradient_O(self):
		return print(self.Gradient_O)
	
	def Peso_S(self):
		return print(self.pesos_os)
	
	def Media(self):
		return print(self.ErrosMedia)
	
	