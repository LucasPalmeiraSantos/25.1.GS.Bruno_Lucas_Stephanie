# Bruno Alves de Souza 566535
# Lucas Palmeira dos Santos 566204
# Stephanie Kolln Sanches 564139

print('REGISTRO DE DESASTRES \n')

#Listas
dados_gerais = []  # tipo, país, cidade, bairro, rua, total afetados
dados_categorias = []  # crianças, adultos, idosos, mobilidade reduzida, feridos

qt_desastres = int(input('Insira a quantidade de Desastres: '))

# Utilizamos o FOR para inserirmos os dados de acordo com a quantidade de desastres inseridos
for i in range(qt_desastres):

    print(f"--- Desastre {i + 1} --- \n")
    tipo_desastre = input('Tipo de desastre: ')
    pais = input('País: ')
    cidade = input('Cidade: ')
    bairro = input('Bairro: ')
    rua = input('Rua: ')

    # Aqui utilizamos o While para repetir os dados que armazenam quantidade,
    # pois caso o usuário cometa algum erro, ele poderá inserir novamente os dados
    while True:

        total_afetados = int(input('Quantidade de pessoas afetadas: '))
        qtd_criancas = int(input('Número de crianças: '))
        qtd_adultos = int(input('Número de adultos: '))
        qtd_idosos = int(input('Número de idosos: '))
        qtd_mob_reduzida = int(input('Número de pessoas com mobilidade reduzida: '))
        qtd_feridos = int(input('Número de feridos: '))

        soma = qtd_criancas + qtd_adultos + qtd_idosos + qtd_mob_reduzida + qtd_feridos

        if soma != total_afetados:
            print("ERRO: A quantidade total informada diverge da soma dos afetados por grupo \n")
            print("Insira novamente os Dados: \n")

        else:
            # Salvando dados nas listas
            dados_gerais.append([tipo_desastre, pais, cidade, bairro, rua, total_afetados])
            dados_categorias.append([qtd_criancas, qtd_adultos, qtd_idosos, qtd_mob_reduzida, qtd_feridos])
            break

print(dados_gerais)
print(dados_categorias)

# Mostra o total de desastres que foram registrados com base no tamanho da lista
total_desastres_registrados = len(dados_gerais)

# Calcula o total de pessoas que foram afetadas pelos desastres
total_geral_afetados = sum([sublista_geral[5] for sublista_geral in dados_gerais])

# Calcula o total de pessoas em cada categoria somando os dados de todos os desastres
total_criancas = sum([sublista_categoria[0] for sublista_categoria in dados_categorias])
total_adultos = sum([sublista_categoria[1] for sublista_categoria in dados_categorias])
total_idosos = sum([sublista_categoria[2] for sublista_categoria in dados_categorias])
total_mob_reduzida = sum([sublista_categoria[3] for sublista_categoria in dados_categorias])
total_feridos = sum([sublista_categoria[4] for sublista_categoria in dados_categorias])

# Identifica qual categoria foi mais afetada no geral
categorias = [total_criancas, total_adultos, total_idosos, total_mob_reduzida, total_feridos]
nomes_categorias = ["Crianças", "Adultos", "Idosos", "Mobilidade reduzida", "Feridos"]
indice_mais_afetada = categorias.index(max(categorias))
categoria_mais_afetada = nomes_categorias[indice_mais_afetada]
qtd_mais_afetada = categorias[indice_mais_afetada]

# Desastre com maior número de afetados
# Começa com -1 para garantir que qualquer número de vítimas será maior
# e assim o primeiro desastre será considerado inicialmente como o mais grave

maior_afetados = -1
indice_maior = -1

# Percorre a lista de desastres com índice e conteúdo usando enumerate
for i, sublista_geral in enumerate(dados_gerais):

    # Se o total de pessoas afetadas nesse desastre (índice 5) for maior que o atual "maior_afetados"
    if sublista_geral[5] > maior_afetados:
        maior_afetados = sublista_geral[5]  # Atualiza o maior número de afetados
        indice_maior = i  # Armazena o índice desse desastre

# Dados do desastre mais grave
desastre_mais_grave = dados_gerais[indice_maior]
tipo_maior = desastre_mais_grave[0]
pais_maior = desastre_mais_grave[1]
cidade_maior = desastre_mais_grave[2]
bairro_maior = desastre_mais_grave[3]
rua_maior = desastre_mais_grave[4]
vitimas_maior = desastre_mais_grave[5]

# RELATÓRIO FINAL

print("=== RELATÓRIO FINAL DE DESASTRES ===\n")

print(f"Quantidade total de desastres registrados: {total_desastres_registrados}\n")

print("Pessoas afetadas por categoria:")
print(f"Crianças: {total_criancas} "
      f"| Adultos: {total_adultos} "
      f"| Idosos: {total_idosos} "
      f"| Mobilidade reduzida: {total_mob_reduzida} "
      f"| Feridos: {total_feridos}\n")

print(f"Categoria mais afetada: {categoria_mais_afetada} (Total: {qtd_mais_afetada})\n")

print(f"Total geral de pessoas afetadas: {total_geral_afetados}\n")

print("Local do desastre mais grave: \n")
print(f"País: {pais_maior}")
print(f"Cidade: {cidade_maior}")
print(f"Bairro: {bairro_maior}")
print(f"Rua: {rua_maior}")
print(f"Desastre: {tipo_maior} | Vítimas: {vitimas_maior}")
