from Common.rpc_utils import RPCClient

def menu():
    print("\n======= CLIENTE RPC =======")
    print("1 - SOMA")
    print("2 - MÉDIA")
    print("3 - BUSCA")
    print("0 - Sair")
    return input("Escolha: ")

while True:
    op = menu()

    if op == "1":
        a = int(input("A: "))
        b = int(input("B: "))
        client = RPCClient("service_soma")
        print("Resultado:", client.call({"a": a, "b": b}))

    elif op == "2":
        valores = list(map(float, input("Digite números separados por espaço: ").split()))
        client = RPCClient("service_media")
        print("Resultado:", client.call({"valores": valores}))

    elif op == "3":
        ID = int(input("ID para buscar: "))
        client = RPCClient("service_busca")
        print("Resultado:", client.call({"id": ID}))

    elif op == "0":
        break

    else:
        print("Opção inválida!")
