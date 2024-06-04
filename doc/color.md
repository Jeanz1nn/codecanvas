# Color Package

O pacote `color` permite personalizar as cores do texto e do fundo.

## Back Function
Função para definir a cor de fundo do texto.

```py
color_code = codecanvas.color.back(color)
```

- `color`: Cor do fundo (black, red, green, yellow, blue, magenta, cyan, white).

**Exemplo de uso:**

```py
print(f"{codecanvas.color.back('blue')}Texto com fundo azul{codecanvas.color.back('reset')}")
```

## Fore Function
Função para definir a cor do texto.

```py
color_code = codecanvas.color.fore(color)
```

- `color`: Cor do texto (black, red, green, yellow, blue, magenta, cyan, white).

**Exemplo de uso:**

```py
print(f"{codecanvas.color.fore('green')}Texto em verde{codecanvas.color.fore('reset')}")
```