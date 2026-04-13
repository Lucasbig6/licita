# Licita - Extrator de Dados de Licitações Públicas

![Python](https://img.shields.io/badge/Python-3.13-blue)
![License](https://img.shields.io/badge/License-MIT-green)

Sistema de extração e análise de dados de licitações públicas do Brasil, utilizando a API do [PNCP (Portal Nacional de Contratações Públicas)](https://pncp.gov.br).

## Sobre o Projeto

O **licita** extrai dados de oportunidades de compra pública diretamente da API do PNCP e os armazena em um banco de dados SQLite para análise e acompanhamento.

### Funcionalidades

- Busca automática de oportunidades de compra no PNCP
- Extração de itens detalhados de cada licitação
- Normalização e estruturação dos dados em DataFrames pandas
- Armazenamento persistente em banco SQLite
- Interface de visualização via Jupyter Notebook

## Tecnologias

| Tecnologia | Versão | Uso |
|------------|--------|-----|
| Python | 3.13+ | Linguagem principal |
| pandas | 3.0.2 | Manipulação de dados |
| requests | 2.33.1 | Cliente HTTP |
| SQLite | - | Banco de dados |
| Jupyter | - | Notebooks interativos |
| DuckDB | - | Visualização de dados (VS Code) |

## Estrutura do Projeto

```
licita/
├── data/
│   ├── data.ipynb        # Notebook de extração de dados
│   └── pncp.db           # Banco de dados SQLite
├── .agent/               # Framework de agentes IA
├── requirements.txt      # Dependências Python
└── .venv/                # Ambiente virtual
```

## Instalação

### 1. Clonar o repositório

```bash
https://github.com/Lucasbig6/licita.git
cd licita
```

### 2. Criar ambiente virtual

```bash
python -m venv .venv
```

### 3. Ativar ambiente (Windows)

```bash
.\.venv\Scripts\activate
```

### 4. Instalar dependências

```bash
pip install -r requirements.txt
```

## Uso

### Executar o Notebook de Extração

```bash
jupyter notebook data/data.ipynb
```

### Atualizar Dados

O notebook `data.ipynb` realiza:

1. **Busca de Oportunidades** - Consulta a API do PNCP por licitações com status "recebendo_proposta"
2. **Extração de Itens** - Para cada licitação, busca os itens detalhados
3. **Normalização** - Estrutura os dados JSON em formato tabular
4. **Armazenamento** - Salva os dados no banco SQLite `data/pncp.db`

### Visualizar Dados (VS Code)

Instale a extensão **DuckDB Data File Viewer** no VS Code para visualizar arquivos de dados:

- `.csv`
- `.parquet`
- `.tsv`

## API do PNCP

O projeto utiliza a API pública do Portal Nacional de Contratações Públicas:

```
https://pncp.gov.br/api/search/
https://pncp.gov.br/api/pncp/v1/orgaos/{cnpj}/compras/{ano}/{sequencial}/itens
```

### Exemplo de Endpoints

| Endpoint | Descrição |
|----------|-----------|
| `/search/` | Busca oportunidades de compra |
| `/pncp/v1/orgaos/{cnpj}/compras/{ano}/{sequencial}/itens` | Lista itens de uma compra |

Consulte a [documentação oficial do PNCP](https://pncp.gov.br/api/docs/) para mais informações.

## Banco de Dados

O banco SQLite (`data/pncp.db`) armazena:

- **Oportunidades de compra** - Dados das licitações
- **Itens** - Detalhes dos produtos/serviços licitados
- **Metadados** - Informações de auditoria (timestamps, status)

### Visualizar Estrutura

```bash
sqlite3 data/pncp.db ".schema"
```

## Requisitos

- Python 3.13 ou superior
- pip (gerenciador de pacotes)
- Jupyter Notebook (para executar o notebook)
- Sistema operacional: Windows/macOS/Linux

## Configuração do VS Code

O projeto inclui configurações em `.vscode/settings.json` para visualização de dados:

```json
{
    "workbench.editorAssociations": {
        "*.parquet": "duckdb.dataFileViewer",
        "*.csv": "duckdb.dataFileViewer",
        "*.tsv": "duckdb.dataFileViewer"
    }
}
```

## Framework de Agentes IA

O diretório `.agent/` contém um framework de agentes IA para desenvolvimento assistido, com:

- 20 agentes especialistas
- 36 habilidades modulares
- 11 fluxos de trabalho automatizados

Para usar os scripts de validação:

```bash
# Validação rápida
python .agent/scripts/checklist.py .

# Verificação completa
python .agent/scripts/verify_all.py . --url http://localhost:3000
```

## Contribuição

1. Fork o repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. See the [LICENSE](LICENSE) file for details.

## Disclaimer

Este projeto não é afiliado ao governo brasileiro ou ao PNCP. Os dados são obtidos através da API pública do portal.

---

**pncp.gov.br** - Portal Nacional de Contratações Públicas
