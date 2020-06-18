def ordenar(sorted, desc=False):
    """Funcion para ordenar listas o tuplas"""
    for j, _ in enumerate(sorted):
        for i, _ in enumerate(sorted[:-j]):
            if sorted[i] > sorted[i + 1]:
                sorted[i], sorted[i + 1] = sorted[i + 1], sorted[i]

    return sorted


if __name__ == '__main__':
    li = [5, 9, 3, 1, 2, 8, 4, 7, 6]

    print(li)
    print(ordenar(li))
