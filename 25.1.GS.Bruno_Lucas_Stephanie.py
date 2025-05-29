#Bruno Alves de Souza 566535
#Lucas Palmeira dos Santos 566204
#Stephanie Kolln Sanches 564139


qt_desastres = int(input('Insira a quantidade de Desastres: '))

for i in range(0, qt_desastres):
    print()
    print(f"--- Desastre {i + 1} --- \n")
    tipo_desastre = input('Tipo de desastre: ')
    pais = input('País: ')
    cidade = input('Cidade: ')
    bairro = input('Bairro: ')
    rua = input('Rua: ')

    while True:
        qt_pessoas_afetadas = int(input('Quantidade de pessoas afetadas: '))
        nr_criancas = int(input('Número de crianças: '))
        nr_adultos = int(input('Número de adultos: '))
        nr_idosos = int(input('Número de idosos: '))
        nr_mobilidade_reduzida = int(input('Número de pessoas com mobilidade reduzida: '))
        nr_feridos = int(input('Número de feridos: '))
        print()

        soma_validacao = nr_criancas + nr_adultos + nr_idosos + nr_mobilidade_reduzida + nr_feridos
        
        if qt_pessoas_afetadas != soma_validacao:
            print("ERRO: A quantidade total informada diverge da soma dos afetados por grupo \n")
            print("Insira novamente os Dados: \n")
        else:
            break
print()