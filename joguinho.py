import random
# Variáveis
saldo = 0.0; valor = 0.0; nome = ''; idade = ''; numAleatorio = 0; VALORPERCA = 0.50; VALORGANHO = 2.0; numEscolhido = ''
# loops
loopCriarConta = loopNome = lacoIdade = loopDeposito = loopAposta = True
loopPrincipal = True
try:
    while loopCriarConta:
        while loopNome:
            primeiroNome = input('Digite seu primeiro nome: ')
            sobreNome = input('Digite o seu sobrenome: ')
            nome = '{}{}'
            nome = nome.format(primeiroNome, sobreNome)
            if nome.isalpha() == False:
                print('Seu nome tem que conter apenas letras!')
                continue
            else:
                nome = '{} {}'
                nome = nome.format(primeiroNome, sobreNome)
                break
        while lacoIdade:
            idade = input('Digite sua idade: ')
            if idade.isnumeric() == False:
                print('Sua idade não pode conter letras!')
                continue
            else:
                idade = int(idade)
                pass
            if idade < 18:
                print('Usuários menores de 18 anos não podem criar conta aqui!')
                loopCriarConta = False
                loopPrincipal = False
                lacoIdade = False
            elif idade >= 18:
                print('\nConta criada com sucesso!\n')
                break
        break
    # Funções
     
    def main():
        print('1 - Ver seu dados\n2 - Iniciar aposta\n3 - Depositar\n4 - Sacar\nS / s - Sair\n')

    def mostrarDados():
            mostrarNome = '\nSeu nome é {}'
            mostrarNome = mostrarNome.format(nome)
            print(mostrarNome)
            mostrarIdade = 'Sua idade é {}'
            mostrarIdade = mostrarIdade.format(idade)
            print(mostrarIdade)
            mostrarSaldo = 'Seu saldo é de R${}\n'
            mostrarSaldo = mostrarSaldo.format(saldo)
            print(mostrarSaldo)

#------------------------------------------------------
    def aposta():
        global saldo, VALORGANHO, VALORPERCA
        print('\n!!! Se você acertar o número aleatório, ganhará R$2.00 !!!\n!!! Se você não acertar o número aleatório, perderá R$0.50 !!!')
        while loopAposta:
            numAleatorio = random.randrange(0, 2)
            numAleatorio = str(numAleatorio)
            numEscolhido = input('\nDigite um número de 0 a 2: ')
            if numAleatorio == numEscolhido:
                saldo += VALORGANHO
                print('\nVocê ganhou :)')
                mensagemGanho = 'Depositamos um valor de R${} na sua conta, seu saldo atual é de R${}\n'
                mensagemGanho = mensagemGanho.format(VALORGANHO, saldo)
                print(mensagemGanho)
                break
            elif numAleatorio != numEscolhido:
                saldo -= VALORPERCA
                print('\nVocê perdeu :(')
                mensagemPerda = 'Retiramos R${} da sua conta, seu saldo atual é R${}\n'
                mensagemPerda = mensagemPerda.format(VALORPERCA, saldo)
                print(mensagemPerda)
                break
#-----------------------------------------------------------------
    def depositar():
        global valor, saldo
        valor = float(input('\nDigite o valor que deseja depositar: R$'))
        saldo += valor
        mostrarValorDepositado = 'Valor de R${} depositado com sucesso!\nSeu saldo agora é de R${}\n'
        mostrarValorDepositado = mostrarValorDepositado.format(valor, saldo)
        print(mostrarValorDepositado)

    while loopPrincipal:
        main()
        opcaoMain = input('Digite uma opção: ')
        if opcaoMain == '1':
            mostrarDados()
        #---------------------------
        elif opcaoMain =='2':
            if saldo <= 0: # --> passou
                print('\nVocê não tem dinheiro suficiente para apostar, deposite uma quantia em R$.')
                mostrarSaldo = 'Seu saldo atual é de R${}\n'
                mostrarSaldo = mostrarSaldo.format(saldo)
                print(mostrarSaldo)
            else:
                aposta()
        #--------------------------
        elif opcaoMain == '3':
            depositar()
        elif opcaoMain == 'S' or opcaoMain == 's':
            print('Volte sempre :)\nSaindo...')
            loopPrincipal = False

except:
    print('Algo deu errado :(')