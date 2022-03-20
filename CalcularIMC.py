def IMC(H, W):
    return (W / (H**2))
print("\nEste programa calcula o IMC de N individuos.")
Q = int(input("\nDigite o n° de pessoas que desseja saber o IMC:"))
while Q >= 1:
    P = 1
    H = float(input("\nDigite a altura da pessoa %d (em metros):" %(P)))
    W = float(input("\nDigite o peso da pessoa %d (em KG):" %(P)))
    imc2 = IMC(H, W) 
    print("\nSeu IMC é de %d" %(imc2))
    if imc2 <= 18.5:
        print("\nDe acordo com a tabela de IMC,a pessoa %d, esta com baixo"
              " peso." %(P))
    elif imc2 > 18.5 and imc2 <= 24.9:
        print("\nDe acordo com a tabela de imc, a pessoa %d, esta com o peso"
              " normal." %(P))
    elif imc2 > 24.9 and imc2 <= 29.9:
        print("\nDe acordo com a tabela de imc, a pessoa %d, esta com"
              " sobrepeso." %(P))
    elif imc2 > 29.9 and imc2 <= 34.9:
        print("\nDe acordo com a tabela de imc, a pessoa %d, esta com obesidade"
              " grau 1." %(P))
    elif imc2 > 34.9 and imc2 <= 39.9:
        print("\nDe acordo com a tabela de imc, a pessoa %d, esta com obesidade"
              " grau 2." %(P))
    else:
        print("\nDe acordo com a tabela de imc, a pessoa %d, esta com obesidade"
              " grau 3 ou mórbida." %(P))
    P += 1
    Q -= 1
print("\nA seguir temos uma tabela de IMC e a classificação.")
print("\nAbaixo do peso        -->            Abaixo 18.5"
      "\nNormal                -->            18.5 - 24.9"
      "\nSobrepeso             -->            25 - 29.9"
      "\nObesidade Grau I      -->            30 - 34.9"
      "\nObesidade Grau II     -->            35 - 39.9"
      "\nObesidade Grau III    -->            Maior ou igual a 40")