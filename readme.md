# Previsão Certa

Previsão Certa é um aplicativo simples de previsão do tempo criado com Python usando a biblioteca `tkinter` para a interface gráfica e `requests` para fazer chamadas à API do OpenWeatherMap. A aplicação permite que os usuários insiram o nome de uma cidade e obtenham informações sobre o clima atual, incluindo temperatura, descrição e ícone.

## Funcionalidades

- **Busca de Cidade**: Permite aos usuários inserir o nome de uma cidade para buscar o clima atual.
- **Informações Climáticas**: Exibe a temperatura (em Celsius), uma descrição do clima e um ícone representando o clima.
- **Interface Gráfica**: Utiliza `tkinter` para criar uma interface amigável e responsiva.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **tkinter**: Biblioteca padrão para criação de interfaces gráficas em Python.
- **requests**: Biblioteca para fazer requisições HTTP.
- **Pillow**: Biblioteca para manipulação de imagens (usada para exibir ícones do clima).
- **ttkbootstrap**: Biblioteca para criar interfaces gráficas estilizadas com o framework `ttk`.

## Instalação

Para executar o aplicativo, você precisa ter o Python instalado na sua máquina. Siga as instruções abaixo para configurar o ambiente e instalar as dependências.

1. **Clone o Repositório**:

    ```bash
    git clone https://github.com/seu-usuario/previsao-certa.git
    cd previsao-certa
    ```

2. **Crie e Ative um Ambiente Virtual** (opcional, mas recomendado):

    **No Windows**:
    ```bash
    python -m venv myenv
    myenv\Scripts\activate
    ```

    **No macOS/Linux**:
    ```bash
    python3 -m venv myenv
    source myenv/bin/activate
    ```

3. **Instale as Dependências**:

    ```bash
    pip install requests pillow ttkbootstrap
    ```

4. **Obtenha uma Chave de API do OpenWeatherMap**:

    - Acesse [OpenWeatherMap](https://openweathermap.org/) e registre-se para obter uma chave de API gratuita.
    - Substitua a chave da API no código `weather_app.py`.

## Uso

1. **Execute o Aplicativo**:

    ```bash
    python weather_app.py
    ```

2. **Interaja com a Interface**:

    - Abra a janela da aplicação.
    - Digite o nome de uma cidade e clique em "Search".
    - Visualize as informações do clima exibidas na interface.


