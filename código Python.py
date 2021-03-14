import pyodbc

def ler_arquivo_faturamento():
    caminho = 'C:\\Users\\judson.santana\\Downloads\\Accenture\\Python\\DADOS_FATURAMENTO.txt'
    auxiliar_coleta_dados = []
    with open(caminho,'r', encoding='latin1') as put:
        for linha in put:
            auxiliar_coleta_dados.append(linha[:-1])
        pass
    desfragmentar_informacoes(auxiliar_coleta_dados)
       
def desfragmentar_informacoes(dados):
    dados_desfragmentados = []
    aux = []
    for i in range(len(dados)):
        data = dados[i][0:4] + '-' + dados[i][4:6] + '-' + dados[i][6:8]
        aux.append(data)
        aux.append(dados[i][8:12])
        aux.append(dados[i][12:16])
        aux.append(dados[i][16:])
        dados_desfragmentados.append(aux)
        aux = []

    conexao_servidor(dados_desfragmentados)

def conexao_servidor(dados):
    connect = pyodbc.connect('Driver={SQL Server};'
                        'Server=NVT-847\\SQLEXPRESS;'
                        'Database=Judson_Santana_Python_Atividade02;'
                        'UID=sa;'
                        'PWD=sa;')

    cursor = connect.cursor()
    for i in range(len(dados)):
        cursor.execute('INSERT INTO DADOS VALUES (?, ?, ?, ?)', dados[i][0], dados[i][1], dados[i][2], dados[i][3])
    cursor.commit()

    print('Dados inseridos no banco com sucesso :)')

    verificacao_dados = input('Deseja ver essas informações no terminal (S/N)? ').strip()

    if verificacao_dados.title() == 'S':
        cursor.execute('SELECT * FROM DADOS')
        for row in cursor.fetchall():
            print(row)

ler_arquivo_faturamento()