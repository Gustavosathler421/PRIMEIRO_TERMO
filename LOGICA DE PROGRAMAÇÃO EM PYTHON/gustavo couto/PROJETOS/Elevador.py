# Sistema de Elevador de Prédio
# O prédio possui 10 andares, sendo o térreo o andar 0. O elevador pode se mover para cima ou para baixo, e tem a capacidade de transportar até 5 pessoas.
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa.
# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas (subindo, descendo, parando). O programa deve continuar rodando até que o usuário decida encerrar.
#O sistema deve impedir o movimento do elevador caso o número de pessoas inserido seja maior que 5. Uma mensagem de "Capacidade Máxima Excedida" deve ser exibida até que o número de passageiros seja ajustado.
#Adicionar um intervalo de tempo, um delay entre os andares e uma mensagem específica indicando "Abrindo Portas" e "Fechando Portas" em cada parada, para dar mais realismo à simulação.
import time
ANDAR_MINIMO = 0
ANDAR_MAXIMO = 10
CAPACIDADE_MAXIMA = 5

andar_atual = 0

print("=== SISTEMA DE ELEVADOR ===")

while True:

    print("\n--------------------------------")
    print(f"Andar atual: {andar_atual}")
    continuar = input("Deseja chamar o elevador? (s/n): ").lower()

    if continuar == "n":
        print("Encerrando sistema do elevador...")
        break
    while True:
        pessoas = int(input("Quantas pessoas entrarão no elevador?"))

        if pessoas > CAPACIDADE_MAXIMA:
            print("Capacidade Máxima Excedida!")
            print("O elevador suporta até 5 pessoas.")
        elif pessoas < 0:
            print("Erro: O número de pessoas não pode ser negativo.")
        else:
            break

    andar_chamada = int(input("Digite o andar onde o elevador foi chamado: "))
    andar_destino = int(input("Digite o andar de destino: "))
    if (
        andar_chamada < ANDAR_MINIMO or andar_chamada > ANDAR_MAXIMO or
        andar_destino < ANDAR_MINIMO or andar_destino > ANDAR_MAXIMO
    ):
        print("Andar inválido!")
        continue

    print("\nElevador indo até o andar solicitado...")

    while andar_atual != andar_chamada:

        if andar_atual < andar_chamada:
            andar_atual += 1
            print(f"Subindo... Andar {andar_atual}")
        else:
            andar_atual -= 1
            print(f"Descendo... Andar {andar_atual}")

        time.sleep(1)
    print("\nElevador parou.")
    print("Abrindo Portas...")
    time.sleep(1)

    print(f"{pessoas} pessoa(s) entraram no elevador.")

    print("Fechando Portas...")
    time.sleep(1)
    print("\nIndo para o andar de destino...")

    while andar_atual != andar_destino:

        if andar_atual < andar_destino:
            andar_atual += 1
            print(f"Subindo... Andar {andar_atual}")
        else:
            andar_atual -= 1
            print(f"Descendo... Andar {andar_atual}")
            time.sleep(1)
            print("\nElevador parou.")
            print("Abrindo Portas...")
            time.sleep(1)
            print(f"{pessoas} pessoa(s) saíram do elevador.")
            print("Fechando Portas...")
            time.sleep(1)
            print(f"Elevador disponível no andar {andar_atual}.")