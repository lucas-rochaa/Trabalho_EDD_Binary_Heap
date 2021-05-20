from arvore_binaria import *
from banco import *
import time
import os

x = select_maxmin()
h = MaxHeap()
dicionario = {}
value = 999
for a in x:
    dicionario[value] = a[0]
    h.put(value)
    value= value - 1

while True:
    #os.system("cls")
    print("(1) - Adicionar novo paciente")
    print("(2) - Chamar próximo paciente")
    print("(3) - Mostrar próximo paciente (sem chamar)")
    print("(4) - Listar os 5 úl1timos chamados")
    print("(5) - Sair do programa")
    choic = int(input("Escolha: "))

    #try:1
    if choic == 1:
        os.system("cls")
        insert("pacientes_novos")
        dicionario.clear()
        value = 999
        for a in x:
            dicionario[value] = a[0]
            h.put(value)
            value= value - 1

        excluir_linha()
        time.sleep(5)

    elif choic == 2:
        os.system("cls")
        pac = h.get()
        id_p = dicionario[pac]
        print("Chamando o número:", str(pac),"\nNome do paciente: ", select_name(id_p), "\nCodigo do paciente: ", id_p)
        insert_ja_chamados(id_p, pac)
        delet(id_p)
        time.sleep(5)


    elif choic == 3:
        os.system("cls")    
        paciente = h.peek()
        print("Proximo da fila:", str(paciente),"\nNome do paciente: ", select_name(paciente), "\nCodigo do paciente: ", dicionario[paciente])
        time.sleep(5)


    elif choic == 4:
        os.system("cls")
        print(ultimo_ci())
        time.sleep(5)

    elif choic ==5:
        os.system("cls")
        excluir_linha()
        print("adeus!")
        break

    
    #except:
        
excluir_linha()
