# -----------------------------------------------------------
# Projeto: SkillBridge - Sistema de Requalificação Inteligente
# Tema: Futuro do Trabalho e Requalificação Profissional
# Aluno: Gustavo Firmino
# RM: 000000 (coloque seu RM)
# -----------------------------------------------------------

# Este programa ajuda profissionais a identificar se sua profissão
# corre risco de automação e sugere novas áreas de aprendizado,
# simulando um sistema de recomendação para o futuro do trabalho.

# ---------------------- FUNÇÕES -----------------------------

def analisar_profissao(profissao):
    """
    Analisa o risco de automação e retorna o nível de risco
    e sugestões de requalificação.
    """
    # Lista de profissões com alto risco de automação
    alto_risco = ["caixa", "motorista", "atendente", "operador", "auxiliar de escritório"]

    # Lista de profissões com risco médio
    medio_risco = ["professor", "enfermeiro", "analista", "engenheiro", "contador"]

    # Normaliza a entrada (tudo minúsculo)
    profissao = profissao.lower()

    # Estruturas condicionais
    if profissao in alto_risco:
        risco = "Alto"
        sugestoes = ["Programação Básica", "Análise de Dados", "Suporte Técnico", "Atendimento Digital com IA"]
    elif profissao in medio_risco:
        risco = "Médio"
        sugestoes = ["Inteligência Artificial Aplicada", "Gestão de Projetos", "Habilidades de Comunicação",
                     "Pensamento Crítico"]
    else:
        risco = "Baixo"
        sugestoes = ["Liderança", "Inovação e Criatividade", "Empreendedorismo Sustentável"]

    return risco, sugestoes


def exibir_recomendacoes(profissao, risco, sugestoes):
    """
    Exibe as recomendações formatadas.
    """
    print("\n--- Resultado da Análise ---")
    print(f"Profissão analisada: {profissao.title()}")
    print(f"Nível de risco de automação: {risco}")
    print("\nSugestões de requalificação para o futuro:")

    # Loop para mostrar lista de sugestões
    for item in sugestoes:
        print(f"- {item}")

    print("\nA requalificação contínua é essencial para se manter relevante no futuro do trabalho!")


# ---------------------- PROGRAMA PRINCIPAL -----------------------------

print("=== Bem-vindo ao SkillBridge ===")
print("Descubra o futuro da sua profissão!\n")

while True:
    profissao_usuario = input("Digite sua profissão (ou 'sair' para encerrar): ")

    # Estrutura de controle para sair do programa
    if profissao_usuario.lower() == "sair":
        print("Encerrando o sistema... Obrigado por usar o SkillBridge!")
        break

    # Chama função de análise
    risco, sugestoes = analisar_profissao(profissao_usuario)

    # Exibe resultado
    exibir_recomendacoes(profissao_usuario, risco, sugestoes)

    print("\n-----------------------------------\n")