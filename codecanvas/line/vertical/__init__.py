def vertical(height):
    """
    Exibe uma linha vertical de barras verticais ("|") com a altura especificada.

    :param height: A altura da linha (int), ou seja, o número de barras verticais a serem exibidas.
    :return: Não retorna nada.
    """
    for count in range(1, height + 1):
        print("|")
