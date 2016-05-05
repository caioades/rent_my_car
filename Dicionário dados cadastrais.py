import firecall
my_firebase = firecall.Firebase("https://rent-my-car.firebaseio.com/")

dados_cadastrais = {}
dados_cadastrais["Sign up"]="Nome de usuário", "Nome completo", "Email", "Endereço", "CEP", "CPF", "Número do cartão", "Senha"
dados_cadastrais["Login"]="Nome de usuário", "Senha"

my_firebase.put(point="/Dados cadastrais", data=dados_cadastrais)