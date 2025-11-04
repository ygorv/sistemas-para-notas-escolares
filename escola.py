def coletar_dados():
    nome = input("Nome do aluno: ").capitalize()
    notas = input("Digite as notas separadas por espaço: ")
    # Converte as notas digitadas em lista de floats
    notas = list(map(float, notas.split()))
    return {"nome": nome, "notas": notas}

def calcular_media(dados):
    media = sum(dados["notas"]) / len(dados["notas"])
    dados["media"] = media
    return dados

def verificar_situacao(dados):
    if dados["media"] >= 7:
        dados["situacao"] = "Aprovado "
    elif dados["media"] >= 5:
        dados["situacao"] = "Recuperação "
    else:
        dados["situacao"] = "Reprovado "
    return dados

def exibir_resultado(dados):
    print(f"\n Resultado final:")
    print(f"Aluno: {dados['nome']}")
    print(f"Notas: {dados['notas']}")
    print(f"Média: {dados['media']:.2f}")
    print(f"Situação: {dados['situacao']}\n")

def pipeline():
    dados = coletar_dados()
    dados = calcular_media(dados)
    dados = verificar_situacao(dados)
    exibir_resultado(dados)

pipeline()

