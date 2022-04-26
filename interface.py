from tkinter import *
from PIL import Image, ImageTk
import networkx as nx
import matplotlib.pyplot as plt
import heapq

# instancia o grafo
Brasil = nx.DiGraph()

# adicionando os nos
Brasil.add_node('RR')
Brasil.add_node('AP')
Brasil.add_node('AM')
Brasil.add_node('AC')
Brasil.add_node('RO')
Brasil.add_node('PA')
Brasil.add_node('AP')
Brasil.add_node('MA')
Brasil.add_node('PI')
Brasil.add_node('CE')
Brasil.add_node('RN')
Brasil.add_node('PB')
Brasil.add_node('PE')
Brasil.add_node('AL')
Brasil.add_node('SE')
Brasil.add_node('BA')
Brasil.add_node('TO')
Brasil.add_node('MT')
Brasil.add_node('GO')
Brasil.add_node('MS')
Brasil.add_node('MG')
Brasil.add_node('ES')
Brasil.add_node('RJ')
Brasil.add_node('SP')
Brasil.add_node('PR')
Brasil.add_node('SC')
Brasil.add_node('RS')

# adicionando as arestas
Brasil.add_edge('RR', 'AM', weight=1)
nx.set_edge_attributes(Brasil, {('RR', 'AM'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('RR', 'PA', weight=1)
nx.set_edge_attributes(Brasil, {('RR', 'PA'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('AP', 'PA', weight=1)
nx.set_edge_attributes(Brasil, {('AP', 'PA'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('AP', 'PA', weight=1)
nx.set_edge_attributes(Brasil, {('AP', 'PA'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('AM', 'PA', weight=1)
nx.set_edge_attributes(Brasil, {('AM', 'PA'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('AM', 'MT', weight=1)
nx.set_edge_attributes(Brasil, {('AM', 'MT'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('AM', 'RO', weight=1)
nx.set_edge_attributes(Brasil, {('AM', 'RO'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('AM', 'AC', weight=1)
nx.set_edge_attributes(Brasil, {('AM', 'AC'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('RR', 'AM', weight=1)
nx.set_edge_attributes(Brasil, {('RR', 'AM'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('RR', 'PA', weight=1)
nx.set_edge_attributes(Brasil, {('RR', 'PA'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('PA', 'RR', weight=1)
nx.set_edge_attributes(Brasil, {('PA', 'RR'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('PA', 'AP', weight=1)
nx.set_edge_attributes(Brasil, {('PA', 'AP'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('PA', 'MA', weight=1)
nx.set_edge_attributes(Brasil, {('PA', 'MA'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('PA', 'TO', weight=1)
nx.set_edge_attributes(Brasil, {('PA', 'TO'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('PA', 'AM', weight=1)
nx.set_edge_attributes(Brasil, {('PA', 'AM'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('PA', 'MT', weight=1)
nx.set_edge_attributes(Brasil, {('PA', 'MT'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('MA', 'PA', weight=1)
nx.set_edge_attributes(Brasil, {('MA', 'PA'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('MA', 'TO', weight=1)
nx.set_edge_attributes(Brasil, {('MA', 'TO'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('MA', 'PI', weight=1)
nx.set_edge_attributes(Brasil, {('MA', 'PI'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('PI', 'MA', weight=1)
nx.set_edge_attributes(Brasil, {('PI', 'MA'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('PI', 'TO', weight=1)
nx.set_edge_attributes(Brasil, {('PI', 'TO'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('PI', 'BA', weight=1)
nx.set_edge_attributes(Brasil, {('PI', 'BA'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('PI', 'PE', weight=1)
nx.set_edge_attributes(Brasil, {('PI', 'PE'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('PI', 'CE', weight=1)
nx.set_edge_attributes(Brasil, {('PI', 'CE'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('CE', 'PI', weight=1)
nx.set_edge_attributes(Brasil, {('CE', 'PI'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('CE', 'RN', weight=1)
nx.set_edge_attributes(Brasil, {('CE', 'RN'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('CE', 'PB', weight=1)
nx.set_edge_attributes(Brasil, {('CE', 'PB'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('CE', 'PE', weight=1)
nx.set_edge_attributes(Brasil, {('CE', 'PE'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('RN', 'CE', weight=1)
nx.set_edge_attributes(Brasil, {('RN', 'CE'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('RN', 'PB', weight=1)
nx.set_edge_attributes(Brasil, {('RN', 'PB'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('PB', 'CE', weight=1)
nx.set_edge_attributes(Brasil, {('PB', 'CE'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('PB', 'RN', weight=1)
nx.set_edge_attributes(Brasil, {('PB', 'RN'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('PB', 'PE', weight=1)
nx.set_edge_attributes(Brasil, {('PB', 'PE'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('PE', 'PB', weight=1)
nx.set_edge_attributes(Brasil, {('PE', 'PB'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('PE', 'CE', weight=1)
nx.set_edge_attributes(Brasil, {('PE', 'CE'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('PE', 'PI', weight=1)
nx.set_edge_attributes(Brasil, {('PE', 'PI'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('PE', 'AL', weight=1)
nx.set_edge_attributes(Brasil, {('PE', 'AL'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('PE', 'BA', weight=1)
nx.set_edge_attributes(Brasil, {('PE', 'BA'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('AL', 'PE', weight=1)
nx.set_edge_attributes(Brasil, {('AL', 'PE'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('AL', 'SE', weight=1)
nx.set_edge_attributes(Brasil, {('AL', 'SE'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('AL', 'BA', weight=1)
nx.set_edge_attributes(Brasil, {('AL', 'BA'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('SE', 'AL', weight=1)
nx.set_edge_attributes(Brasil, {('SE', 'AL'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('SE', 'BA', weight=1)
nx.set_edge_attributes(Brasil, {('SE', 'BA'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('BA', 'SE', weight=1)
nx.set_edge_attributes(Brasil, {('BA', 'SE'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('BA', 'AL', weight=1)
nx.set_edge_attributes(Brasil, {('BA', 'AL'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('BA', 'PE', weight=1)
nx.set_edge_attributes(Brasil, {('BA', 'PE'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('BA', 'PI', weight=1)
nx.set_edge_attributes(Brasil, {('BA', 'PI'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('BA', 'TO', weight=1)
nx.set_edge_attributes(Brasil, {('BA', 'TO'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('BA', 'GO', weight=1)
nx.set_edge_attributes(Brasil, {('BA', 'GO'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('BA', 'MG', weight=1)
nx.set_edge_attributes(Brasil, {('BA', 'MG'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('BA', 'ES', weight=1)
nx.set_edge_attributes(Brasil, {('BA', 'ES'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('TO', 'PA', weight=1)
nx.set_edge_attributes(Brasil, {('TO', 'PA'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('TO', 'MA', weight=1)
nx.set_edge_attributes(Brasil, {('TO', 'MA'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('TO', 'PI', weight=1)
nx.set_edge_attributes(Brasil, {('TO', 'PI'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('TO', 'BA', weight=1)
nx.set_edge_attributes(Brasil, {('TO', 'BA'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('TO', 'GO', weight=1)
nx.set_edge_attributes(Brasil, {('TO', 'GO'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('TO', 'MT', weight=1)
nx.set_edge_attributes(Brasil, {('TO', 'MT'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('MT', 'RO', weight=1)
nx.set_edge_attributes(Brasil, {('MT', 'RO'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('MT', 'AM', weight=1)
nx.set_edge_attributes(Brasil, {('MT', 'AM'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('MT', 'PA', weight=1)
nx.set_edge_attributes(Brasil, {('MT', 'PA'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('MT', 'TO', weight=1)
nx.set_edge_attributes(Brasil, {('MT', 'TO'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('MT', 'GO', weight=1)
nx.set_edge_attributes(Brasil, {('MT', 'GO'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('MT', 'MS', weight=1)
nx.set_edge_attributes(Brasil, {('MT', 'MS'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('RO', 'MT', weight=1)
nx.set_edge_attributes(Brasil, {('RO', 'MT'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('RO', 'AM', weight=1)
nx.set_edge_attributes(Brasil, {('RO', 'AM'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('RO', 'AC', weight=1)
nx.set_edge_attributes(Brasil, {('RO', 'AC'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('AC', 'AM', weight=1)
nx.set_edge_attributes(Brasil, {('AC', 'AM'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('AC', 'RO', weight=1)
nx.set_edge_attributes(Brasil, {('AC', 'RO'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('GO', 'MT', weight=1)
nx.set_edge_attributes(Brasil, {('GO', 'MT'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('GO', 'TO', weight=1)
nx.set_edge_attributes(Brasil, {('GO', 'TO'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('GO', 'BA', weight=1)
nx.set_edge_attributes(Brasil, {('GO', 'BA'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('GO', 'MG', weight=1)
nx.set_edge_attributes(Brasil, {('GO', 'MG'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('GO', 'MS', weight=1)
nx.set_edge_attributes(Brasil, {('GO', 'MS'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('MG', 'BA', weight=1)
nx.set_edge_attributes(Brasil, {('MG', 'BA'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('MG', 'ES', weight=1)
nx.set_edge_attributes(Brasil, {('MG', 'ES'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('MG', 'GO', weight=1)
nx.set_edge_attributes(Brasil, {('MG', 'GO'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('MG', 'RJ', weight=1)
nx.set_edge_attributes(Brasil, {('MG', 'RJ'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('MG', 'SP', weight=1)
nx.set_edge_attributes(Brasil, {('MG', 'SP'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('MG', 'MS', weight=1)
nx.set_edge_attributes(Brasil, {('MG', 'MS'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('ES', 'BA', weight=1)
nx.set_edge_attributes(Brasil, {('ES', 'BA'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('ES', 'MG', weight=1)
nx.set_edge_attributes(Brasil, {('ES', 'MG'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('ES', 'RJ', weight=1)
nx.set_edge_attributes(Brasil, {('ES', 'RJ'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('RJ', 'ES', weight=1)
nx.set_edge_attributes(Brasil, {('RJ', 'ES'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('RJ', 'MG', weight=1)
nx.set_edge_attributes(Brasil, {('RJ', 'MG'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('RJ', 'SP', weight=1)
nx.set_edge_attributes(Brasil, {('RJ', 'SP'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('MS', 'MT', weight=1)
nx.set_edge_attributes(Brasil, {('MS', 'MT'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('MS', 'GO', weight=1)
nx.set_edge_attributes(Brasil, {('MS', 'GO'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('MS', 'MG', weight=1)
nx.set_edge_attributes(Brasil, {('MS', 'MG'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('MS', 'SP', weight=1)
nx.set_edge_attributes(Brasil, {('MS', 'SP'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('MS', 'PR', weight=1)
nx.set_edge_attributes(Brasil, {('MS', 'PR'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('SP', 'RJ', weight=1)
nx.set_edge_attributes(Brasil, {('SP', 'RJ'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('SP', 'MG', weight=1)
nx.set_edge_attributes(Brasil, {('SP', 'MG'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('SP', 'MS', weight=1)
nx.set_edge_attributes(Brasil, {('SP', 'MS'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('SP', 'PR', weight=1)
nx.set_edge_attributes(Brasil, {('SP', 'PR'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('PR', 'MS', weight=1)
nx.set_edge_attributes(Brasil, {('PR', 'MS'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('PR', 'SP', weight=1)
nx.set_edge_attributes(Brasil, {('PR', 'SP'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('PR', 'SC', weight=1)
nx.set_edge_attributes(Brasil, {('PR', 'SC'): {"posto": [2, 3, 6, 5]}})
Brasil.add_edge('SC', 'PR', weight=1)
nx.set_edge_attributes(Brasil, {('SC', 'PR'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('SC', 'RS', weight=1)
nx.set_edge_attributes(Brasil, {('SC', 'RS'): {"posto": [1, 3, 4, 5]}})
Brasil.add_edge('RS', 'SC', weight=1)
nx.set_edge_attributes(Brasil, {('RS', 'SC'): {"posto": [1, 3, 4, 5]}})

estados = list(Brasil.nodes)
estados.sort()
traduz = []
for i in range(len(estados)):
    traduz.append({'estado': str(estados[i]), 'cod': i})

malha_rodoviaria = {}


def retorna_cod_estado(estado):
    for i in range(len(estados)):
        if traduz[i]['estado'] == estado:
            cod = traduz[i]['cod']
    return cod


def retorna_nome_estado(cod):
    estado = str('-')
    for i in range(len(traduz)):
        if traduz[i]['cod'] == int(cod):
            estado = traduz[i]['estado']
    return estado


def dijkstra(grafo, origem, destino):

    INF = ((1 << 63) - 1)//2
    antecessor = {i: i for i in grafo}
    distancia = {i: INF for i in grafo}
    distancia[origem] = 0

    PQ = []
    heapq.heappush(PQ, [distancia[origem], origem])

    while(PQ):

        u = heapq.heappop(PQ)
        u_dist = u[0]
        u_id = u[1]

        if u_dist == distancia[u_id]:

            for v in grafo[u_id]:

                v_id = v[0]
                w_uv = v[1]

                if distancia[u_id] + w_uv < distancia[v_id]:

                    distancia[v_id] = distancia[u_id] + w_uv
                    heapq.heappush(PQ, [distancia[v_id], v_id])
                    antecessor[v_id] = u_id

    if distancia[destino] == INF:

        caminho = str("Não há caminho entre", origem, "e", destino)
        return caminho

    else:

        st = []
        no = destino

        while(True):

            st.append(str(no))
            if(no == antecessor[no]):
                break
            no = antecessor[no]

        caminho = st[::-1]
        return caminho


def bfs(grafo, inicio, fim):

    explorado = []
    fila = [[inicio]]
    if inicio == fim:
        return inicio
    while fila:
        caminho = fila.pop(0)
        no = caminho[-1]
        if no not in explorado:
            vizinhos = grafo[no]
            for vizinho in vizinhos:
                novo_caminho = caminho.copy()
                novo_caminho.append(vizinho)
                fila.append(novo_caminho)
                if vizinho == fim:
                    return novo_caminho
            explorado.append(no)


def reativa_estrada(estado1, estado2):
    Brasil.add_edge(estado1, estado2)
    return


def estados_ligados(estado):
    lista_estados_ligados = Brasil.neighbors(estado)
    return lista_estados_ligados


def imprime_mapa():

    fluxo_livre = [(u, v)
                   for (u, v, d) in Brasil.edges(data=True) if d["weight"] == 1]
    moderado = [(u, v)
                for (u, v, d) in Brasil.edges(data=True) if d["weight"] == 1.6]
    pesado = [(u, v)
              for (u, v, d) in Brasil.edges(data=True) if d["weight"] == 2.5]
    congestionamento = [(u, v) for (u, v, d) in Brasil.edges(
        data=True) if d["weight"] == 5]

    pos = nx.spring_layout(Brasil, seed=9)  # melhores: 3, 9, 20

    nx.draw_networkx_nodes(Brasil, pos, node_size=300, node_color="gray")

    nx.draw_networkx_edges(Brasil, pos, edgelist=fluxo_livre,
                           width=2, alpha=1, edge_color="green", style="solid", connectionstyle="arc3, rad=0.05")
    nx.draw_networkx_edges(Brasil, pos, edgelist=moderado,
                           width=2, alpha=1, edge_color="yellow", style="solid", connectionstyle="arc3, rad=0.05")
    nx.draw_networkx_edges(Brasil, pos, edgelist=pesado,
                           width=2, alpha=1, edge_color="orange", style="solid", connectionstyle="arc3, rad=0.05")
    nx.draw_networkx_edges(Brasil, pos, edgelist=congestionamento,
                           width=2, alpha=1, edge_color="red", style="solid", connectionstyle="arc3, rad=0.05")

    nx.draw_networkx_labels(Brasil, pos, font_size=10,
                            font_family="sans-serif", font_weight="bold")

    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()


lista_estradas_inativas = []


def inativa_estrada(estado1, estado2):

    postos = nx.get_edge_attributes(Brasil, "posto")
    posto = postos[(estado1, estado2)]

    Brasil.remove_edge(estado1, estado2)
    lista_estradas_inativas.append(
        {'estado1': estado1, 'estado2': estado2, 'posto': posto})

    return


def traduz_transito(peso):

    if peso == 1:
        resposta = str('Fluxo livre')
        return resposta
    elif peso == 1.6:
        resposta = str('Trânsito mediano')
        return resposta
    elif peso == 2.5:
        resposta = str('Trânsito pesado')
        return resposta
    elif peso == 5:
        resposta = str('Congestionamento')
        return resposta
    else:
        resposta = str('Número errado')
        return resposta


def mostra_estradas_inativas():
    if len(lista_estradas_inativas) == 0:
        return '\nNão há estradas inativas.\n'
    else:
        lista_final = []
        lista_final.append('Estradas inativas:\n')
        for i in range(len(lista_estradas_inativas)):
            lista_final.append(str(i) + '. ' +
                               str(lista_estradas_inativas[i]['estado1']) + ' - ' + str(lista_estradas_inativas[i]['estado2']))
        lista_final = ('\n'.join(lista_final))
        return lista_final


def melhor_caminho(estado_1, estado_2):

    malha_rodoviaria = {}

    estradas = list(Brasil.edges.data())

    for i in range(len(estradas)):

        estado1 = estradas[i][0]
        estado2 = estradas[i][1]
        peso = estradas[i][2]['weight']
        cod_estado1 = retorna_cod_estado(estado1)
        cod_estado2 = retorna_cod_estado(estado2)
        if cod_estado1 not in malha_rodoviaria:
            malha_rodoviaria[cod_estado1] = []

        malha_rodoviaria[cod_estado1].append((cod_estado2, peso))

    lista_final = []
    lista_final.append('O melhor caminho para você utilizar é: ')
    caminho = dijkstra(malha_rodoviaria, retorna_cod_estado(
        estado_1), retorna_cod_estado(estado_2))

    for i in range(len(caminho)):
        if i == (len(caminho) - 1):
            lista_final.append(retorna_nome_estado(caminho[i]))
        else:
            lista_final.append(retorna_nome_estado(caminho[i]) + ' -> ')

    lista_final.append('. Boa viagem!')
    lista_final = (''.join(lista_final))

    return lista_final


def pergunta_caminho():

    lista_estados = list(Brasil.nodes)
    lista_estados.sort()
    lista_final = []
    for i in range(len(lista_estados)):
        if i == (len(lista_estados) - 1):
            lista_final.append(str(lista_estados[i]) + '.')
        else:
            lista_final.append(str(lista_estados[i]) + ', ')

    lista_final = (''.join(lista_final))
    return lista_final


def mostra_estradas():

    lista_estradas = list(Brasil.edges)

    if len(lista_estradas) == 0:
        return '\nNão há estradas ativas.\n'

    lista_final = []
    lista_final.append('Estradas ativas:\n')
    for i in range(len(lista_estradas)):
        lista_final.append(str(i) + '. ' +
                           str(lista_estradas[i][0]) + ' -> ' + str(lista_estradas[i][1]))
    lista_final = ('\n'.join(lista_final))
    return lista_final


def mostra_estradas_transito():

    lista_estradas = list(Brasil.edges.data())

    if len(lista_estradas) == 0:
        return '\nNão há estradas ativas.\n'

    lista_final = []
    lista_final.append('Estradas ativas:\n')
    for i in range(len(lista_estradas)):
        lista_final.append(str(i) + '. ' +
                           str(lista_estradas[i][0]) + ' -> ' + str(lista_estradas[i][1]) + ' - ' + str(traduz_transito(lista_estradas[i][2]['weight'])))
    lista_final = ('\n'.join(lista_final))
    return lista_final


def mostra_estradas_posto():

    lista_estradas = list(Brasil.edges.data())

    if len(lista_estradas) == 0:
        return '\nNão há estradas ativas.\n'

    lista_final = []
    lista_final.append('Estradas ativas:\n')
    for i in range(len(lista_estradas)):
        if len(lista_estradas[i][2]['posto']) == 0:
            lista_final.append(str(i) + '. ' +
                               str(lista_estradas[i][0]) + ' -> ' + str(lista_estradas[i][1]) + ' - ' + 'sem postos credenciados')
        else:
            lista_final.append(str(i) + '. ' +
                               str(lista_estradas[i][0]) + ' -> ' + str(lista_estradas[i][1]) + ' - ' + 'distância dos postos: ' + str(lista_estradas[i][2]['posto']))
    lista_final = ('\n'.join(lista_final))
    return lista_final


def mostra_estradas_transito_ruim():

    lista_estradas = list(Brasil.edges.data())

    if len(lista_estradas) == 0:
        return '\nNão há estradas ativas.\n'

    lista_final = []
    lista_final.append('Estradas ativas:\n')
    for i in range(len(lista_estradas)):
        if lista_estradas[i][2]['weight'] > 1:
            lista_final.append(str(i) + '. ' + str(lista_estradas[i][0]) + ' -> ' + str(
                lista_estradas[i][1]) + ' - ' + str(traduz_transito(lista_estradas[i][2]['weight'])))

    if len(lista_final) > 1:
        lista_final = ('\n'.join(lista_final))
        return lista_final

    else:
        lista_final = str(
            'Neste momento não há estradas com trânsito ruim! :D')
        return lista_final


def sinaliza_transito(estado1, estado2, velo):
    Brasil.remove_edge(estado1, estado2)

    if int(velo) >= 100:
        velocidade = 1
    elif int(velo) >= 60 and int(velo) < 100:
        velocidade = 1.6
    elif int(velo) >= 40 and int(velo) < 60:
        velocidade = 2.5
    elif int(velo) < 40:
        velocidade = 5

    Brasil.add_edge(estado1, estado2, weight=velocidade)
    return


def sinaliza_posto(estado1, estado2, dist):

    postos = nx.get_edge_attributes(Brasil, "posto")
    postos[(estado1, estado2)].append(int(dist))

    return


def pergunta_sinalizar_posto(x, dist):

    lista_estradas = list(Brasil.edges.data())
    cod_estrada = int(x)

    if(int(x) > len(lista_estradas) or int(x) < 0):
        return 'Não existe essa estrada! Digite um número listado.'

    estado_origem = lista_estradas[cod_estrada][0]
    estado_final = lista_estradas[cod_estrada][1]
    lista_final = []

    sinaliza_posto(estado_origem, estado_final, dist)

    lista_final.append('\nO posto no km ' + str(dist) + ' foi sinalizado na estrada que liga ' + estado_origem +
                       ' a ' + estado_final + '.\n')
    lista_final = (''.join(lista_final))
    return lista_final


def pergunta_sinalizar_transito(x, velocidade):

    lista_estradas = list(Brasil.edges.data())
    cod_estrada = int(x)

    if(int(x) > len(lista_estradas) or int(x) < 0):
        return 'Não existe essa estrada! Digite um número listado.'

    estado_origem = lista_estradas[cod_estrada][0]
    estado_final = lista_estradas[cod_estrada][1]
    lista_final = []

    sinaliza_transito(estado_origem, estado_final, velocidade)

    if int(velocidade) >= 100:
        velo = 1
    elif int(velocidade) >= 60 and int(velocidade) < 100:
        velo = 1.6
    elif int(velocidade) >= 40 and int(velocidade) < 60:
        velo = 2.5
    elif int(velocidade) < 40:
        velo = 5

    lista_final.append('\n' + str(traduz_transito(velo)) + '(' + str(velocidade) + ' km/h) foi sinalizado na estrada que liga ' + estado_origem +
                       ' a ' + estado_final + '.\n')
    lista_final = (''.join(lista_final))
    return lista_final


def pergunta_inativar(x):

    lista_estradas = list(Brasil.edges)
    cod_estrada = int(x)

    if(int(x) > len(lista_estradas) or int(x) < 0):
        return 'Não existe essa estrada! Digite um número listado.'

    estado_origem = lista_estradas[cod_estrada][0]
    estado_final = lista_estradas[cod_estrada][1]
    lista_final = []
    inativa_estrada(estado_origem, estado_final)

    lista_final.append('\nA estrada que liga ' + estado_origem +
                       ' a ' + estado_final + ' foi desativada.\n')
    lista_final = (''.join(lista_final))
    return lista_final


def ativa_estrada(estado1, estado2, posto):

    Brasil.add_edge(estado1, estado2, weight=1)
    nx.set_edge_attributes(Brasil, {(estado1, estado2): {"posto": posto}})

    return


def pergunta_ativar(x):

    print(lista_estradas_inativas)

    cod_estrada = int(x)

    if(int(x) > len(lista_estradas_inativas) or int(x) < 0):
        return 'Essa estrada não está inativa! Digite um número listado.'

    estado_origem = lista_estradas_inativas[cod_estrada]['estado1']
    estado_final = lista_estradas_inativas[cod_estrada]['estado2']
    posto = lista_estradas_inativas[cod_estrada]['posto']
    lista_final = []
    ativa_estrada(estado_origem, estado_final, posto)
    lista_estradas_inativas.pop(cod_estrada)

    lista_final.append('\nA estrada que liga ' + estado_origem +
                       ' a ' + estado_final + ' foi reativada.\n')

    lista_final = (''.join(lista_final))
    return lista_final


#
#
#   Funções de Greedy
#
#


def melhor_abastecimento(postos, capacidade):

    lista_paradas = []
    lista_dist = []
    caminho = capacidade
    num = 0

    for i in range(len(postos)-1):

        dist = abs(postos[i+1] - postos[i])

        if dist > capacidade:
            return -1
        else:
            lista_dist.append(abs(postos[i+1] - postos[i]))

    print(lista_dist)

    for i in range(len(lista_dist)):
        if caminho >= lista_dist[i]:
            caminho = caminho - lista_dist[i]
        else:
            caminho = capacidade
            lista_paradas.append(i)
            caminho = caminho - lista_dist[i]
            num += 1

    return lista_paradas


def abastecer(estado_1, estado_2, capacidade):

    malha_rodoviaria = {}

    estradas = list(Brasil.edges.data())

    for i in range(len(estradas)):

        estado1 = estradas[i][0]
        estado2 = estradas[i][1]
        peso = estradas[i][2]['weight']
        cod_estado1 = retorna_cod_estado(estado1)
        cod_estado2 = retorna_cod_estado(estado2)
        if cod_estado1 not in malha_rodoviaria:
            malha_rodoviaria[cod_estado1] = []

        malha_rodoviaria[cod_estado1].append((cod_estado2, peso))

    lista_final = []

    caminho = dijkstra(malha_rodoviaria, retorna_cod_estado(
        estado_1), retorna_cod_estado(estado_2))

    for i in range(len(caminho)):
        lista_final.append(retorna_nome_estado(caminho[i]))

    postos = nx.get_edge_attributes(Brasil, "posto")

    lista_postos = [0]

    for i in range(len(lista_final) - 1):

        lista_postos_atual = postos[(lista_final[i], lista_final[i+1])]
        lista_postos_atual.sort()

        if i == 0:

            if len(lista_postos_atual) == 0:
                return -1
            else:
                for i in range(len(lista_postos_atual)):
                    lista_postos.append(lista_postos_atual[i])

        else:

            ultimo = lista_postos.pop()
            lista_postos.append(ultimo)

            if len(lista_postos_atual) == 0:
                return -1
            else:
                for i in range(len(lista_postos_atual)):
                    lista_postos.append(lista_postos_atual[i]+ultimo)

    paradas = melhor_abastecimento(lista_postos, capacidade)
    saida = []
    saida.append('A melhor maneira de abastecer é parando nos postos: ')

    for i in range(len(paradas)):
        if i == (len(paradas) - 1):
            saida.append(str(paradas[i]) + 'º')
        else:
            saida.append(str(paradas[i]) + 'º -> ')

    saida.append(' posto(s). Boa viagem!')
    saida = (''.join(saida))

    return saida


def interval_scheduling(inicio, fim, part, dest):
    index = list(range(len(inicio)))
    max_set = set()
    prev_event_time = 0
    local_ini = []
    local_fim = []
    for i in index:
        if inicio[i] >= prev_event_time:
            max_set.add(i)
            local_ini.append(part[i] + ' as ' + str(inicio[i]) +
                             'h para ' + dest[i] + ' as ' + str(fim[i]) + 'h')
            local_ini.append('\n')
            # local_ini.append(part[i])
            # local_fim.append(dest[i])
            prev_event_time = fim[i]
    #print(local_ini, local_fim)
    # print(local_ini)
    return ''.join(local_ini)

#
#
#   Interface gráfica
#
#


root = Tk()

root.geometry('1000x800')
root.config(background='White')
root.resizable(width=False, height=False)

imag_1 = Image.open('background.jpg')

imag_1 = ImageTk.PhotoImage(imag_1)

background = Label(image=imag_1)
background.grid(row=0, column=0, columnspan=3)


def estradas_ativas(x):
    global background
    background.grid_forget()
    background = Label(image=imag_1)
    background.grid(row=1, column=0, columnspan=3)

    text = Text(root, width=25, height=30, fg='white', bg='#228B22', font=24)
    text.place(relx=0.5, rely=0.4, anchor=CENTER)
    texto = mostra_estradas()
    text.insert(END, texto)
    if int(x) == 1:
        buttonVoltar = Button(root, text='Voltar', padx=30,
                              pady=5, fg='black', bg='#A8A8A8', border=5, command=caminhoneiro)
        buttonVoltar.place(relx=0.5, rely=0.8, anchor=CENTER)
    else:
        buttonVoltar = Button(root, text='Voltar', padx=30,
                              pady=5, fg='black', bg='#A8A8A8', border=5, command=fiscal)
        buttonVoltar.place(relx=0.5, rely=0.8, anchor=CENTER)


def visualiza_transito(x):
    global background
    background.grid_forget()
    background = Label(image=imag_1)
    background.grid(row=1, column=0, columnspan=3)

    text = Text(root, width=28, height=30, fg='white', bg='#228B22', font=24)
    text.place(relx=0.5, rely=0.4, anchor=CENTER)
    texto = mostra_estradas_transito()
    text.insert(END, texto)
    if int(x) == 1:
        buttonVoltar = Button(root, text='Voltar', padx=30,
                              pady=5, fg='black', bg='#A8A8A8', border=5, command=caminhoneiro)
        buttonVoltar.place(relx=0.5, rely=0.8, anchor=CENTER)
    else:
        buttonVoltar = Button(root, text='Voltar', padx=30,
                              pady=5, fg='black', bg='#A8A8A8', border=5, command=fiscal)
        buttonVoltar.place(relx=0.5, rely=0.8, anchor=CENTER)


def visualiza_transito_ruim(x):
    global background
    background.grid_forget()
    background = Label(image=imag_1)
    background.grid(row=1, column=0, columnspan=3)

    text = Text(root, width=29, height=30, fg='white', bg='#228B22', font=24)
    text.place(relx=0.5, rely=0.4, anchor=CENTER)
    texto = mostra_estradas_transito_ruim()
    text.insert(END, texto)
    if int(x) == 1:
        buttonVoltar = Button(root, text='Voltar', padx=30,
                              pady=5, fg='black', bg='#A8A8A8', border=5, command=caminhoneiro)
        buttonVoltar.place(relx=0.5, rely=0.8, anchor=CENTER)
    else:
        buttonVoltar = Button(root, text='Voltar', padx=30,
                              pady=5, fg='black', bg='#A8A8A8', border=5, command=fiscal)
        buttonVoltar.place(relx=0.5, rely=0.8, anchor=CENTER)


def estradas_ativas_posto(x):
    global background
    background.grid_forget()
    background = Label(image=imag_1)
    background.grid(row=1, column=0, columnspan=3)

    text = Text(root, width=60, height=20, fg='white', bg='#228B22', font=24)
    text.place(relx=0.5, rely=0.35, anchor=CENTER)
    texto = mostra_estradas_posto()
    text.insert(END, texto)

    text = Text(root, width=55, height=3, fg='white', bg='#228B22')
    text.place(relx=0.5, rely=0.05, anchor=CENTER)
    texto = 'Nossa empresa somente abastece em postos credenciados.\nAqui você pode informá-los aos caminhoneiros.\nAbaixo estão listados cada estrada e seus postos:\n'
    text.insert(END, texto)

    text = Text(root, width=60, height=1, fg='white', bg='#228B22')
    text.place(relx=0.5, rely=0.6, anchor=CENTER)
    texto = 'Digite o número da estrada em que você registrar um posto:'
    text.insert(END, texto)
    estrada1 = Entry(root, width=26, fg='black', bg='White')
    estrada1.place(relx=0.5, rely=0.65, anchor=CENTER)

    text = Text(root, width=70, height=1, fg='white', bg='#228B22')
    text.place(relx=0.5, rely=0.7, anchor=CENTER)
    texto = 'Digite a quilometragem onde o posto está localizado nesta estrada:'
    text.insert(END, texto)
    estrada2 = Entry(root, width=26, fg='black', bg='White')
    estrada2.place(relx=0.5, rely=0.76, anchor=CENTER)

    buttonConfirmar = Button(root, text='Confirmar', padx=30, pady=5,
                             fg='black', bg='#A8A8A8', border=5, command=lambda: MyClick3(estrada1.get(), estrada2.get()))
    buttonConfirmar.place(relx=0.5, rely=0.85, anchor=CENTER)

    buttonVoltar = Button(root, text='Voltar', padx=30, pady=5,
                          fg='black', bg='#A8A8A8', border=5, command=lambda: fiscal())
    buttonVoltar.place(relx=0.5, rely=0.95, anchor=CENTER)


def estradas_inativas(y):
    global background
    background.grid_forget()
    background = Label(image=imag_1)
    background.grid(row=1, column=0, columnspan=3)

    if int(y) == 1:
        buttonVoltar = Button(root, text='Voltar', padx=30,
                              pady=5, fg='black', bg='#A8A8A8', border=5, command=caminhoneiro)
        buttonVoltar.place(relx=0.5, rely=0.8, anchor=CENTER)
    else:
        buttonVoltar = Button(root, text='Voltar', padx=30,
                              pady=5, fg='black', bg='#A8A8A8', border=5, command=fiscal)
        buttonVoltar.place(relx=0.5, rely=0.8, anchor=CENTER)

    text = Text(root, width=25, height=30, fg='white', bg='#228B22', font=24)
    text.place(relx=0.5, rely=0.4, anchor=CENTER)
    texto = mostra_estradas_inativas()
    text.insert(END, texto)


def MyClick(atual, dest):
    text = Text(root, width=90, height=2, fg='black', bg='#E0FFFF', font=24)
    text.place(relx=0.5, rely=0.55, anchor=CENTER)
    texto = melhor_caminho(atual, dest)
    text.insert(END, texto)


def MyClick4(atual_horario, dest_horario, qtd, atual_local, dest_local):
    text = Text(root, width=40, height=3, fg='black', bg='#E0FFFF', font=24)
    text.place(relx=0.5, rely=0.65, anchor=CENTER)
    qtd = int(qtd)
    atual_horario = atual_horario.format(qtd).split()
    atual_horario = [int(begin) for begin in atual_horario]

    dest_horario = dest_horario.format(qtd).split()
    dest_horario = [int(end) for end in dest_horario]

    atual_local = atual_local.format(qtd).split()
    atual_local = [(begin) for begin in atual_local]

    dest_local = dest_local.format(qtd).split()
    dest_local = [(end) for end in dest_local]

    texto = interval_scheduling(
        atual_horario, dest_horario, atual_local, dest_local)
    text.insert(END, texto)


def MyClick5(atual, dest, capacidade):
    text = Text(root, width=90, height=2, fg='black', bg='#E0FFFF', font=24)
    text.place(relx=0.5, rely=0.55, anchor=CENTER)
    texto = abastecer(atual, dest, capacidade)
    text.insert(END, texto)


def encontrar():
    global background
    background.grid_forget()
    background = Label(image=imag_1)
    background.grid(row=1, column=0, columnspan=3)

    text = Text(root, width=34, height=2, fg='white', bg='#228B22', font=24)
    text.place(relx=0.5, rely=0.1, anchor=CENTER)
    texto = '\t    Olá, Caminhoneiro!\nNo Brasil nós temos os seguintes estados:\n'
    text.insert(END, texto)

    text = Text(root, width=82, height=1.5, fg='white', bg='#228B22', font=18)
    text.place(relx=0.5, rely=0.17, anchor=CENTER)
    texto = pergunta_caminho()
    text.insert(END, texto)

    text = Text(root, width=33, height=1, fg='white', bg='#228B22', font=16)
    text.place(relx=0.3, rely=0.3, anchor=CENTER)
    texto = 'Insira o local de partida: (apenas a sigla)'
    text.insert(END, texto)
    estado_atual = Entry(root, width=10, fg='black', bg='#E0FFFF')
    estado_atual.place(relx=0.3, rely=0.34, anchor=CENTER)

    text = Text(root, width=34, height=1, fg='white', bg='#228B22', font=16)
    text.place(relx=0.7, rely=0.3, anchor=CENTER)
    texto = 'Insira o local da chegada: (apenas a sigla)'
    text.insert(END, texto)
    estado_destino = Entry(root, width=10, fg='black', bg='#E0FFFF')
    estado_destino.place(relx=0.7, rely=0.34, anchor=CENTER)

    buttonConfirmar = Button(root, text='Encontrar', padx=30, pady=5, fg='black', bg='#A8A8A8',
                             border=5, command=lambda: MyClick(estado_atual.get(), estado_destino.get()))
    buttonConfirmar.place(relx=0.5, rely=0.4, anchor=CENTER)

    buttonVoltar = Button(root, text='Voltar', padx=30, pady=5,
                          fg='black', bg='#A8A8A8', border=5, command=lambda: caminhoneiro())
    buttonVoltar.place(relx=0.5, rely=0.8, anchor=CENTER)


def abastecimento():
    global background
    background.grid_forget()
    background = Label(image=imag_1)
    background.grid(row=1, column=0, columnspan=3)

    text = Text(root, width=34, height=2, fg='white', bg='#228B22', font=24)
    text.place(relx=0.5, rely=0.1, anchor=CENTER)
    texto = '\t    Olá, Caminhoneiro!\nNo Brasil nós temos os seguintes estados:\n'
    text.insert(END, texto)

    text = Text(root, width=82, height=1.5, fg='white', bg='#228B22', font=18)
    text.place(relx=0.5, rely=0.17, anchor=CENTER)
    texto = pergunta_caminho()
    text.insert(END, texto)

    text = Text(root, width=33, height=1, fg='white', bg='#228B22', font=16)
    text.place(relx=0.3, rely=0.3, anchor=CENTER)
    texto = 'Insira o local de partida: (apenas a sigla)'
    text.insert(END, texto)
    estado_atual = Entry(root, width=10, fg='black', bg='#E0FFFF')
    estado_atual.place(relx=0.3, rely=0.34, anchor=CENTER)

    text = Text(root, width=34, height=1, fg='white', bg='#228B22', font=16)
    text.place(relx=0.7, rely=0.3, anchor=CENTER)
    texto = 'Insira o local da chegada: (apenas a sigla)'
    text.insert(END, texto)
    estado_destino = Entry(root, width=10, fg='black', bg='#E0FFFF')
    estado_destino.place(relx=0.7, rely=0.34, anchor=CENTER)

    text = Text(root, width=34, height=1, fg='white', bg='#228B22', font=16)
    text.place(relx=0.5, rely=0.4, anchor=CENTER)
    texto = 'Insira a capacidade do tanque do caminhão:'
    text.insert(END, texto)
    capacidade = Entry(root, width=10, fg='black', bg='#E0FFFF')
    capacidade.place(relx=0.5, rely=0.44, anchor=CENTER)

    buttonConfirmar = Button(root, text='Encontrar', padx=30, pady=5, fg='black', bg='#A8A8A8',
                             border=5, command=lambda: MyClick5(estado_atual.get(), estado_destino.get(), int(capacidade.get())))
    buttonConfirmar.place(relx=0.5, rely=0.6, anchor=CENTER)

    buttonVoltar = Button(root, text='Voltar', padx=30, pady=5,
                          fg='black', bg='#A8A8A8', border=5, command=lambda: caminhoneiro())
    buttonVoltar.place(relx=0.5, rely=0.8, anchor=CENTER)


def MyClick1(atual):
    text = Text(root, width=42, height=2, fg='white', bg='#228B22')
    text.place(relx=0.5, rely=0.82, anchor=CENTER)
    texto = pergunta_inativar(atual)
    text.insert(END, texto)

    text = Text(root, width=25, height=20, fg='white', bg='#228B22', font=18)
    text.place(relx=0.5, rely=0.35, anchor=CENTER)
    texto = mostra_estradas()
    text.insert(END, texto)


def inativar():
    global background
    background.grid_forget()
    background = Label(image=imag_1)
    background.grid(row=1, column=0, columnspan=3)

    text = Text(root, width=25, height=20, fg='white', bg='#228B22', font=18)
    text.place(relx=0.5, rely=0.35, anchor=CENTER)
    texto = mostra_estradas()
    text.insert(END, texto)

    text = Text(root, width=50, height=3, fg='white', bg='#228B22', font=24)
    text.place(relx=0.5, rely=0.05, anchor=CENTER)
    texto = '                Há algum problema com as estradas?\n                 Aqui você pode desativar uma delas.\n    Atualmente temos as seguintes estradas funcionando:\n'
    text.insert(END, texto)

    text = Text(root, width=45, height=1, fg='white', bg='#228B22', font=16)
    text.place(relx=0.5, rely=0.65, anchor=CENTER)
    texto = 'Digite o número da estrada que você deseja desativar:'
    text.insert(END, texto)
    estrada = Entry(root, width=10, fg='black', bg='#E0FFFF')
    estrada.place(relx=0.5, rely=0.7, anchor=CENTER)

    buttonConfirmar = Button(root, text='Confirmar', padx=30, pady=5,
                             fg='black', bg='#A8A8A8', border=5, command=lambda: MyClick1(estrada.get()))
    buttonConfirmar.place(relx=0.5, rely=0.75, anchor=CENTER)

    buttonVoltar = Button(root, text='Voltar', padx=30, pady=5,
                          fg='black', bg='#A8A8A8', border=5, command=lambda: fiscal())
    buttonVoltar.place(relx=0.5, rely=0.9, anchor=CENTER)


def MyClick2(atual):
    text = Text(root, width=41, height=2, fg='white', bg='#228B22')
    text.place(relx=0.5, rely=0.82, anchor=CENTER)
    texto = pergunta_ativar(atual)
    text.insert(END, texto)

    text = Text(root, width=25, height=20,
                fg='white', bg='#228B22', font=18)
    text.place(relx=0.5, rely=0.4, anchor=CENTER)
    texto = mostra_estradas_inativas()
    text.insert(END, texto)


def MyClick3(atual, peso):
    text = Text(root, width=92, height=2, fg='white', bg='#228B22', font=24)
    text.place(relx=0.5, rely=0.75, anchor=CENTER)
    texto = pergunta_sinalizar_posto(atual, peso)
    text.insert(END, texto)

    text = Text(root, width=60, height=20, fg='white', bg='#228B22', font=24)
    text.place(relx=0.5, rely=0.35, anchor=CENTER)
    texto = mostra_estradas_posto()
    text.insert(END, texto)


def reativar():
    global background
    background.grid_forget()
    background = Label(image=imag_1)
    background.grid(row=1, column=0, columnspan=3)

    text = Text(root, width=25, height=25, fg='white', bg='#228B22', font=18)
    text.place(relx=0.5, rely=0.4, anchor=CENTER)
    texto = mostra_estradas_inativas()
    text.insert(END, texto)

    text = Text(root, width=50, height=3, fg='white', bg='#228B22', font=24)
    text.place(relx=0.5, rely=0.05, anchor=CENTER)
    texto = 'Há alguma estrada restaurada?\nAqui você pode reativar uma delas.\nAtualmente temos as seguintes estradas desativadas:\n'
    text.insert(END, texto)

    text = Text(root, width=44, height=1, fg='white', bg='#228B22', font=16)
    text.place(relx=0.5, rely=0.67, anchor=CENTER)
    texto = 'Digite o número da estrada que você deseja reativar:'
    text.insert(END, texto)
    estrada = Entry(root, width=10, fg='black', bg='#E0FFFF')
    estrada.place(relx=0.5, rely=0.7, anchor=CENTER)

    buttonConfirmar = Button(root, text='Confirmar', padx=30, pady=5,
                             fg='black', bg='#A8A8A8', border=5, command=lambda: MyClick2(estrada.get()))
    buttonConfirmar.place(relx=0.5, rely=0.75, anchor=CENTER)

    buttonVoltar = Button(root, text='Voltar', padx=30, pady=5,
                          fg='black', bg='#A8A8A8', border=5, command=lambda: fiscal())
    buttonVoltar.place(relx=0.5, rely=0.9, anchor=CENTER)


def visualiza_cronograma(x):
    global background
    background.grid_forget()
    background = Label(image=imag_1)
    background.grid(row=1, column=0, columnspan=3)

    text = Text(root, width=40, height=1, fg='white', bg='#228B22')
    text.place(relx=0.5, rely=0.2, anchor=CENTER)
    texto = 'Digite o número de tarefas:'
    text.insert(END, texto)
    qtd_ativ = Entry(root, width=26, fg='black', bg='White')
    qtd_ativ.place(relx=0.5, rely=0.25, anchor=CENTER)
    #qtd_ativ1 = conversorInteiro(qtd_ativ)
    #qtd_ativ1 = int(qtd_ativ1)

    text = Text(root, width=54, height=2, fg='white', bg='#228B22')
    text.place(relx=0.25, rely=0.3, anchor=CENTER)
    texto = 'Digite os horarios do local de partida das atividades:\n   (Apenas horarios inteiros, exemplos: 1 4 14 23)'
    text.insert(END, texto)
    partida_horario = Entry(root, width=20, fg='black', bg='White')
    partida_horario.place(relx=0.25, rely=0.35, anchor=CENTER)
    #partida1 = partida.format(qtd_ativ1).split()
    #partida1 = [int(begin) for begin in partida1]

    text = Text(root, width=54, height=2, fg='white', bg='#228B22')
    text.place(relx=0.75, rely=0.3, anchor=CENTER)
    texto = 'Digite os horarios do local do destino das atividades:\n   (Apenas horarios inteiros, exemplos: 5 9 17 24)'
    text.insert(END, texto)
    destino_horario = Entry(root, width=20, fg='black', bg='White')
    destino_horario.place(relx=0.75, rely=0.35, anchor=CENTER)
    #destino1 = destino.format(qtd_ativ1).split()
    #destino1 = [int(end) for end in destino1]

    text = Text(root, width=41, height=1, fg='white', bg='#228B22')
    text.place(relx=0.25, rely=0.5, anchor=CENTER)
    texto = 'Digite o local de partida das atividades:'
    text.insert(END, texto)
    partida_local = Entry(root, width=20, fg='black', bg='White')
    partida_local.place(relx=0.25, rely=0.55, anchor=CENTER)

    text = Text(root, width=41, height=1, fg='white', bg='#228B22')
    text.place(relx=0.75, rely=0.5, anchor=CENTER)
    texto = 'Digite o local do destino das atividades:'
    text.insert(END, texto)
    destino_local = Entry(root, width=20, fg='black', bg='White')
    destino_local.place(relx=0.75, rely=0.55, anchor=CENTER)

    buttonConfirmar = Button(root, text='Criar', padx=30, pady=5, fg='black', bg='#A8A8A8',
                             border=5, command=lambda: MyClick4(partida_horario.get(), destino_horario.get(), qtd_ativ.get(), partida_local.get(), destino_local.get()))
    buttonConfirmar.place(relx=0.5, rely=0.75, anchor=CENTER)

    if int(x) == 1:
        buttonVoltar = Button(root, text='Voltar', padx=30,
                              pady=5, fg='black', bg='#A8A8A8', border=5, command=caminhoneiro)
        buttonVoltar.place(relx=0.5, rely=0.85, anchor=CENTER)


def caminhoneiro():

    global background
    background.grid_forget()
    background = Label(image=imag_1)
    background.grid(row=1, column=0, columnspan=3)

    text = Text(root, width=34, height=4, fg='white', bg='#228B22', font=90)
    text.place(relx=0.5, rely=0.1, anchor=CENTER)
    texto = '\n\t    Olá, Caminhoneiro!\n\tO que você deseja fazer?\n'
    text.insert(END, texto)

    buttonEncontrar = Button(root, text='Encontrar a melhor rota',
                             padx=30, pady=5, fg='black', bg='#A8A8A8', border=5, command=lambda: encontrar())
    buttonEncontrar.place(relx=0.5, rely=0.3, anchor=CENTER)

    buttonMapa = Button(root, text='Ver mapa com estradas atuais', padx=5,
                        pady=5, fg='black', bg='#A8A8A8', border=5, command=lambda: imprime_mapa())
    buttonMapa.place(relx=0.5, rely=0.4, anchor=CENTER)

    buttonVisualizaTransitoRuim = Button(root, text='Consultar escala de abastecimento', padx=30,
                                         pady=5, fg='black', bg='#A8A8A8', border=5, command=lambda: abastecimento())
    buttonVisualizaTransitoRuim.place(relx=0.5, rely=0.5, anchor=CENTER)

    buttonVisualizaCronograma = Button(root, text='Consultar o cronograma de atividades', padx=30,
                                       pady=5, fg='black', bg='#A8A8A8', border=5, command=lambda: visualiza_cronograma(1))
    buttonVisualizaCronograma.place(relx=0.5, rely=0.6, anchor=CENTER)

    buttonVoltar = Button(root, text='Voltar', padx=30,
                          pady=5, fg='black', bg='#A8A8A8', border=5, command=menu)
    buttonVoltar.place(relx=0.5, rely=0.9, anchor=CENTER)


def fiscal():

    global background
    background.grid_forget()
    background = Label(image=imag_1)
    background.grid(row=1, column=0, columnspan=3)

    text = Text(root, width=34, height=4, fg='white', bg='#228B22', font=90)
    text.place(relx=0.5, rely=0.1, anchor=CENTER)
    texto = '\n\t    Olá, Gerente!\n\tO que você deseja fazer?\n'
    text.insert(END, texto)

    buttonInativar = Button(root, text='Bloquear uma estrada', padx=30,
                            pady=5, fg='black', bg='#A8A8A8', border=5, command=lambda: inativar())
    buttonInativar.place(relx=0.5, rely=0.3, anchor=CENTER)

    buttonReativar = Button(root, text='Voltar a permitir uma estrada', padx=30,
                            pady=5, fg='black', bg='#A8A8A8', border=5, command=lambda: reativar())
    buttonReativar.place(relx=0.5, rely=0.4, anchor=CENTER)

    buttonMapa = Button(root, text='Ver mapa com estradas recomendadas', padx=5,
                        pady=5, fg='black', bg='#A8A8A8', border=5, command=lambda: imprime_mapa())
    buttonMapa.place(relx=0.5, rely=0.5, anchor=CENTER)

    buttonEditaTransito = Button(root, text='Cadastrar postos credenciados', padx=5,
                                 pady=5, fg='black', bg='#A8A8A8', border=5, command=lambda: estradas_ativas_posto(0))
    buttonEditaTransito.place(relx=0.5, rely=0.6, anchor=CENTER)

    buttonVoltar = Button(root, text='Voltar', padx=30,
                          pady=5, fg='black', bg='#A8A8A8', border=5, command=menu)
    buttonVoltar.place(relx=0.5, rely=0.9, anchor=CENTER)


def menu():

    global background
    background.grid_forget()
    background = Label(image=imag_1)
    background.grid(row=1, column=0, columnspan=3)

    logo = Image.open('assets/logo.jpg')
    logo = logo.resize((480, 260))
    logo = ImageTk.PhotoImage(logo)
    logo_label = Label(root, image=logo)
    logo_label.image = logo
    logo_label.grid(column=0, row=1)
    logo_label.place(relx=0.5, rely=0.3, anchor=CENTER)

    buttonCaminhoneiro = Button(root, text='Caminhoneiro', padx=30,
                                pady=5, fg='black', bg='#A8A8A8', border=5, command=caminhoneiro)
    buttonCaminhoneiro.place(relx=0.5, rely=0.55, anchor=CENTER)

    buttonFiscal = Button(root, text='Gerente de transporte', padx=29,
                          pady=5, fg='black', bg='#A8A8A8', border=5, command=fiscal)
    buttonFiscal.place(relx=0.5, rely=0.65, anchor=CENTER)

    buttonSaida = Button(root, text='Sair', padx=30, pady=5,
                         fg='black', bg='#A8A8A8', border=5, command=root.quit)
    buttonSaida.place(relx=0.5, rely=0.9, anchor=CENTER)


menu()
root.mainloop()
