# Style Package
O pacote `style` permite aplicar estilos como também resetar as configurações

## Decoration Function
Função para aplicar estilos ao texto.

```py
style_code = codecanvas.style.decoration(decoration)
```

- `decoration`: Estilo a ser aplicado (bold, underline).

**Exemplo de uso:**

```py
print(f"{codecanvas.style.decoration('bold')}Texto em Negrito")
```

## Reset Function
Função para resetar configurações de Estilos e Cores.

```py
reset_style = codecanvas.style.reset()
```

- Essa função não possui nenhum parâmetro obrigatório e nem oculto.

**Exemplo de uso:**

```py
# Foi utilizado um estilo de exemplo para mostrar o funcionamento do RESET.
print(f"{codecanvas.style.decoration('bold')}Exemplo {codecanvas.style.reset()}de uso")
```