# CodeCanvaS

CodeCanvaS é um pacote Python que permite adicionar estilo e formatação visual ao console.

## Principais Recursos

- Crie textos formatados com cores e estilos personalizados.
- Personalize a aparência do console com temas predefinidos ou personalizados.

## Instalação

Você pode instalar o CodeCanvas usando pip:

```
pip install codecanvas==1.0.0
```

## Uso Básico

Para começar a usar o CodeCanvas, importe os módulos necessários conforme sua necessidade:

```python
from codecanvas import *
```

Agora você pode usar esses módulos para adicionar estilo e formatação ao seu console.

## Módulos Disponíveis

### Color

O pacote `color` permite personalizar as cores do texto e do fundo.

- `color.fore(color)`: Retorna o código de escape ANSI para a cor do texto especificada.
- `color.back(color)`: Retorna o código de escape ANSI para a cor de fundo especificada.

### Item

O pacote `item` oferece funções para criar listas de itens ordenadas e não ordenadas.

- `item.ordered(*items)`: Exibe uma lista ordenada dos itens fornecidos.
- `item.unordered(*items)`: Exibe uma lista não ordenada dos itens fornecidos.

### Line

O pacote `line` fornece funções para desenhar linhas horizontais e verticais, e para pular linhas.

- `line.skip(quantity)`: Exibe uma quantidade especificada de linhas em branco.
- `line.vertical(height)`: Exibe uma linha vertical de barras verticais ("|") com a altura especificada.
- `line.horizontal(width)`: Exibe uma linha horizontal de traços ("-") com a largura especificada.

### Style

O módulo `style` permite aplicar estilos de formatação ao texto, como negrito, sublinhado e inversão.

- `style(decoration)`: Retorna o código de escape ANSI para o estilo de decoração especificado.

### Text

O módulo `text` oferece a função `text()` para exibir textos altamente personalizáveis.

- `text(message)`: Exibe um texto formatado.

### Title

O módulo `title` fornece a função `title()` para exibir títulos formatados com bordas.

- `title(message)`: Exibe um título formatado.

## Licença

Este projeto é licenciado sob a [MIT License](https://opensource.org/licenses/MIT).
