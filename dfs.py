def dfs(grafo, vertice_inicial, vertice_final):
    res, visitados = [], []

    def dfsloop(vertice_atual):
        visitados.append(vertice_atual)
        for adj in grafo[vertice_atual]:
            if vertice_final not in res:
                if adj != vertice_final:
                    if adj not in visitados:
                        dfsloop(adj)
                else:
                    res.append(adj)
                    visitados.append(adj)
            else:
                return res, visitados

    return dfsloop(vertice_inicial)


if __name__ == "__main__":
    grafo = {
        'a': ['b', 'd', 'e'],
        'b': ['a', 'c', 'e'],
        'c': ['b', 'e'],
        'd': ['a', 'e'],
        'e': ['a', 'b', 'c', 'd', 'f'],
        'f': ['e']
    }
    print(dfs(grafo, 'a', 'f'))
