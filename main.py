Entrada = str(
 input(
  "Bem vindo ao site da clinica de vacinação \n caso você seja um cliente, digite 1, caso você seja da administração, digite o código encriptografado."
 ))
#ps: o código é &5)cjs$54%vf

if (Entrada == "1"):
	nome = str(input("Digite o seu nome"))
	cpf = str(input("Digite o seu CPF"))
	#laudo médico e histórico de vacinação receberia uma imagem, vou desenvolver isso dps
	email = str(input("Digite seu email"))
	telefone = str(input("Digite seu telefone"))
	vacina = str(input("Qual vacina você deseja tomar?"))
	dia = str(input("Qual o dia que você gostaria de agendar?"))

if (Entrada == "&5)cjs$54%vf"):
	entrada2 = str(
	 input(
	  "O que você deseja administrar? \n 1. O cadastro dos profissionais enfermeiros da clínica \n 2. As vacinas"
	 ))
	if (entrada2 == 1):
		nomeEnfermeira = str(input("Digite o nome do profissional enfeimeira(o)"))
		cpfEnfermeira = str(input("Digite o cpf do profissional"))
		#laudo médica será desenvolvido dps
		emailEnfermeira = str(input("Digite o email do profissional"))
		telefonePessoalEnfermeira = str(
		 input("Digite o telefone pessoal do profissional"))
		telefoneCasaEnfermeira = str(
		 input("Digite o telefone de casa do profissional"))
		#registro de carteira de trabalho será feita dps
		print("Nome:", nomeEnfermeira, "\n")
		print("CPF:", cpfEnfermeira, "\n")
		print("Telefone Pessoal:", telefonePessoalEnfermeira, "\n")
		print("Telefone de casa:", telefoneCasaEnfermeira, "\n")
	if (entrada2 == 2):
		nomeVacina = str(input("Qual é a vacina?"))
		dataFabricacao = str(input("Qual é sua data de fabricação?"))
		validade = str(input("Qual é sua validade?"))
		