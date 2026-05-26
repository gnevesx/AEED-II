from collections import deque
from heapq import heappop, heappush
from grafo_arroio_grande import (
    heuristica_hospital,
    inicio,
    mapa_arroio_grande,
    objetivo,
    ruas_bloqueadas,
)


'''
Funcao para obter os vizinhos de um no no grafo.
Retorna uma lista de tuplas (vizinho, distancia, nome_da_rua).
'''
def obter_vizinhos(grafo, no):
    return grafo.get(no, [])


'''
Busca em largura (BFS).

A BFS e uma busca as cegas, pois nao usa heuristica. Ela percorre os trechos
por camadas e ignora ruas bloqueadas.
'''
def busca_bfs(grafo, inicio, objetivo, bloqueios):
    fila = deque([(inicio, [inicio], 0)])
    visitados = set([inicio])
    ordem_visitados = []

    while fila:
        no_atual, caminho, custo = fila.popleft()
        ordem_visitados.append(no_atual)

        if no_atual == objetivo:
            return caminho, custo, ordem_visitados

        for vizinho, distancia, rua in obter_vizinhos(grafo, no_atual):
            if rua in bloqueios:
                continue

            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append((vizinho, caminho + [vizinho], custo + distancia))

    return None, 0, ordem_visitados


'''
Busca A*.

f(n) = g(n) + h(n)

g(n): distancia real percorrida pelos trechos de rua.
h(n): distancia em linha reta ate a Santa Casa.
'''
def busca_a_estrela(grafo, heuristica, inicio, objetivo, bloqueios):
    abertos = []
    contador = 0
    heappush(abertos, (heuristica[inicio], contador, inicio, [inicio], 0))

    fechados = set()
    melhor_custo = {inicio: 0}
    ordem_visitados = []

    while abertos:
        _, _, no_atual, caminho, custo = heappop(abertos)

        if no_atual in fechados:
            continue

        fechados.add(no_atual)
        ordem_visitados.append(no_atual)

        if no_atual == objetivo:
            return caminho, custo, ordem_visitados

        for vizinho, distancia, rua in obter_vizinhos(grafo, no_atual):
            if rua in bloqueios or vizinho in fechados:
                continue

            novo_custo = custo + distancia

            if novo_custo < melhor_custo.get(vizinho, float('inf')):
                melhor_custo[vizinho] = novo_custo
                prioridade = novo_custo + heuristica[vizinho]
                contador += 1
                heappush(abertos, (prioridade, contador, vizinho, caminho + [vizinho], novo_custo))

    return None, 0, ordem_visitados


'''
Converte o caminho de nos em uma lista detalhada de trechos.
'''
def trechos_do_caminho(grafo, caminho):
    if not caminho:
        return []

    trechos = []

    for indice in range(len(caminho) - 1):
        origem = caminho[indice]
        destino = caminho[indice + 1]

        for vizinho, distancia, rua in obter_vizinhos(grafo, origem):
            if vizinho == destino:
                trechos.append((rua, distancia, origem, destino))
                break

    return trechos


'''
Compacta nomes de ruas consecutivos para facilitar a leitura da rota.
'''
def ruas_em_ordem(trechos):
    ruas = []

    for rua, _, _, _ in trechos:
        if not ruas or ruas[-1] != rua:
            ruas.append(rua)

    return ruas


def exibir_resultado(titulo, caminho, custo, visitados):
    print(titulo)

    if not caminho:
        print('Caminho nao encontrado')
        print(f'Nos visitados: {len(visitados)}')
        return

    trechos = trechos_do_caminho(mapa_arroio_grande, caminho)
    ruas = ruas_em_ordem(trechos)

    print(f'Ruas do caminho: {" -> ".join(ruas)}')
    print(f'Distancia total aproximada: {custo:.0f} metros')
    print(f'Ruas no caminho: {len(ruas)}')
    print(f'Trechos percorridos: {len(trechos)}')
    print(f'Nos analisados: {len(visitados)}')


def main():
    caminho_bfs, custo_bfs, visitados_bfs = busca_bfs(
        mapa_arroio_grande,
        inicio,
        objetivo,
        ruas_bloqueadas
    )

    caminho_astar, custo_astar, visitados_astar = busca_a_estrela(
        mapa_arroio_grande,
        heuristica_hospital,
        inicio,
        objetivo,
        ruas_bloqueadas
    )

    print('--- Dados do problema ---')
    print('Origem: Rua Andrade Neves, 53')
    print('Destino: Hospital Santa Casa')
    print(f"Ruas bloqueadas: {', '.join(sorted(ruas_bloqueadas))}")

    print('\n--- BFS ---')
    exibir_resultado('', caminho_bfs, custo_bfs, visitados_bfs)

    print('\n--- A* ---')
    exibir_resultado('', caminho_astar, custo_astar, visitados_astar)

    print('\n--- Comparacao ---')
    print(f'BFS analisou {len(visitados_bfs)} nos.')
    print(f'A* analisou {len(visitados_astar)} nos.')
    print(f'Distancia da rota BFS: {custo_bfs:.0f} metros')
    print(f'Distancia da rota A*: {custo_astar:.0f} metros')

    if len(visitados_astar) < len(visitados_bfs):
        print('O A* visitou menos nos porque usou a distancia em linha reta ate a Santa Casa.')
    else:
        print('Neste caso, os algoritmos tiveram desempenho parecido.')

    if custo_astar < custo_bfs:
        diferenca = custo_bfs - custo_astar
        print(f'A rota do A* tambem ficou {diferenca:.0f} metros mais curta que a rota da BFS.')


if __name__ == '__main__':
    main()
