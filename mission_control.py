# MISSION CONTROL AI - Sistema de monitoramento espacial.
# Global Solution - Pensamento Computacional e Automação com Python.


# Identificação da missão e equipe.
nome_missao = "Missão TURBO"
nome_equipe = "Equipe NITRO"

# Matriz de dados da missão.
dados_missao = [
    [22, 95, 90, 98, 92],   # Ciclo 1 - Estável
    [25, 88, 85, 96, 88],   # Ciclo 2 - Leve queda
    [29, 72, 68, 93, 75],   # Ciclo 3 - Atenção em temperatura e bateria
    [34, 50, 45, 89, 60],   # Ciclo 4 - Crítico parcial
    [38, 32, 22, 79, 42],   # Ciclo 5 - Estado crítico
    [33, 58, 38, 84, 55]    # Ciclo 6 - Recuperação, ainda em atenção
]

# Lista de áreas monitoradas.
areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

# Limitando valores de cada parâmetro para classifica-los depois (normal ou atenção ou crítico).
limites = {
    "temperatura": {"normal_min": 18, "normal_max": 30, "atencao_max": 35},
    "comunicacao": {"normal_min": 60, "atencao_min": 30},
    "bateria": {"normal_min": 50, "atencao_min": 20},
    "oxigenio": {"normal_min": 90, "atencao_min": 80},
    "estabilidade": {"normal_min": 70, "atencao_min": 40}
}

# FUNÇÕES PARA ANÁLISE DE CADA PARÂMETRO.
# As funções classificarão o status (normal ou atenção ou crítico), farão as pontuações e mandar uma mensagem.

# TEMPERATURA:
def analisar_temperatura(valor):
    if valor < limites["temperatura"]["normal_min"] or (
            limites["temperatura"]["normal_max"] < valor <= limites["temperatura"]["atencao_max"]):
        return ("ATENÇÃO", 1, "Temperatura fora da faixa ideal")
    elif valor > limites["temperatura"]["atencao_max"]:
        return ("CRÍTICO", 2, "Risco de superaquecimento")
    else:
        return ("NORMAL", 0, "Temperatura estável")

# COMUNICAÇÃO:
def analisar_comunicacao(valor):
    if valor >= limites["comunicacao"]["normal_min"]:
        return ("NORMAL", 0, "Comunicação estável")
    elif valor >= limites["comunicacao"]["atencao_min"]:
        return ("ATENÇÃO", 1, "Comunicação instável")
    else:
        return ("CRÍTICO", 2, "Comunicação com base em nível crítico")

# BATERIA:
def analisar_bateria(valor):
    if valor >= limites["bateria"]["normal_min"]:
        return ("NORMAL", 0, "Energia estável")
    elif valor >= limites["bateria"]["atencao_min"]:
        return ("ATENÇÃO", 1, "Bateria abaixo do recomendado")
    else:
        return ("CRÍTICO", 2, "Bateria em nível crítico")

# OXIGÊNIO:
def analisar_oxigenio(valor):
    if valor >= limites["oxigenio"]["normal_min"]:
        return ("NORMAL", 0, "Oxigênio adequado")
    elif valor >= limites["oxigenio"]["atencao_min"]:
        return ("ATENÇÃO", 1, "Oxigênio abaixo do ideal")
    else:
        return ("CRÍTICO", 2, "Oxigênio em nível crítico")

# ESTABILIDADE:
def analisar_estabilidade(valor):
    if valor >= limites["estabilidade"]["normal_min"]:
        return ("NORMAL", 0, "Estabilidade operacional adequada")
    elif valor >= limites["estabilidade"]["atencao_min"]:
        return ("ATENÇÃO", 1, "Estabilidade operacional reduzida")
    else:
        return ("CRÍTICO", 2, "Estabilidade operacional crítica")


# Função para classificar o ciclo com base na pontuação.
def classificar_ciclo(pontuacao):
    if pontuacao <= 2:
        return "MISSÃO ESTÁVEL"
    elif pontuacao <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


# Função para gerar recomendação para status individuais.
def gerar_recomendacao_para_ciclo(status_por_area):
    """
    status_por_area: lista de tuplas (classificacao, pontos, mensagem) para cada área.
    Retorna uma string com recomendação adequada ao ciclo.
    """
    criticas = []
    atencao = []

    # CORREÇÃO: desempacotar os 3 valores
    for i, (classif, _, _) in enumerate(status_por_area):
        area = areas_monitoradas[i]
        if classif == "CRÍTICO":
            criticas.append(area)
        elif classif == "ATENÇÃO":
            atencao.append(area)

    if "Temperatura interna" in criticas:
        return "Verificar controle térmico da missão com urgência."
    if "Comunicação com a base" in criticas:
        return "Tentar restabelecer contato com a base imediatamente."
    if "Sistema de energia" in criticas:
        return "Ativar modo de economia de energia e verificar fontes."
    if "Suporte de oxigênio" in criticas:
        return "Adicionar protocolo de suporte à vida."
    if "Estabilidade operacional" in criticas:
        return "Reduzir operações não essenciais e estabilizar sistemas."

    if len(atencao) >= 3:
        return "Monitorar sistemas em atenção e preparar plano de contingência."
    elif len(atencao) > 0:
        return "Verificar sistemas em atenção e tomar medidas corretivas."
    else:
        return "Manter operação normal e continuar monitoramento."


# Função para analisar tendência da missão.
def analisar_tendencia(pontuacoes):
    """ Compara o primeiro com o último ciclo e retorna a tendência. """
    if len(pontuacoes) < 2:
        return "não é possível determinar (apenas um ciclo)."
    primeiro = pontuacoes[0]
    ultimo = pontuacoes[-1]
    if ultimo > primeiro:
        return "A missão apresentou tendência de piora."
    elif ultimo < primeiro:
        return "A missão apresentou tendência de  melhora."
    else:
        return "A missão permaneceu estável em relação ao início."


# Função para identificar a área mais afetada.
def indentificar_area_mais_afetada(pontuacao_acumulada_areas):
    """ pontuacao_acumulada_areas: Lista com soma de pontos para cada área.
    Retorna o nome da área com maior pontuacao. """

    max_pontos = max(pontuacao_acumulada_areas)
    indices_max = [i for i, p in enumerate(pontuacao_acumulada_areas) if p == max_pontos]
    # caso haja empate:
    return areas_monitoradas[indices_max[0]]


# Função para gerar o relatório final.
def gerar_relatorio_final(dados, pontuacoes_ciclos, status_por_ciclos, pontuacao_acumulada_areas, medias):

    print("\n" + "=" * 60)
    print("RELATÓRIO FINAL DA MISSÃO".center(60))
    print("=" * 60)
    print(f"Missão: {nome_missao}")
    print(f"Equipe: {nome_equipe}\n")

    print(f"Quantidade de ciclos analisados: {len(dados)}")
    print(f"Média de temperatura: {medias[0]:.2f} °C")
    print(f"Média de comunicação: {medias[1]:.2f}%")
    print(f"Média de bateria: {medias[2]:.2f}%")
    print(f"Média de oxigênio: {medias[3]:.2f}%")
    print(f"Média de estabilidade: {medias[4]:.2f}%\n")

    # Ciclo mais crítico.
    max_pont = max(pontuacoes_ciclos)
    idx_critico = pontuacoes_ciclos.index(max_pont) + 1
    print(f"Ciclo mais crítico: Ciclo {idx_critico}")
    print(f"Maior pontuação de risco: {max_pont}")

    risco_medio = sum(pontuacoes_ciclos) / len(pontuacoes_ciclos)
    print(f"Risco médio da missão: {risco_medio:.2f}")

    qtd_criticos = sum(1 for p in pontuacoes_ciclos if p >= 6)
    print(f"Quantidade de ciclos criticos: {qtd_criticos}\n")

    # Tendência.
    tendencia = analisar_tendencia(pontuacoes_ciclos)
    print(f"Tendencia da missão: {tendencia}\n")

    # Pontuação acumulada por área.
    print("Pontuação acumulada por área:")
    for i, area in enumerate(areas_monitoradas):
        print(f" {area}: {pontuacao_acumulada_areas[i]} pontos")

    area_afetada = indentificar_area_mais_afetada(pontuacao_acumulada_areas)
    print(f"\nÁrea mais afetada: {area_afetada}\n")

    # Classificação final na missão, baseada na média de pontos
    media_risco = sum(pontuacoes_ciclos) / len(pontuacoes_ciclos)
    classificacao_final = classificar_ciclo(media_risco)
    print(f"Classificação final da missão: {classificacao_final}\n")

    # Conclusão.
    print("Conclusão:")
    if classificacao_final == "MISSÃO ESTÁVEL":
        print("A Missão foi realizada dentro dos parâmetros seguros, continue o monitoramento.")
    elif classificacao_final == "MISSÃO EM ATENÇÃO":
        print("A Missão apresentou instabilidade relevante durante a operação, apesar da tentativa.")
        print("de recuperação, ainda existem sistemas em atenção. A equipe deve manter o plano")
        print("de contingência ativo.")
    else:
        print("A missão enfrentou falhas críticas. Protocolos de emergência devem ser executados")
        print("imediatamente e a missão deve ser reavaliada.")

    print("\n" + "=" * 60)


# Programa principal
def main():
    print("=" * 60)
    print("MISSION CONTROL AI".center(60))
    print("=" * 60)
    print(f"Missão: {nome_missao}")
    print(f"Equipe: {nome_equipe}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print("=" * 60)

    # Acumuladores
    pontuacoes_ciclos = []
    status_por_ciclo = []  # lista de listas com (classif, mensagem) por área
    pontuacao_acumulada_areas = [0, 0, 0, 0, 0]  # temperatura, comunic, bateria, oxig, estab

    # Para cálculo das médias
    soma = [0, 0, 0, 0, 0]  # temperatura, comunic, bateria, oxig, estab

    # Percorrer cada ciclo da matriz
    for idx, ciclo in enumerate(dados_missao, start=1):
        print(f"\nCICLO {idx}")
        print("-" * 40)

        # Extrair valores
        temp, comm, bat, oxi, est = ciclo

        # Acumular para médias
        soma[0] += temp
        soma[1] += comm
        soma[2] += bat
        soma[3] += oxi
        soma[4] += est

        # Analisar cada parâmetro
        resultado_temp = analisar_temperatura(temp)
        resultado_comm = analisar_comunicacao(comm)
        resultado_bat = analisar_bateria(bat)
        resultado_oxi = analisar_oxigenio(oxi)
        resultado_est = analisar_estabilidade(est)

        # Lista de status por área para este ciclo
        status_ciclo = [resultado_temp, resultado_comm, resultado_bat, resultado_oxi, resultado_est]
        status_por_ciclo.append(status_ciclo)

        # Exibir informações do ciclo
        print(f"Temperatura: {temp} °C | {resultado_temp[0]} | {resultado_temp[2]}")
        print(f"Comunicação: {comm}% | {resultado_comm[0]} | {resultado_comm[2]}")
        print(f"Bateria: {bat}% | {resultado_bat[0]} | {resultado_bat[2]}")
        print(f"Oxigênio: {oxi}% | {resultado_oxi[0]} | {resultado_oxi[2]}")
        print(f"Estabilidade: {est}% | {resultado_est[0]} | {resultado_est[2]}")

        # Calcular pontuação total do ciclo
        pontos_ciclo = (resultado_temp[1] + resultado_comm[1] + resultado_bat[1] +
                        resultado_oxi[1] + resultado_est[1])
        pontuacoes_ciclos.append(pontos_ciclo)

        # Acumular pontuação por área
        pontuacao_acumulada_areas[0] += resultado_temp[1]
        pontuacao_acumulada_areas[1] += resultado_comm[1]
        pontuacao_acumulada_areas[2] += resultado_bat[1]
        pontuacao_acumulada_areas[3] += resultado_oxi[1]
        pontuacao_acumulada_areas[4] += resultado_est[1]

        # Classificar o ciclo
        classificacao = classificar_ciclo(pontos_ciclo)
        print(f"\nPontuação de risco do ciclo: {pontos_ciclo}")
        print(f"Classificação do ciclo: {classificacao}")

        # Gerar recomendação específica
        recomendacao = gerar_recomendacao_para_ciclo(status_ciclo)
        print(f"Recomendação: {recomendacao}")

    # Calcular médias
    medias = [s / len(dados_missao) for s in soma]

    # Gerar relatório final
    gerar_relatorio_final(dados_missao, pontuacoes_ciclos, status_por_ciclo,
                          pontuacao_acumulada_areas, medias)


if __name__ == "__main__":
    main()