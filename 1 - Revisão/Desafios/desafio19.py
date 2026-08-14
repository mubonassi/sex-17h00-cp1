print("Sistema de Cadastro e Login!")
print("-"*30)

admin = input("Você é administrador? ")

if admin.lower() == "sim":
    usuario = "admin"
    senha = "root123"
else:
    usuario = input("Cadastre um usuário: ")
    senha = input("Cadastre uma senha: ")

print("Faça login!")

login_usuario = input("Digite o usuário: ")
login_senha = input("Digite a senha: ")

if login_usuario == usuario and login_senha == senha:
    print("Login realizado com sucesso!")
else:
    print("Usuário ou senha incorretos!")
