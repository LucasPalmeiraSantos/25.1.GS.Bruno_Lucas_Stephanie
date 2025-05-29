# Bruno Alves de Souza 566535
# Lucas Palmeira dos Santos 566204
# Stephanie Kolln Sanches 564139

qt_desastres = int(input('Digite a quantidade de desastres registrados: '))
i = 0

while i < qt_desastres:
    print(f"\n--- Desastre {i + 1} ---")
    tipo_desastre = input('Tipo de desastre: ')
    pais = input('País: ')
    cidade = input('Cidade: ')
    bairro = input('Bairro: ')
    rua = input('Rua: ')
    qt_pessoas_afetadas = int(input('Quantidade de pessoas afetadas: '))
    nr_criancas = int(input('Número de crianças: '))
    nr_adultos = int(input('Número de adultos: '))
    nr_idosos = int(input('Número de idosos: '))
    nr_mobilidade_reduzida = int(input('Número de pessoas com mobilidade reduzida: '))
    nr_feridos = int(input('Número de feridos: \n'))
    soma_validacao = (nr_feridos + nr_idosos + nr_adultos + nr_criancas + nr_mobilidade_reduzida)

    if qt_pessoas_afetadas != soma_validacao:
        print("A quantidade total informada diverge da soma dos afetados por grupo!")
        print("Informe novamente!")

    else:
        i = i + 1
