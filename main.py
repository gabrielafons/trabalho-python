  #Trabalho feito por: Igor de araujo borges  E Gabriel Afonso dos Santos

import random 
from datetime import datetime #tempo


dadostotais = {}#dicionario central, é aqui onde os dados do cliente são armazenados e daqui é mandado para o arquivo, ele é a base da nossa aplicação, os dados são digitados pelo usuario, e armazenados em um dicionario, e esse dicionario é lido por om laço for e copiado no Clientes.txt
dados = []#lista de apoio para o dicionario, essa lista é criada para armazenar os dados digitados pelo usuario, e posteriormente armazenados no dicionario, porem nesta não ha o cnpj, pois o cnpj é a chave do dicionario


dados1 = []
arquivo = open("Clientes.txt","r")
for linha in arquivo.readlines(): #laço for que vai ler cada linha do Clientes.txt por vez, armazenar o conteudo da linha em formato string na variavel "linha"
  
  linhaseparada = linha.strip().split(",") #a linha é separada em pedaços e armazenada em uma lista
  
  cnpj = linhaseparada[0] # define o item de indexador 0 como o cnpj
  dados1.append(linhaseparada[1].strip("'['")) #define o item de indexador 1 como o nome do cliente e retira o [ da lista
  dados1.append(float(linhaseparada[2]))#define o item de indexador 2 como o saldo e tranforma ele em float pois ele era uma string antes
  dados1.append(linhaseparada[3].strip(""))# define o item de indexador 3 como tipo de conta do cliente
  dados1.append(int(linhaseparada[4].strip("]"))) #define o item com indexador 4 comoa a senha, as antes disso ele retira o ] e tranforma em um numero inteiro
  dadostotais[cnpj] = dados1 #esta linha vai pegar o dicionario dadostotais, e vai criar uma chave com o conteudo da variavel cnpj, e como valor o conteudo da lista dados1.
  dados1=[]
arquivo.close()

#função que atualiza o arquivo Clientes com o conteudo do dicionario
def updatearquivo():
  arquivo = open("Clientes.txt","w")# o x armazena a chave e o y armazena o conteudo da chave
  for x, y in dadostotais.items():
    arquivo.write("%s,%s,%s,%s,%s\n" %(x,y[0],y[1],y[2],y[3])) # escreve cada variavel separadamente no arquivo assim não existe possibilidade de aparecer '' ou qualquer outro caractere indesejado
  arquivo.close()

#salva os dados em variaveis e manda para o dicionario
def op1():
  print("========= Cadastrar um usuario =========")
  print("")
  Razaosocial = input("Digite o nome da empresa: ")
  
  while True: #laço while que se repete eternamente enquanto o usuario não digitar um numero válido
   CNPJ = input("Digite o seu CNPJ:")
   if len(CNPJ) != 14:
     print("++++++ CNPJ precisa de 14 caracteres ++++++")
   elif CNPJ in dadostotais:
     print("++++++ CNPJ ja cadastrado ++++++")
   else:
    break
  
  v_inicial = float(input("Digite a quantia inicial em sua conta:"))
  while True: #laço while para o usuario digitar a opção correta, se não for COMUM ou PLUS desse jeito o codigo da erro
    conta_minuscula = input("Digite o seu tipo de conta (COMUM ou PLUS): ")
    Conta = conta_minuscula.upper()
    tipo= "COMUM"
    tipo2="PLUS"
    if (Conta != tipo) and (Conta != tipo2):
      print("++++++ Tipo de conta invalido ++++++")
    else:
      break
  Senha = int(input("Digite sua senha: "))
  Emprestimo = 0 
  #salva os dados em um dicionario
  dados = [Razaosocial,v_inicial,Conta,Senha]  # os dados digitatos são salvos em uma lista porque o valor de cada chave tem que ser uma lista de valores
  dadostotais[CNPJ] = dados
  
  print("")
  print("Razão Social: ", Razaosocial)
  print("CNPJ: ", CNPJ)
  print("Seu valor inicial:", v_inicial)
  print("Sua Conta: ", Conta)
  print("Sua senha:  ", Senha)
  print("")
  updatearquivo()

def op2():


  print("========= apagar os dados =========")
  print("")
  valida_cnpj = input("Digite o CNPJ cadastrado no sitema: ")# armazena o cnpj digitado em uma variavel
  if valida_cnpj in dadostotais: # verfica a existencia do cnpj digitado no dicionario
    del dadostotais[valida_cnpj] #deleta o cnpj digitado
    print("Seus dados foram apagados")
    updatearquivo() #chama a função updatearquivo para atualizar o arquivo

    #depois é preciso apagar os extratos da conta apagada, assim não tem problemas com os cnpjs futuros
    extrato = open("Extrato.txt", "r")
    linhas_mantidas = [] #lista onde as linhas serão armazenadas
    for linha in extrato.readlines(): #le o arquivo linha por linha
      lista = linha.split(",") #separa cada linha por , e manda para uma lista
      if lista[0] != valida_cnpj: #compara o idx 0 que é o cnpj com o digitado
        linhas_mantidas.append(linha) #se o cnpj digitado dor diferente ele vai ser preservado em uma lista
    extrato.close()
    extrato = open("Extrato.txt", "w")
    extrato.writelines(linhas_mantidas) #escreve somente as linhas que foram preservadas
    extrato.close()
    

  else:
    print("++++++ CNPJ invalido ++++++")
  



  #amarzena   os dados que forem digitados na op1 e mostra eles na op3
def op3():
  print("========= Lista dos clientes =========")
  print("")
  for cnpj, dados in dadostotais.items():
        # Exibindo CNPJ, Senha, Valor Inicial e Tipo de Conta
    print("CNPJ:", cnpj)
    print("Razão Social:", dados[0])
    print("Senha:", dados[3])
    print("Saldo:", dados[1])
    print("Conta:", dados[2])
    print("")

def op4():
  print("========= Saque =========")
    #Pega o cnpj e senha e verifica se e o usuario certo 
  valida_cnpj = input("Digite seu CNPJ: ")
  if valida_cnpj in dadostotais:
    x = dadostotais.get(valida_cnpj) #armazen na variavel x uma copia da lista de valores do cnpj digitado
    saldo = x[1] 
    senha = int(x[3])
    
    valida_senha = int(input("Digite sua senha: "))
    if valida_senha == senha: 
#Debita da conta o valor e verifica se e comum ou plus a conta
      v = float(input("Digite o valor que deverá ser debitado de sua conta: "))
      if (x[1] >= -1000 and x[2] == "COMUM") or (x[1] >= -5000 and x[2] == "PLUS"):
        
        x[1] -= v
        if x[2] == "COMUM":
          taxa = v * 0.05
          x[1] -= taxa
          data = datetime.now().strftime("%d,%m,%Y")
          tempo = datetime.now().strftime("%H:%M:%S")
         
          updatearquivo() #chama a função de update do arquivo
          print("R$", v, "foram debitados de sua conta.")
          #abre o arquivo Extrato.txt e escreve o cnpj, data, quantia, taxa e o saldo na hora da transação
          extrato = open("Extrato.txt","a")
          extrato.write("{0}, - {1},{2},{3},{4},{5}\n".format(valida_cnpj,v,data,tempo,taxa,saldo))
          extrato.close()         
        
        elif x[2] == "PLUS":
          taxa = v * 0.03
          x[1] -= taxa
          data = datetime.now().strftime("%d,%m,%Y")
          tempo = datetime.now().strftime("%H:%M:%S")
          #abre o arquivo Extrato.txt e escreve o cnpj, data, quantia, taxa e o saldo na hora da transação
          extrato = open("Extrato.txt","a")
          extrato.write("{0}, - {1},{2},{3},{4},{5}\n".format(valida_cnpj,v,data,tempo,taxa,saldo))
          extrato.close()
          
          print("R$", v, "foram debitados de sua conta.")
          updatearquivo()
        
      else:
        print("+++++++ Saldo limite alcançado +++++++")
    else:
        print("+++++++ Senha inválida +++++++")
  else:
        print("+++++++ CNPJ inválido +++++++")




def op5():
  print("========= Deposito =========")
  #Pega o cnpj e senha e verifica se e o usuario certo 
  valida_cnpj = input("Digite seu CNPJ: ")
  if valida_cnpj in dadostotais:
    x = dadostotais.get(valida_cnpj)
    senha = int(x[3])
    valida_senha = int(input("Digite sua senha: "))
    if valida_senha == senha:
     #adiciona o valor exigido na conta 
      v = float(input("Digite o valor que deverá ser depositado em sua conta: "))
      y = dadostotais.get(valida_cnpj)
      
      saldo = y[1]
      y[1] += v
       
      taxa = 0
      #coloca o tempo e hora
      data = datetime.now().strftime("%d,%m,%Y")
      tempo = datetime.now().strftime("%H:%M:%S")
        
          
      print("R$", v, "foram depositados em sua conta.")
      updatearquivo()
      #abre o arquivo Extrato.txt e escreve o cnpj, data, quantia, taxa e o saldo na hora da transação
      extrato = open("Extrato.txt","a")
      extrato.write("{0}, + {1},{2},{3},{4},{5}\n".format(valida_cnpj,v,data,tempo,taxa,saldo))
      extrato.close()
    
    else:
      print("+++++++Senha inválida+++++++")
  else:
    print("+++++++CNPJ inválido+++++++")

#/////////////////////////////////////////////////////////////////////





def op6():
  print("========= Extrato =========")
#Pega o cnpj e senha e verifica se e o usuario certo
  valida_cnpj = input("Digite seu CNPJ: ")
  if valida_cnpj in dadostotais:
    x = dadostotais.get(valida_cnpj)
    senha = int(x[3])
    valida_senha = int(input("Digite sua senha: "))
    if valida_senha == senha:
      #mostra tudo que foi armazenado na 4,5,7 e 8
      extrato = open("Extrato.txt","r")
      print("========= Seu Extrato =========")
      print("")
      print("Razão Social:", dadostotais[valida_cnpj][0])
      print("CNPJ:", valida_cnpj)
      print("Conta:", dadostotais[valida_cnpj][2])
      print("")
      for linha in extrato.readlines():
       lista_extrato = []
       lista_extrato = linha.strip("\n").split(",")
       data = lista_extrato[2:6]
       if lista_extrato[0] == valida_cnpj:
         
         print("Data:{0}     {1}   Tarifa: {2}   Saldo:{3}".format(data,lista_extrato[1],lista_extrato[6],lista_extrato[7]))
      extrato.close()
    else:
      print("Senha inválida")
  else:
    print("CNPJ inválido")



def op7():
  print("========= Transferência entre Contas =========")
  valida_cnpj = input("Digite seu CNPJ: ") #variavel de validacao, o valor dela sera procurada no dicionario
  if valida_cnpj in dadostotais: #procura da vriavel no dicionario
    x = dadostotais.get(valida_cnpj) #registra em uma variavel uma lista do cnpj indicado
    senha = x[3] #registro uma variavel como o indexador 3 (senha), da lista do codigo de cima
    valida_senha = int(input("Digite sua senha: "))
    if valida_senha == senha:
      cnpj_2 = input("digite o CNPJ destino: ")
      if cnpj_2 in dadostotais:
        
        v =float(input("digite o valor que deverá ser transferido: "))
              #tirar o dinheiro da conta 

        y1 = dadostotais.get(valida_cnpj)
        saldo_1 =y1[1]
        y1[1] -= v
        # lista1 =  dadostotais.get(valida_cnpj)
        # lista1[1]=x1
        

              #colocar na outra contra
        y = dadostotais.get(cnpj_2)
        saldo = y[1]
        y[1] += v
        
        print("R$",v," foram debitados de sua conta e foram depositados na conta de",cnpj_2)
        data = datetime.now().strftime("%d,%m,%Y")
        tempo = datetime.now().strftime("%H:%M:%S")
        taxa=0 #na operações onde não há taxa, o valor da taxa é 0
        #abre o arquivo Extrato.txt e escreve o cnpj, data, quantia, taxa e o saldo na hora da transação
        extrato = open("Extrato.txt","a")
        extrato.write("{0}, - {1},{2},{3},{4},{5}\n".format(valida_cnpj,v,data,tempo,taxa,saldo_1))
        extrato.write("{0}, + {1},{2},{3},{4},{5}\n".format(cnpj_2,v,data,tempo,taxa,saldo))
        extrato.close()
        updatearquivo()
      else:
        print("++++++ cnpj destino não encontrado ++++++")

    else:
      print("++++++ senha invalida ++++++")


  else:
    print("++++++ CNPJ invalido ++++++")



def op8():
  #operação livre consiste em uma aposta com o banco , em que se tira dinheiro de uma conta para apostar, a aposta é cara e coroa
  print("========= Teste sua Sorte =========")
  print("")
  print("O banco não se responsabiliza por eventuais perdas monetarias")
  print("")
  valida_cnpj = input("Digite seu CNPJ: ")
  if valida_cnpj in dadostotais:
    x = dadostotais.get(valida_cnpj)
    senha = int(x[3])
    valida_senha = int(input("Digite sua senha: "))
    if valida_senha == senha:
      #valor da aposta escolhido 
      valor_aposta = float(input("Digite o valor que deseja apostar: "))
        #ve se ele possui dinheiro na conta para jogar 
      if valor_aposta <= x[1]:
        print("1. Cara")
        print("2. Coroa")
        escolha = int(input("Escolha 1 para Cara ou 2 para Coroa: "))
        resultado = random.randint(1, 2)  # Escolhe um numero aleatorio entre 1 e 2 
        #Tem a chance de dobrar o valor
        if escolha == resultado:
          x[1] += valor_aposta 
          print("Parabéns! Você acertou! Seu saldo foi dobrado.")
          data = datetime.now().strftime("%d,%m,%Y")
          tempo = datetime.now().strftime("%H:%M:%S")
          taxa = 0
          y1 = dadostotais.get(valida_cnpj)
          saldo_1 =y1[1]
          y[1] += escolha
          
          extrato = open("Extrato.txt","a")
          extrato.write("{0}, + {1},{2},{3},{4},{5}\n".format(valida_cnpj,valor_aposta,data,tempo,taxa,saldo))
          extrato.close()
          updatearquivo()
          # JA ERA SUA GRANA (perde a grana)
        else:
          x[1] -= valor_aposta  
          print("Você perdeu! Sua grana.")
          data = datetime.now().strftime("%d,%m,%Y")
          tempo = datetime.now().strftime("%H:%M:%S")
          taxa=0
          y1 = dadostotais.get(valida_cnpj)
          saldo =y1[1]
          y[1] -= escolha
          extrato = open("Extrato.txt","a")
          extrato.write("{0}, - {1},{2},{3},{4},{5}\n".format(valida_cnpj,valor_aposta,data,tempo,taxa,saldo))
          extrato.close()
          updatearquivo()
      else:
        print("++++++ Saldo insuficiente para realizar a aposta ++++++")
    else:
      print("++++++ senha invalida ++++++")
  else:
    print("++++++ CNPJ invalido ++++++")
 
#tela inicial para ver qual opcao sera escolhida
while True:
  print("========= Bem Vindo! =========")
  print("")
  print("1. Novo cliente")
  print("2. Apaga cliente")
  print("3. Listar clientes")
  print("4. Débito")
  print("5. Depósito")
  print("6. Extrato")
  print("7. Transferência entre contas ")
  print("8. Tente a sorte")
  print("9. Sair")
  print("")
  N = int((input("========= escolha uma opção =========\n"))) 
#recebe o numero da opção

    #escolha das opc
  if N==1:
    op1()
  elif N==2:
    op2()
  elif N==3:
    op3()
  elif N==4:
    op4()
  elif N==5:
    op5()
  elif N==6:
    op6()
  elif N==7:
    op7()
  elif N==8:
    op8()
  elif N == 9:
    break
  else:
    print("")
    print("++++++ digite uma opção valida ++++++")
    print("")

arquivo.close()

