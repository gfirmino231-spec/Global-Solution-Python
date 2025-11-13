# -----------------------------------------------------------
# Projeto: SkillBridge - FUTURE AT WORK
# Tema: Requalificação Inteligente para o Futuro do Trabalho
# Alunos:
# - Gustavo Firmino Barbosa – RM 566903
# - Igor Marchiolli – RM XXXXXXX
# - Lucas Nerebeck – RM XXXXXXX
# -----------------------------------------------------------

# Objetivo:
# Programa que analisa habilidades, experiências e interesses
# e recomenda trilhas de carreira do FUTURO DO TRABALHO.
# -----------------------------------------------------------


# ---------------------- FUNÇÕES -----------------------------

def coletar_habilidades():
    """
    Coleta habilidades digitadas e retorna uma lista com elas.
    """
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
                print(f"{i} - {habilidades[i].title()}")

            indice = int(input("Digite o número da habilidade para remover: "))
            removidas.append(habilidades.pop(indice))
            print("Habilidade removida!\n")
            continue
        
        else:
            habilidades.append(entrada)
            print("Habilidade adicionada!\n")

    return habilidades, removidas



def analisar_perfil(habilidades):
    """
    Atribui pontuações para cada trilha com base nas habilidades.
    Retorna a lista das trilhas mais compatíveis.
    """

    trilhas = {
        "Inteligência Artificial": ["programar", "dados", "python", "tecnologia"],
        "Cibersegurança": ["segurança", "rede", "investigar"],
        "Saúde Digital": ["saúde", "biologia", "cuidar"],
        "Economia Criativa": ["arte", "criatividade", "design", "desenhar"],
        "Sustentabilidade": ["natureza", "meio ambiente", "verde"]
    }

    pontuacao = {
        "Inteligência Artificial": 0,
        "Cibersegurança": 0,
        "Saúde Digital": 0,
        "Economia Criativa": 0,
        "Sustentabilidade": 0
    }

    # Calcula pontuação
    for habilidade in habilidades:
        for trilha in trilhas:
            for palavra in trilhas[trilha]:
                if palavra in habilidade:
                    pontuacao[trilha] += 1

    # Acha a maior pontuação
    maior = 0
    for t in pontuacao:
        if pontuacao[t] > maior:
            maior = pontuacao[t]

    # Se nenhuma habilidade encaixa, recomenda trilha genérica
    if maior == 0:
        return ["Empreendedorismo e Aprendizado Contínuo"]

    # Retorna todas trilhas que empataram com maior pontuação
    recomendadas = []
    for t in pontuacao:
        if pontuacao[t] == maior:
            recomendadas.append(t)

    return recomendadas



def gerar_cursos(trilha):
    """
    Recebe uma trilha e devolve os cursos sugeridos.
    """
    if trilha == "Inteligência Artificial":
        return ["Programação Básica", "Lógica", "Fundamentos de IA", "Dados"]
    elif trilha == "Cibersegurança":
        return ["Redes", "Introdução à Criptografia", "Segurança Digital", "Análise de Ameaças"]
    elif trilha == "Saúde Digital":
        return ["Telemedicina", "Biossegurança", "IA na Saúde", "Cuidados Preventivos"]
    elif trilha == "Economia Criativa":
        return ["Design Digital", "Storytelling", "Edição de Imagem", "Criação de Conteúdo"]
    elif trilha == "Sustentabilidade":
        return ["Gestão Ambiental", "Tecnologias Verdes", "Inovações Sustentáveis", "Economia Circular"]
    else:
        return ["Produtividade", "Comunicação", "Organização", "Aprendizado Contínuo"]



def exibir_relatorio(habilidades, removidas, trilhas):
    """
    Exibe um relatório detalhado e formatado.
    """
    print("\n========================================")
    print("🔮 RELATÓRIO FINAL – SKILLBRIDGE")
    print("========================================")

    print("\n🧠 Habilidades informadas:")
    for h in habilidades:
        print(" -", h.title())

    if len(removidas) > 0:
        print("\n🗑️ Habilidades removidas:")
        for r in removidas:
            print(" -", r.title())

    print("\n🚀 Trilhas recomendadas para seu futuro:")
    for t in trilhas:
        print(">>", t.upper())

        cursos = gerar_cursos(t)
        print("   📚 Cursos sugeridos:")
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
