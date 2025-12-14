# Painel de Gerentes

Um painel interativo desenvolvido em Flask para gerenciamento e acesso de informações de 21 gerências diferentes.

## 📋 Descrição

Este projeto é uma aplicação web que fornece uma interface intuitiva para seleção e acesso de diferentes gerências. O painel permite visualizar informações específicas de cada uma das 21 gerências disponíveis através de uma interface de botões organizada.

**Gerências disponíveis:**
- ANCHIETA
- JARDIM CAMBURI
- BOM JESUS DO ITABAPOANA
- MASTERPLACE
- ICONHA
- NORTE SUL
- MIRACEMA
- ITACIBA
- PIUMA
- JACARAÍPE
- QUISSAMA
- LARANJEIRAS
- SANTO ANTONIO DE PADUA
- MARCILIO DE NORONHA
- SAO FIDELIS
- MONTSERRAT
- CENTRO VILA VELHA
- PORTO CANOA
- CENTRO VIX
- SERRA SEDE
- GLÓRIA

## 🚀 Tecnologias Utilizadas

- **Python 3.x**
- **Flask 2.3.3** - Framework web
- **Werkzeug 2.3.7** - WSGI utilities
- **HTML5** - Estrutura do frontend
- **CSS3** - Estilização

## 📁 Estrutura do Projeto

```
painel-gerentes/
├── app.py                  # Aplicação Flask principal
├── requirements.txt        # Dependências do projeto
├── README.md              # Este arquivo
├── static/                # Arquivos estáticos
│   ├── FUNDO-BI.jpg      # Imagem de fundo
│   ├── Simbolo.png       # Ícone/Logo
│   └── css/
│       └── style.css     # Estilos CSS
└── templates/            # Templates HTML
    ├── index.html        # Página inicial (lista de gerências)
    └── gerencia.html     # Página individual de gerência
```

## 🛠️ Instalação

### Pré-requisitos
- Python 3.7 ou superior
- pip (gerenciador de pacotes do Python)

### Passos de Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/NycollasBlenes-max/painel-gerentes.git
cd painel-gerentes
```

2. **Crie um ambiente virtual (recomendado):**
```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

## 🎯 Como Executar

Para iniciar a aplicação:

```bash
python app.py
```

A aplicação estará disponível em `http://localhost:5000`

## 📱 Funcionalidades

- **Página Inicial**: Apresenta um grid com 21 botões, um para cada gerência
- **Páginas Individuais**: Cada gerência possui sua própria página com informações específicas
- **Normalização de Nomes**: Função que normaliza nomes de lojas removendo acentos para comparações mais robustas
- **Logging**: Sistema de logs que registra quando usuários acessam o sistema

## 🎨 Recursos Visuais

- Logo/Símbolo personalizado
- Imagem de fundo (FUNDO-BI.jpg)
- Interface responsiva com grid de botões
- Estilização CSS moderna

## 📝 Exemplo de Uso

1. Acesse a página inicial
2. Visualize os 21 botões das gerências disponíveis
3. Clique em uma gerência para acessar suas informações
4. Cada gerência tem sua própria página de detalhes

## 🔧 Funcionalidades Principais do Código

### `normalizar_nome_loja()`
Função que normaliza nomes de lojas removendo acentos e convertendo para minúsculas, facilitando comparações entre nomes.

### `index()`
Rota principal que exibe a página com todos os botões das gerências. Inclui logging do acesso dos usuários.

### `gerencia(num)`
Rota dinâmica que exibe a página individual de cada gerência baseada no número.

## 📦 Dependências

- **Flask**: Framework web Python leve e flexível
- **Werkzeug**: Utilidades WSGI para tratamento de requisições

Para informações detalhadas das versões, veja `requirements.txt`

## 🤝 Contribuições

Para contribuir com melhorias:
1. Crie um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está disponível sob a licença MIT.

## 👤 Autor

**NycollasBlenes-max**

## 📞 Contato

Para dúvidas ou sugestões, abra uma issue no repositório.

---

**Última atualização:** 14 de dezembro de 2025
