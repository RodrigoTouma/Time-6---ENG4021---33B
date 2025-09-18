import pandas as pd
from colorama import Fore, Style

# Caminho do arquivo
df = pd.read_csv(r"C:\Users\mathe\OneDrive\Área de Trabalho\PUC - Rio 2025.2\Projeto de Software\perguntas_quiz_cultural_30.csv")

# Sistema de pontuação
pontuacao_regras = {
    "Fácil": {"certo": 5, "errado": -2},
    "Média": {"certo": 7, "errado": -1},
    "Difícil": {"certo": 10, "errado": 0}
}

def avaliar_desempenho(pontos, total_maximo):
    if total_maximo == 0:
        return "Sem perguntas jogadas."
    porcentagem = (pontos / total_maximo) * 100
    if porcentagem >= 80:
        return "🌟 Excelente! Você mandou muito bem!"
    elif porcentagem >= 60:
        return "👍 Bom desempenho! Mas dá para melhorar."
    elif porcentagem >= 40:
        return "😐 Regular. Que tal revisar alguns temas culturais?"
    else:
        return "📚 Precisa estudar mais sobre cultura e arte."

def selecionar_perguntas():
    perguntas_f = df[df["Dificuldade"] == "Fácil"].sample(5)
    perguntas_m = df[df["Dificuldade"] == "Média"].sample(3)
    perguntas_d = df[df["Dificuldade"] == "Difícil"].sample(2)
    return pd.concat([perguntas_f, perguntas_m, perguntas_d]).sample(frac=1).reset_index(drop=True)

def rodar_quiz(modo="valendo"):
    print("\n" + "="*55)
    print(Fore.CYAN + "             🎮 BEM-VINDO AO QUIZ CULTURAL 🎮" + Style.RESET_ALL)
    print("="*55 + "\n")
    
    pontuacao = 0
    total_maximo = 0
    vidas = 3 if modo == "valendo" else None
    perguntas = selecionar_perguntas()
    
    for i, row in perguntas.iterrows():
        if modo == "valendo" and vidas == 0:
            print(Fore.RED + "\n💀 Fim de jogo! Você perdeu todas as vidas." + Style.RESET_ALL)
            break

        print("\n" + "═"*55)
        print(Fore.YELLOW + f"📌 Pergunta {i+1} | {row['Categoria']} | Dificuldade: {row['Dificuldade']}" + Style.RESET_ALL)
        print("─"*55)
        print(row['Pergunta'] + "\n")
        print(f"   A) {row['Alternativa A']}")
        print(f"   B) {row['Alternativa B']}")
        print(f"   C) {row['Alternativa C']}")
        print(f"   D) {row['Alternativa D']}")
        print("─"*55)
        if modo == "valendo":
            print(Fore.MAGENTA + f"❤️ Vidas: {vidas}   🎯 Pontos: {pontuacao}" + Style.RESET_ALL)
        print("═"*55)

        resposta = input(Fore.WHITE + "👉 Sua resposta (A/B/C/D): " + Style.RESET_ALL).strip().upper()
        
        if resposta == "A":
            escolha = row['Alternativa A']
        elif resposta == "B":
            escolha = row['Alternativa B']
        elif resposta == "C":
            escolha = row['Alternativa C']
        elif resposta == "D":
            escolha = row['Alternativa D']
        else:
            print(Fore.RED + "Resposta inválida! Pulando...\n" + Style.RESET_ALL)
            continue
        
        total_maximo += pontuacao_regras[row["Dificuldade"]]["certo"]
        
        if escolha == row['Resposta Correta']:
            print(Fore.GREEN + "\n✅ Correto!" + Style.RESET_ALL)
            pontuacao += pontuacao_regras[row["Dificuldade"]]["certo"]
        else:
            print(Fore.RED + f"\n❌ Errado! Resposta certa: {row['Resposta Correta']}" + Style.RESET_ALL)
            pontuacao += pontuacao_regras[row["Dificuldade"]]["errado"]
            if modo == "valendo":
                vidas -= 1
    
    print("\n" + "="*55)
    print(Fore.CYAN + f"Fim do Quiz ({'Treino' if modo=='treino' else 'Valendo'})" + Style.RESET_ALL)
    print("="*55)
    print(f"Sua pontuação final: {pontuacao}/{total_maximo}")
    print(avaliar_desempenho(pontuacao, total_maximo))

# Menu inicial
print("Escolha o modo de jogo:")
print("1 - Treino (sem perder vidas)")
print("2 - Valendo (com 3 vidas)")
escolha_modo = input("Digite 1 ou 2: ")

if escolha_modo == "1":
    rodar_quiz(modo="treino")
else:
    rodar_quiz(modo="valendo")
