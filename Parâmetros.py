from Rede_Artificial import Rede
from Matriz_Class import Matriz
import random



# ---------- Comentario Do Criador.


print(' '*14, 'Defina Os Parâmetros Da Rede'.upper())
print('-'*24, '@heyEvaldo', '-'*24)
print()
print()



""" Essa Rede Tem Como Funcao De Ativacao A Sigmoid. Dependendo De Quandas Matrizes De Dados Você For Precisar Para Treimar A Rede, Maior Sera A Quantidade Treinos. No Xor Problem A Quantidade De Treinos Que Eu Usei Pra Treinar A Rede Foi 900.000(novecentos mil), Metade Disso Ja Nao E O Suficiente Para Rede Aprender!! (Tenha Paciencia)
 Ja A Funcao De Ativacao Que Usei Foi A Sigmoid(Mesmo Sendo Limitada, Foi O Suficiente Para Resolver O Problema).  """




# [1] ------------- Definindo Os Parametros Da Rede.

geracao = int(input('Digite o número de Treinos: '))
entrada = int(input('Digite o número de neuronios de entrada: '))
oculta = int(input('Digite o número de neuronios ocultos: '))
saida = int(input('Digite o número de neuronios de saída: '))
print()
print()


# [2] ------------- Criando As Classes De Entradas/Saidas.

Entrada = Matriz(1, entrada)
Saida = Matriz(1, saida)



# [3] ------------- Criando/Inserindo Os Dados Nas Matrizes Que Treinará A Rede.

dados_entr1 = Entrada.Input()
print('Saida Experada; '.upper())
dados_sai1 = Saida.Input()
print()
print()

dados_entr2 = Entrada.Input()
print('Saida Experada; '.upper())
dados_sai2 = Saida.Input()
print()
print()

dados_entr3 = Entrada.Input()
print('Saida Experada; '.upper())
dados_sai3 = Saida.Input()
print()
print()

dados_entr4 = Entrada.Input()
print('Saida Experada; '.upper())
dados_sai4 = Saida.Input()
print()
print()



# [4] --------------- Chamando A Classe Que Cria E Treina A Rede E Inserindo As Matrizes De Dados Criadas No [3].

Rede = Rede(entrada, oculta, saida)



# 't'E O Conjunto De Entradas/Saidas Que Serao Treinadas Na Rede. Altere O 't' Conforme O Numeros De Dados(Entradas/Saida) Que Foram Criadas La No [3].


for c in range(0, geracao):
	t = random.randint(1, 4)
	if t == 1:
		rede = Rede.FeedFoward(dados_entr1, dados_sai1 )
	elif t == 2:
		rede = Rede.FeedFoward(dados_entr2, dados_sai2 )
	elif t == 3:
		rede = Rede.FeedFoward(dados_entr3, dados_sai3 )
	else:
		rede = Rede.FeedFoward(dados_entr4, dados_sai4 )



# [5] ------------------- Teste Da Rede Treinada.


# O Loop Comeca Com Respota Sim, Enquando A Resposta For Sim, Vc Podera Inserir Na Rede Ja Treinadas Pra Confirmar Se Ela Progrediu Ao Longo Do Treino.

c = 'S'

while not c == 'N':
	
	if c == 'S':
		print()
		rede = Rede.Predizer()
		print(rede)
		print()
		Rede.Media()
		c = str(input('Deseja Continuar [S/N]: ')).upper()
	
	else:
		print('Valor Invalido!! Tente Novamente.')
		c = str(input('Deseja Continuar [S/N]: ')).upper()




