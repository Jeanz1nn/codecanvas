def horizontal(width):
    """
    Exibe uma linha horizontal de traços ("-") com a largura especificada.

    :param width: A largura da linha (int), ou seja, o número de traços a serem exibidos.
    :return: Não retorna nada.
    """
    for count in range(1, width + 1):
        print("-", end="")
    print()
