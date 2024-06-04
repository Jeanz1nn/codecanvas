# Title Functions
Função para criar títulos formatados.

```py
codecanvas.title(message, level=1, width=50, bold=False, style="reset")
```

- `message`: Título a ser exibido.
- `level`: Nível do título (1, 2, 3). Padrão: 1.
- `width`: Largura do título. Padrão: 50.
- `bold`: Exibir título em negrito. Padrão: False.
- `style`: Estilo do título (reset, bold, underline, black, red, green, yellow, blue, magenta, cyan, white). Padrão: reset.

**Exemplo de uso:**

```py
codecanvas.title("Título vem aqui!", level=1, width=60, bold=True, style="blue")
```