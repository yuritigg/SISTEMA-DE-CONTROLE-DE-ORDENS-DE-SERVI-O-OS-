lista_os = []

def abrir_chamado(lista_os:str, cliente:str, equipamento:str):
    id = len(lista_os)
    lista_os.append({'id' : id,
    'cliente' : cliente,
    'equipamento' : equipamento,
    'defeito': '',
    'status' : 'pendente',
    'valor' : 0.0})

def atualizar_orcamento(lista_os:str, id_os: int, novo_valor: float):
    try:
        lista_os[id_os]['valor'] = novo_valor
    except IndexError: 
        print('Digite um id válido') 

def alterar_status(lista_os:str, id_os:int, novo_status:str):
    try:
        lista_os[id_os]['status'] = novo_status.lower()
    except IndexError: 
        print('Digite um id válido') 

def listar_chamados_por_status(lista_os:str, status:str):
    lista_status = []
    for i in range(len(lista_os)):
        if lista_os[i]['status'] == status.lower():
            lista_status.append(lista_os[i])
    return lista_status
