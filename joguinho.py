# módulos
import random
# Variáveis
saldo = 0.0; valor = 0.0; nome = ''; idade = ''; numAleatorio = 0; VALORPERCA = 0.50; VALORGANHO = 2.0; numEscolhido = ''
# loops
loopCriarConta = loopNome = lacoIdade = loopDeposito = loopAposta = loopSacar = True
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
                print('Usuários menores de 18 anos não podem jogar ;)')
                loopCriarConta = False
                loopPrincipal = False
                lacoIdade = False
            elif idade >= 18:
                print('\nConta criada com sucesso!\n')
                break
        break
    # Funções
     
    def main():
        print('1 - Ver seu dados\n2 - Iniciar aposta\n3 - Depositar\n4 - Sacar\n5 - Loja (MANUTENÇÃO)\n6 - Inventário (MANUTENÇÃO)\nS / s - Sair\n')

    def mostrarDados():
        global mostrarNome,  mostrarIdade, mostrarSaldo
        mostrarNome = '\nSeu nome é {}'
        mostrarNome = mostrarNome.format(nome)
        print(mostrarNome)
        mostrarIdade = 'Sua idade é {}'
        mostrarIdade = mostrarIdade.format(idade)
        print(mostrarIdade)
        mostrarSaldo = 'Seu saldo é de R${}\n'
        mostrarSaldo = mostrarSaldo.format(saldo)
        print(mostrarSaldo)

    def aposta():
        global saldo, VALORGANHO, VALORPERCA, numAleatorio, numEscolhido, mensagemGanho, mensagemPerda, mostrarNumeroSorteado
        print('\n!!! Se você acertar o número aleatório, ganhará R$2.00 !!!\n!!! Se você não acertar o número aleatório, perderá R$0.50 !!!')
        while loopAposta:
            numAleatorio = random.randrange(0, 4)
            numAleatorio = str(numAleatorio)
            numEscolhido = input('\nDigite um número de 0 a 3: ')
            if numAleatorio == numEscolhido:
                saldo += VALORGANHO
                mostrarNumeroSorteado = '\nO número sorteado foi {}.'
                mostrarNumeroSorteado = mostrarNumeroSorteado.format(numAleatorio)
                print(mostrarNumeroSorteado)
                print('Você ganhou :)')
                mensagemGanho = 'Depositamos um valor de R${} na sua conta, seu saldo atual é de R${}\n'
                mensagemGanho = mensagemGanho.format(VALORGANHO, saldo)
                print(mensagemGanho)
                break
            elif numAleatorio != numEscolhido:
                saldo -= VALORPERCA
                mostrarNumeroSorteado = '\nO número sorteado foi {}.'
                mostrarNumeroSorteado = mostrarNumeroSorteado.format(numAleatorio)
                print(mostrarNumeroSorteado)
                print('Você perdeu :(')
                mensagemPerda = 'Retiramos R${} da sua conta, seu saldo atual é R${}\n'
                mensagemPerda = mensagemPerda.format(VALORPERCA, saldo)
                print(mensagemPerda)
                break
    def depositar():
        global valor, saldo, mostrarValorDepositado
        valor = float(input('\nDigite o valor que deseja depositar: R$'))
        saldo += valor
        mostrarValorDepositado = 'Valor de R${} depositado com sucesso!\nSeu saldo agora é de R${}\n'
        mostrarValorDepositado = mostrarValorDepositado.format(valor, saldo)
        print(mostrarValorDepositado)

    def sacar():
        global loopSacar, valor, saldo, mostrarSaldo, mostrarValorSacado
        while loopSacar:
            if saldo == 0.0:
                print('Você não tem dinheiro suficiente para sacar :(')
                mostrarSaldo = 'Seu saldo atual é de R${}'
                mostrarSaldo = mostrarSaldo.format(saldo)
                print(mostrarSaldo)
                break
            else:
                pass
            valor = float(input('Digite o valor que deseja sacar: R$'))
            if valor > saldo:
                print('Saldo insuficiente :(')
                mostrarSaldo = 'Seu saldo atual é {}'
                mostrarSaldo = mostrarSaldo.format(saldo)
                print(mostrarSaldo)
                break
            else:
                saldo -= valor
                mostrarValorSacado = 'Saque no valor de R${} realizado com sucesso :)'
                mostrarValorSacado = mostrarValorSacado.format(valor)
                print(mostrarValorSacado)
                mostrarSaldo = 'Seu saldo atual é {}'
                mostrarSaldo = mostrarSaldo.format(saldo)
                print(mostrarSaldo)
                break

    while loopPrincipal:
        main()
        opcaoMain = input('Digite uma opção: ')
        if opcaoMain == '1':
            mostrarDados()
        elif opcaoMain =='2':
            if saldo <= 0.0: # --> passou
                print('\nVocê não tem dinheiro suficiente para apostar, deposite uma quantia em R$.')
                mostrarSaldo = 'Seu saldo atual é de R${}\n'
                mostrarSaldo = mostrarSaldo.format(saldo)
                print(mostrarSaldo)
            else:
                aposta()
        elif opcaoMain == '3':
            depositar()
        elif opcaoMain == '4':
            sacar()
        elif opcaoMain == '5':
            print('Ainda estamos implementando este sistema, em breve estará disponível :)')
        elif opcaoMain == '6':
            print('Ainda estamos implementando este sistema, em breve estará disponível :)')
        elif opcaoMain == 'S' or opcaoMain == 's':
            print('Volte sempre :)\nSaindo...')
            loopPrincipal = False
        else:
            print('Digite um valor válido!')

except:
    print("Algo deu errado :(")