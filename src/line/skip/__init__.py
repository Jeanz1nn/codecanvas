def skip(quantity):
    """
    Exibe uma quantidade especificada de linhas em branco.

    :param quantity: O número de linhas em branco a serem exibidas (int).
    :return: Não retorna nada.
    """
    for count in range(1, quantity + 1):
        print()
