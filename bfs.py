def bfs(grafo, vertice_inicial, vertice_final):
    res = []
    visitados = [vertice_inicial]
    fila = [grafo[vertice_inicial]]

    while fila:
        fila_vertice = fila.pop(0)
        for adj in fila_vertice:
            if adj != vertice_final:
                if adj not in visitados:
                    visitados.append(adj)
                    for i in grafo[adj]:
                        if i not in visitados:
                            fila.append(i)
            else:
                res.append(adj)
                visitados.append(adj)
                return res, visitados


if __name__ == "__main__":
    grafo = {
        'a': ['b', 'd', 'e'],
        'b': ['a', 'c', 'e'],
        'c': ['b', 'e'],
        'd': ['a', 'e'],
        'e': ['a', 'b', 'c', 'd', 'f'],
        'f': ['e']
    }
    print(bfs(grafo, 'a', 'f'))
