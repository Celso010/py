aluno = {}
matricula = []


def func_atualizar():
  try:
    posicao = int(input("digite o numero de matricula: "))
    matricula[posicao]
    while True:
      opcao = func_menuAtualizacao()
      if (opcao == 1):
        nameCheckAtualizacao(matricula, posicao)
        break
      elif (opcao == 2):
        sexoCheckAtualizacao(matricula, posicao)
        break
      elif (opcao == 3):
        cpfCheckAtualizacao(matricula, posicao)
        break
      elif (opcao == 4):
        dataCheckAtualizacao(matricula, posicao)
        break
      elif (opcao == 5):
        break
      else:
        print("opção invalida!")
  except IndexError:
    print("matricula não encontrada")


def nameCheckAtualizacao(matricula, posicao):
  while True:
    matricula[posicao]["nome"] = input("Digite o novo nome do aluno: ")
    if aluno["nome"].replace(" ", "").isalpha():
      break
    else:
      print("Nome inválido")

  print("nome atualizado com sucesso!")


def nameCheck(aluno):
  while True:
    aluno["nome"] = input("Digite o nome do aluno: ")
    if aluno["nome"].replace(" ", "").isalpha():
      break
    else:
      print("Nome inválido")


def dataCheckAtualizacao(matricula, posicao):
  while True:
    matricula[posicao]["data"] = input("Digite a nova data do aluno: ")

    if int(aluno['data'][:2]) > 0 and int(aluno['data'][:2]) < 30:
      if int(aluno['data'][2:4]) > 0 and int(aluno['data'][2:4]) < 13:
        if int(aluno['data'][4:]) > 1900 and int(aluno['data'][4:]) < 2023:
          if len(matricula[posicao]["data"]) == 8:
            data_formatada = (f"{aluno['data'][:2]}/"
                              f"{aluno['data'][2:4]}/{aluno['data'][4:]}")
            matricula[posicao]["data"] = data_formatada
          if len(aluno["data"]) == 10:
            if aluno["data"].replace("/", "").isdigit():
              break
            else:
              print("Data inválida, formato DD/MM/AAAA")
          else:
            print("Data inválida, formato DD/MM/AAAA ")
        else:
          print("ano inválido ")
      else:
        print("mes inválido")
    else:
      print("Dia inválido ")

  print("data atualizada com sucesso!")


def dataCheck(aluno):
  while True:
    aluno["data"] = input("Digite a data de nascimento do aluno: ")
    if int(aluno['data'][:2]) > 0 and int(aluno['data'][:2]) < 30:
      if int(aluno['data'][2:4]) > 0 and int(aluno['data'][2:4]) < 13:
        if int(aluno['data'][4:]) > 1900 and int(aluno['data'][4:]) < 2023:
          if len(aluno["data"]) == 8:
            data_formatada = f"{aluno['data'][:2]}/{aluno['data'][2:4]}/{aluno['data'][4:]}"
            aluno['data'] = data_formatada
          if len(aluno["data"]) == 10:
            if aluno["data"].replace("/", "").isdigit():
              break
            else:
              print("Data inválida, formato DD/MM/AAAA ")
          else:
            print("Data inválida, formato DD/MM/AAAA ")
        else:
          print("ano inválido ")
      else:
        print("mes inválido")
    else:
      print("Dia inválido ")


def cpfCheckAtualizacao(matricula, posicao):
  while True:
    matricula[posicao]["cpf"] = input("Digite o novo cpf do aluno: ")

    if len(matricula[posicao]["cpf"]) == 11:
      cpf_formatado = (f"{aluno['cpf'][:3]}."
                       f"{aluno['cpf'][3:6]}."
                       f"{aluno['cpf'][6:9]}-"
                       f"{aluno['cpf'][9:]}")
      matricula[posicao]["cpf"] = cpf_formatado
    if len(aluno["cpf"]) == 14:
      if aluno["cpf"].replace("-", "").replace(".", "").isdigit():
        break
      else:
        print("Cpf inválido")
    else:
      print("Cpf inválido")
  print("cpf atualizado com sucesso!")


def cpfCheck(aluno):
  while True:
    aluno["cpf"] = input("Digite o cpf do aluno: ")
    if len(aluno["cpf"]) == 11:
      cpf_formatado = (f"{aluno['cpf'][:3]}."
                       f"{aluno['cpf'][3:6]}."
                       f"{aluno['cpf'][6:9]}-"
                       f"{aluno['cpf'][9:]}")
      aluno["cpf"] = cpf_formatado
    if len(aluno["cpf"]) == 14:
      if aluno["cpf"].replace("-", "").replace(".", "").isdigit():
        break
      else:
        print("Cpf inválido")
    else:
      print("Cpf inválido")


def sexoCheckAtualizacao(matricula, posicao):
  while True:
    matricula[posicao]["sexo"] = input("Digite o novo sexo do aluno: ")
    if aluno["sexo"] in "SsMm":
      break
    else:
      print("digito invalido")

  print("sexo atualizado com sucesso!")


def sexoCheck(aluno):
  while True:
    aluno["sexo"] = input("Digite o sexo do aluno: ")
    if aluno["sexo"] in "SsMm":
      break
    else:
      print("digito invalido")


def CheckEntrada(aluno):
  nameCheck(aluno)
  sexoCheck(aluno)
  dataCheck(aluno)
  cpfCheck(aluno)
  return aluno


def funcListar():
  while True:
    opcao = func_menuLista()
    if opcao == 1:
      imprimirNome()
    elif opcao == 2:
      imprimirNomeEMatricula()
    elif opcao == 3:
      imprimirNomeEcpf()
    elif opcao == 4:
      imprimirNomeEdata()
    elif opcao == 5:
      imprimirNomeEsexo()
    elif opcao == 6:
      imprimirTudo()
    elif opcao == 7:
      break


def imprimirTudo():
  for p, d in enumerate(matricula):
    print("-" * 30)
    for k, v in d.items():
      print(f"{k}: {v}", end=" ")
      print()
    print(f"matricula : {p}")


def imprimirNome():
  for d in matricula:
    print("-" * 30)
    print(f" aluno {d['nome']}")


def imprimirNomeEMatricula():
  for k, d in enumerate(matricula):
    print("-" * 30)
    print(f"aluno: {d['nome']}, matricula: {k}", end=" ")
    print()


def imprimirNomeEcpf():
  for d in matricula:
    print("-" * 30)
    print(f"aluno: {d['nome']}, cpf: {d['cpf']}", end=" ")
    print()


def imprimirNomeEdata():
  for d in matricula:
    print("-" * 30)
    print(f"aluno: {d['nome']}, data de nacimento: {d['data']}", end=" ")
    print()


def imprimirNomeEsexo():
  for d in matricula:
    print("-" * 30)
    print(f"aluno: {d['nome']}, sexo: {d['sexo']}", end=" ")
    print()


def func_menuLista():
  print("-" * 30)
  print("1.nome")
  print("2.nome matricula")
  print("3.nome e cpf")
  print("4.nome e data")
  print("5.nome e sexo")
  print("6.tudo")
  print("7.sair")
  print("-" * 30)
  return int(input("o que deseja listar: "))


def func_menuAtualizacao():
  print("-" * 30)
  print("1.nome")
  print("2.sexo")
  print("3.cpf")
  print("4.data")
  print("5.sair")
  print("-" * 30)
  return int(input("o que deseja atualizar: "))


def menu_principal():
  print("-" * 30)
  print("\nMenu:")
  print("1. Cadastrar")
  print("2. Excluir")
  print("3. Atualizar")
  print("4. Listar")
  print("5. Sair")
  print("-" * 30)
  return int(input("Escolha uma opção: "))


def func_cadastro():
  cadastro = CheckEntrada(aluno)
  matricula.append(cadastro.copy())


def func_excluir():
  try:
    del matricula[int(input("fale o numero de matricula: "))]
    print("matricula removida")
  except IndexError:
    print("matricula não encontrada")

#Main
while True:
  escolha = menu_principal()
  print()
  if escolha == 1:
    func_cadastro()
    print(matricula)
  elif escolha == 2:
    func_excluir()
  elif escolha == 3:
    func_atualizar()
  elif escolha == 4:
    funcListar()
  elif escolha == 5:
    print("programa encerrado!")
    break
  else:
    print("Opção inválida. Tente novamente.")
