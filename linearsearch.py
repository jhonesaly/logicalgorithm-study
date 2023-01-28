import os

list = [0, 20, 80, 30, 60, 50, 110, 100, 130, 170]

os.system('cls')
while exit != True:

    x = input('Digite "exit" para sair ou o número a ser buscado: ')

    if x.isnumeric():
        try:
            x = int(x)
        except:
            os.system('cls')
            print('digite um número inteiro')

    elif x == 'exit':
        os.system('cls')
        print('até a próxima!')
        exit = True
        break

    i = 0
    for num in list:
        
        if num == x:
            os.system('cls')
            print(f'o número faz parte da lista! Sua posição na memória é {i}')
            break            
    
        i += 1

    if i == len(list):
        os.system('cls')
        print('o número não faz parte da lista!')
        
        

