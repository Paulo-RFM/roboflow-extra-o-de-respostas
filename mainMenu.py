import os


def menu():
    print("1. Rodar prova.py")
    print("2. Rodar multipla escolha 1")
    print("3. Rodar multipla escolha 2")
    print("4. Rodar multipla escolha 3")
    print("5. Rodar Multipla escolha com scanner")
    print("6. Sair")
    escolha = input("Escolha uma opção: ")
    return escolha

def rodar_arquivo(arquivo):
    os.system(f'python {arquivo}')

while True:
    escolha = menu()
    if escolha == '1':
        rodar_arquivo('C:/Users/paulo/Documents/pixForce/provas_roboflow.py')
    elif escolha == '2':
        rodar_arquivo('C:/Users/paulo/Documents/pixForce/roboflow_gabarito1.py')
    elif escolha == '3':
        rodar_arquivo('C:/Users/paulo/Documents/pixForce/roboflow_gabarito2.py')
    elif escolha == '4':
        rodar_arquivo('C:/Users/paulo/Documents/pixForce/roboflow_gabarito3.py')
    elif escolha == '5':
        rodar_arquivo('C:/Users/paulo/Documents/pixForce/scanner_gabarito.py')
    elif escolha == '6':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
