# Text Functions
Função para criar textos altamente personalizáveis.

```py
codecanvas.text(
    message, 
    align="left", 
    width=0, 
    bold=False, 
    underline=False, 
    transform="", 
    fore_color="reset", 
    back_color="reset"
)
```

- `message`: Mensagem de texto a ser exibida.
- align: Alinhamento do texto (left, center, right). Padrão: left.
- `width`: Largura do texto para alinhamento. Padrão: 0.
- `bold`: Exibir texto em negrito. Padrão: False.
- `underline`: Sublinha o texto. Padrão: False.
- `transform`: Transformação do texto (upper, capitalize, lower). Padrão: "".
- `fore_color`: Cor do texto (fg_black, fg_red, fg_green, fg_yellow, fg_blue, fg_magenta, fg_cyan, fg_white). Padrão: reset.
- `back_color`: Cor do fundo do texto (bg_black, bg_red, bg_green, bg_yellow, bg_blue, bg_magenta, bg_cyan, bg_white). Padrão: reset.

**Exemplo de uso:**

```py
codecanvas.text("Hello, World!", align="center", width=50, bold=True, fore_color="fg_blue")
```