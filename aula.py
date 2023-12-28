#loop
#De -> Para

#for numero in range(20):
#   print(numero)

#pode usar loop para mostrar cada item, mesmo sendo uma palavra    
#for letra in "Cauan":
#    print(letra)

# != diferente  == igual

# o f antes de um texto formata ele podendo colocar {} dentro de uma string é para usar uma variavel dentro de aspas duplas

#for numero in range(20):
#    if numero % 2 == 0:
#        print(f'O numero {numero} é par')
#    else:
#        print(f'O numero {numero} é ímpar')

#Transfroma o selecionado em comentário ctrl+kc ctrl+ku

# pagamentoConfirmado = False
# tentativas = 0

# print(f'Tentativa {tentativas} de 5')

# while not pagamentoConfirmado:
#     tentativas += 1
    
#     if tentativas >= 5:
#         break


#funcoes
#pascal case = sempre a primeira letra é maiuscula
#camel case = somente a segunda palavra é maiuscula 

# def minhaFuncao(nome, apelido):
#     print(f"Essa é a funcão do {nome} {apelido}")
    
# nome = input("Digite seu nome: ")
# apelido = input("Digite seu apelido: ")
    
# minhaFuncao(nome, apelido)


#xArgs = *args

# def listaDeCompras(*itens):
#     for item in itens:
#         print(item)
        
# listaDeCompras('banana', 'maça', 'uva')

# cidades = [
#     'São Paulo',
#     'Belo Horizonte',
#     'Salvador',
#     'Monte Belo']

# print(cidades[2])
# cidades.append('Santo André')
# cidades.insert(1, 'São Bernardo')

# usar .lower na funcão busca para ajustar a palavra escrita igual a minha lista, assim sempre vai achar o caracter igual

# frutas = ['banana', 'laranja', 'uva', 'maça']
# busca = input('Digite a fruta que deseja: ')

# if busca.lower() in frutas:
#     print('Sim, a fruta está na lista')


# #lista pode mudar, é mais pesada porque ela fica em aberto para poder ser alterada ou aumentada
# frutas = ['banana', 'laranja', 'uva', 'pera', 'melancia']

# #tuple é imutável e é mais rápida
# carros = {'Ford', 'Fiat', 'VW', 'Chevrolet'}