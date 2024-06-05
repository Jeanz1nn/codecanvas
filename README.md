# CodeCanvaS

CodeCanvaS é um pacote Python que permite adicionar estilos ao console.

## Índice

- [Instalação](#instalação)
- [Uso Básico](#uso-básico)
- [Módulos Disponíveis](#módulos-disponíveis)
  - [Color](#color)
  - [Style](#style)
- [Exemplos de Uso](#exemplos-de-uso)
- [Documentação Completa](#documentação-completa)
- [Licença](#licença)

## Instalação

Você pode instalar o CodeCanvas usando pip:

```sh
pip install codecanvas
```

## Uso Básico
Para começar a usar o CodeCanvas, importe os módulos necessários conforme sua necessidade:

```python
from codecanvas import *
```

Agora você pode usar esses módulos para adicionar estilo e formatação ao seu console.

## Módulos Disponíveis

## Color
O pacote `color` permite personalizar as cores do texto e do fundo.

`color.fore(color)`: Retorna o código de escape ANSI para a cor do texto especificada.
`color.back(color)`: Retorna o código de escape ANSI para a cor de fundo especificada.

**Cores Disponíveis**
As cores disponíveis para o texto e fundo são:

- black
- red
- green
- yellow
- blue
- magenta
- cyan
- white

### Style
O pacote `style` permite aplicar estilos de formatação ao texto, como negrito e sublinhado.

`style.decoration(decoration):` Retorna o código de escape ANSI para o estilo de decoração especificado.
`style.reset()`: Retorna o código escape ANSI que reseta todos os Estilos e Cores do texto.

**Estilos Disponíveis**
Os estilos disponíveis são:

- bold
- underline

## Exemplos de Uso
Aqui estão alguns exemplos de como usar o CodeCanvas para estilizar o texto no console:

```py
from codecanvas import *

# Exemplo de mudança de cor
print(f"{color.fore('red')}Este texto é vermelho{style.reset()}")

# Exemplo de mudança de fundo
print(f"{color.back('green')}Este texto tem fundo verde{style.reset()}")

# Exemplo de aplicação de estilo
print(f"{style.decoration('bold')}Este texto é negrito{style.reset()}")

# Combinando cor e estilo
print(f"{color.fore('blue')}{style.decoration('underline')}Este texto é azul e sublinhado{style.reset()}")
```

## Documentação Completa
A documentação completa do pacote CodeCanvaS pode ser encontrada na pasta `doc` dentro do repositório do pacote. Essa documentação fornece detalhes adicionais sobre todas as funcionalidades, exemplos avançados e informações sobre a API.

## Licença
Este projeto é licenciado sob a MIT License.