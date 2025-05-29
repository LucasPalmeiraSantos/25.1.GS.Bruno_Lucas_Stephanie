# Bruno Alves de Souza 566535
# Lucas Palmeira dos Santos 566204
# Stephanie Kolln Sanches 564139

print('REGISTRO DE DESASTRES \n')

# Listas principais com sublistas
dados_gerais = []       # tipo, país, cidade, bairro, rua, total afetados
dados_categorias = []   # crianças, adultos, idosos, mobilidade reduzida, feridos

#Aqui você insere a quantidade de Desastres
qt_desastres = int(input('Insira a quantidade de Desastres: '))

for i in range(qt_desastres): #Utilizamos o FOR para inserirmos os dados de acordo com a quantidade de desastres inseridos
    print()
    print(f"--- Desastre {i + 1} --- \n")
    
    #inputs para obter as informações de desastre
    tipo_desastre = input('Tipo de desastre: ')
    pais = input('País: ')
    cidade = input('Cidade: ')
    bairro = input('Bairro: ')
    rua = input('Rua: ')
    
    #Aqui utilizamos o While para loopar os dados que armazenam quantidade, pois caso o usuario cometa algum erro, ele poderá inserir novamente os dados
    while True:
        total_afetados = int(input('Quantidade de pessoas afetadas: '))
        qtd_criancas = int(input('Número de crianças: '))
        qtd_adultos = int(input('Número de adultos: '))
        qtd_idosos = int(input('Número de idosos: '))
        qtd_mob_reduzida = int(input('Número de pessoas com mobilidade reduzida: '))
        qtd_feridos = int(input('Número de feridos: '))
        print()
        
        soma = qtd_criancas + qtd_adultos + qtd_idosos + qtd_mob_reduzida + qtd_feridos
        
         #Aqui exibimos uma mensagem de erro caso haja uma divergencia de Dados
        if soma != total_afetados:
            print("ERRO: A quantidade total informada diverge da soma dos afetados por grupo \n")
            print("Insira novamente os Dados: \n")
        else:
            #salvando dados nas listas
            dados_gerais.append([tipo_desastre, pais, cidade, bairro, rua, total_afetados])
            dados_categorias.append([qtd_criancas, qtd_adultos, qtd_idosos, qtd_mob_reduzida, qtd_feridos])
            break

print()

#Calcula o total de desastres que foram registrados
total_desastres_registrados = len(dados_gerais)

#Calcula o total de pessoas que foram afetadas pelo desastre
total_geral_afetados = sum([d[5] for d in dados_gerais])

#Total de pessoas em cada categoria somando os dados de todos os desastres
total_criancas = sum([c[0] for c in dados_categorias])
total_adultos = sum([c[1] for c in dados_categorias])
total_idosos = sum([c[2] for c in dados_categorias])
total_mob_reduzida = sum([c[3] for c in dados_categorias])
total_feridos = sum([c[4] for c in dados_categorias])

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
for i, d in enumerate(dados_gerais):
     # Se o total de pessoas afetadas nesse desastre (Indice 5) for maior que o atual "maior_afetados"
    if d[5] > maior_afetados:
        maior_afetados = d[5] # Atualiza o maior número de afetados
        indice_maior = i # Armazena o índice desse desastre


# Dados do desastre mais grave
desastre_mais_grave = dados_gerais[indice_maior]
tipo_maior = desastre_mais_grave[0]
pais_maior = desastre_mais_grave[1]
cidade_maior = desastre_mais_grave[2]
bairro_maior = desastre_mais_grave[3]
rua_maior = desastre_mais_grave[4]
vitimas_maior = desastre_mais_grave[5]


#RELATÓRIO FINAL
print("=== RELATÓRIO FINAL DE DESASTRES ===\n")

# Quantidade total de desastres registrados
print(f"Quantidade total de desastres registrados: {total_desastres_registrados}\n")

print("Pessoas afetadas por categoria:")
print(f"Crianças: {total_criancas} | Adultos: {total_adultos} | Idosos: {total_idosos} | Mobilidade reduzida: {total_mob_reduzida} | Feridos: {total_feridos}\n")

print(f"Categoria mais afetada: {categoria_mais_afetada} (Total: {qtd_mais_afetada})\n")

print(f"Total geral de pessoas afetadas: {total_geral_afetados}\n")

print("Local do desastre mais grave: \n")

print(f"País: {pais_maior}")
print(f"Cidade: {cidade_maior}")
print(f"Bairro: {bairro_maior}")
print(f"Rua: {rua_maior}")
print(f"Desastre: {tipo_maior} | Vítimas: {vitimas_maior}")
