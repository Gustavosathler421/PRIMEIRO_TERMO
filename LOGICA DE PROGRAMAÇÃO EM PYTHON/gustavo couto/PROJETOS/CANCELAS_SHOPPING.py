
# Passo 1:  
# Perguntar informações sobre o veiculo ou forma acesso
# Pressionar o botao para emitir ticket
# Verificar se possui TAG para acesso liberado 
# Se possuir erros informar ao usuario

# Passo 2:
# Verificar tempo de permanencia
# Valor a ser cobrado

# Passo 3:
# Saida como sera?
# Calcular tempo de permanencia
# Se for tag gerar na fatura da tag
# Pagar ticket
# Devolver ticket na saida

# Passo 4:
# Gerar relatorio de entradas e saidas
# Tratamento de Erros
# Revisão do código

import datetime

# Banco de dados simulado
veiculos_no_shopping = {} 
tag_db = ["ABC1234", "TAG4567"] 

def entrada_veiculo():
    print("--- MENU DE ENTRADA ---")
    try:
        placa = input("Digite a placa do veículo: ").upper()
        if placa in veiculos_no_shopping:
            print(f"Erro: Veículo {placa} já registrado no sistema.")
            return
        tem_tag = input("Possui TAG? (s/n): ").lower()
        if tem_tag == 's':
            if placa in tag_db:
                print(f"TAG Identificada! Acesso liberado, {placa}.")
                veiculos_no_shopping[placa] = datetime.datetime.now()
                return
            else:
                print("TAG não reconhecida. Procedendo como cliente comum.")

        input("Pressione Enter para emitir ticket...")
        hora_entrada = datetime.datetime.now()
        veiculos_no_shopping[placa] = hora_entrada
        print(f"Ticket emitido. Placa: {placa} | Hora: {hora_entrada.strftime('%H:%M:%S')}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        def calcular_valor():
            print("\n--- CÁLCULO DE SAÍDA ---")
    try:
        placa = input("Digite a placa do veículo para saída: ").upper()
        
        if placa not in veiculos_no_shopping:
            print("Erro: Veículo não encontrado no sistema.")
            return None
        valor_hora = float(input("Digite o valor por hora: R$ "))
        
        hora_entrada = veiculos_no_shopping[placa]
        hora_saida = datetime.datetime.now()
        duracao = hora_saida - hora_entrada
        duracao_em_horas = duracao.total_seconds() / 3600
        horas_cobradas = max(1, round(duracao_em_horas)) 
        valor_final = horas_cobradas * valor_hora
        
        print(f"Tempo permanência: {duracao_em_horas:.2f} horas")
        print(f"Total a pagar: R$ {valor_final:.2f}")
        
        return {"placa": placa, "valor": valor_final, "tempo": duracao_em_horas}

    except ValueError:
        print("Erro: Valor digitado inválido.")
        return None
    def saida_veiculo(dados_saida):
        if not dados_saida:
            return
    
    print("\n--- MENU DE SAÍDA ---")
    placa = dados_saida['placa']
    if placa in tag_db:
        print(f"Cobrança automática na fatura da TAG para {placa}.")
        print("Cancela liberada!")
    else:
        pago = input(f"Confirmar pagamento de R${dados_saida['valor']:.2f}? (s/n): ").lower()
        if pago == 's':
            print("Ticket pago. Devolvendo ticket...")
            print("Cancela liberada!")
        else:
            print("Pagamento pendente. Acesso bloqueado.")
            return
    del veiculos_no_shopping[placa]
    print(f"Veículo {placa} saiu.")
historico_registros = []
