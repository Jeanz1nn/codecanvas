def unordered(*items):
    """
    Exibe uma lista não ordenada dos itens fornecidos.

    :param items: Uma sequência de itens a serem listados.
    :return: Não retorna nada.
    """
    for index in range(1, len(items) + 1):
        print(f"- {items[index - 1]}")