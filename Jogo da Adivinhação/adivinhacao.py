def titulo(mensagem):
    print('--' * 50)
    print(f'{mensagem:^100}')
    print('--' * 50)


def escolhe_numero_secreto():
    from random import randint
    numero_secreto = randint(1, 10)
    return numero_secreto


def escolhe_chute():

    print('\nEscolha um número entre 1 e 10')

    while True:
        try:
            chute = int(input('Sua escolha: '))
            return chute

        except:
            print('\nOcorreu um erro com sua resposta. Tente novamente!!!')
            continue


def escolhe_nível():

    titulo('ESCOLHA UM NÍVEL DE JOGO')

    print('[1] - Facil  [2] - Médio  [3] - dificil\n')
    

    while True:
        try:
            nivel = int(input('Sua escolha: '))

            if nivel > 0 and nivel < 4:
                break
            else:
                print('\nDigite apenas os números 1, 2 ou 3!!!')
                continue
        except:
            print('\nDigite apenas os números 1, 2 ou 3!!!')

    return nivel


def iniciar():

    nivel = escolhe_nível()

    tentativas = 0

    cpu = escolhe_numero_secreto()


    if nivel == 1:
        tentativas = 10
    
    elif nivel == 2:
        tentativas = 5
    
    elif nivel == 3:
        tentativas = 3

    x = 1
    while x <= tentativas:
        print(f'\nTentativa {x} de {tentativas}.')

        jogador = escolhe_chute()
       
        if jogador == cpu:
            print('\nParabens, você acertou o número secréto.')
            break

        elif jogador > cpu:
            print(f'\nVocê errou. O número secreto é menor que {jogador}.')

        elif jogador < cpu:
            print(f'\nVocê errou. O número secreto é maior que {jogador}.')
        
        x += 1


titulo('Bem Vindo ao jogo da Adivinhação')

iniciar()