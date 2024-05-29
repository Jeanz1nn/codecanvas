# CodeCanvas

CodeCanvas é um pacote Python que permite adicionar estilo e formatação visual ao console.

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
from codecanvas.color.fore import fore
from codecanvas.color.back import back
from codecanvas.item.unordered import unordered
from codecanvas.item.ordered import ordered
from codecanvas.line.skip import skip
from codecanvas.line.vertical import vertical
from codecanvas.line.horizontal import horizontal
from codecanvas.style import style
from codecanvas.text import text
from codecanvas.title import title
```

Agora você pode usar esses módulos para adicionar estilo e formatação ao seu console.

## Módulos Disponíveis

### Color

O módulo `color` permite personalizar as cores do texto e do fundo.

- `fore(color)`: Retorna o código de escape ANSI para a cor do texto especificada.
- `back(color)`: Retorna o código de escape ANSI para a cor de fundo especificada.

### Item

O módulo `item` oferece funções para criar listas de itens ordenadas e não ordenadas.

- `ordered(*items)`: Exibe uma lista ordenada dos itens fornecidos.
- `unordered(*items)`: Exibe uma lista não ordenada dos itens fornecidos.

### Line

O módulo `line` fornece funções para desenhar linhas horizontais e verticais, e para pular linhas.

- `skip(quantity)`: Exibe uma quantidade especificada de linhas em branco.
- `vertical(height)`: Exibe uma linha vertical de barras verticais ("|") com a altura especificada.
- `horizontal(width)`: Exibe uma linha horizontal de traços ("-") com a largura especificada.

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
