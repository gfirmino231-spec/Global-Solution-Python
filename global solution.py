# -----------------------------------------------------------
# Projeto: SkillBridge - FUTURE AT WORK
# Tema: Requalificação Inteligente para o Futuro do Trabalho
# Alunos:
# Gustavo Firmino – RM 566903
# Igor Marchiolli – RM 568330
# Lucas Nehrebecki – RM 568186
# -----------------------------------------------------------


# ---------------------- FUNÇÕES -----------------------------

def coletar_habilidades():
    habilidades = []
    removidas = []

    print("\nDigite suas habilidades (ex: programar, criatividade, saúde).")
    print("Digite 'remover' para retirar uma habilidade.")
    print("Digite 'sair' quando terminar.\n")

    while True:
        entrada = input("Habilidade: ").lower()

        if entrada == "sair":
            break

        elif entrada == "remover":
            if len(habilidades) == 0:
                print("Nenhuma habilidade para remover.\n")
                continue

            print("\nHabilidades atuais:")
            for i in range(len(habilidades)):
                print(f"{i} - {habilidades[i]}")

            try:
                indice = int(input("Digite o número da habilidade para remover: "))
                if 0 <= indice < len(habilidades):
                    removidas.append(habilidades.pop(indice))
                    print("Habilidade removida!\n")
                else:
                    print("Índice inválido. Tente novamente.\n")
            except ValueError:
                print("Entrada inválida. Digite um número.\n")

        else:
            habilidades.append(entrada)
            print("Habilidade adicionada!\n")

    return habilidades, removidas


def analisar_perfil(habilidades):
    # Palavras-chave separadas em listas simples
    trilha_ia = ["programar", "dados", "python", "tecnologia"]
    trilha_ciber = ["segurança", "rede", "investigar"]
    trilha_saude = ["saúde", "biologia", "cuidar"]
    trilha_criativa = ["arte", "criatividade", "design", "desenhar"]
    trilha_sust = ["natureza", "meio ambiente", "verde"]

    # Pontuações
    pontos_ia = 0
    pontos_ciber = 0
    pontos_saude = 0
    pontos_criativa = 0
    pontos_sust = 0

    # Verifica matches manualmente
    for h in habilidades:
        for p in trilha_ia:
            if p in h:
                pontos_ia += 1

        for p in trilha_ciber:
            if p in h:
                pontos_ciber += 1

        for p in trilha_saude:
            if p in h:
                pontos_saude += 1

        for p in trilha_criativa:
            if p in h:
                pontos_criativa += 1

        for p in trilha_sust:
            if p in h:
                pontos_sust += 1

    # Lista com os nomes das trilhas
    trilhas = ["Inteligência Artificial",
               "Cibersegurança",
               "Saúde Digital",
               "Economia Criativa",
               "Sustentabilidade"]

    # Lista com pontuações na mesma ordem
    pontuacoes = [pontos_ia, pontos_ciber, pontos_saude, pontos_criativa, pontos_sust]

    maior = 0
    for p in pontuacoes:
        if p > maior:
            maior = p

    if maior == 0:
        return ["Empreendedorismo e Aprendizado Contínuo"]

    recomendadas = []
    for i in range(len(pontuacoes)):
        if pontuacoes[i] == maior:
            recomendadas.append(trilhas[i])

    return recomendadas


def gerar_cursos(trilha):
    if trilha == "Inteligência Artificial":
        return ["Programação Básica", "Lógica", "Fundamentos de IA", "Dados"]
    elif trilha == "Cibersegurança":
        return ["Redes", "Criptografia", "Segurança Digital", "Análise de Ameaças"]
    elif trilha == "Saúde Digital":
        return ["Telemedicina", "Biossegurança", "IA na Saúde", "Cuidados Preventivos"]
    elif trilha == "Economia Criativa":
        return ["Design Digital", "Storytelling", "Edição de Imagem", "Criação de Conteúdo"]
    elif trilha == "Sustentabilidade":
        return ["Gestão Ambiental", "Tecnologias Verdes", "Inovações Sustentáveis", "Economia Circular"]
    else:
        return ["Produtividade", "Comunicação", "Organização", "Aprendizado Contínuo"]


def exibir_relatorio(habilidades, removidas, trilhas):
    print("\n========================================")
    print(" RELATÓRIO FINAL – SKILLBRIDGE")
    print("========================================")

    print("\n Habilidades informadas:")
    if len(habilidades) == 0:
        print(" - Nenhuma habilidade informada.")
    else:
        for h in habilidades:
            print(" -", h)

    if len(removidas) > 0:
        print("\n Habilidades removidas:")
        for r in removidas:
            print(" -", r)
    else:
        print("\n Habilidades removidas:")
        print(" - Nenhuma habilidade removida.")

    print("\n Trilhas recomendadas para seu futuro:")
    for t in trilhas:
        print(">>", t)
        cursos = gerar_cursos(t)
        print("    Cursos sugeridos:")
        for c in cursos:
            print("    -", c)

        print()

    print("💡 Continue se requalificando para garantir seu espaço no Futuro do Trabalho!\n")


# ---------------------- PROGRAMA PRINCIPAL -----------------------------

print("=== Bem-vindo ao SkillBridge – FUTURE AT WORK ===")
print("Descubra quais caminhos do futuro combinam com você!\n")

habilidades, removidas = coletar_habilidades()
trilhas_recomendadas = analisar_perfil(habilidades)
exibir_relatorio(habilidades, removidas, trilhas_recomendadas)
