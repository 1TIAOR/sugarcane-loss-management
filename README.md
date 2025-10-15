# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Gestão de Perdas na Colheita de Cana-de-Açúcar

## Grupo: DataAgro Solutions

## 👨‍🎓 Integrantes:

- <a href="https://www.linkedin.com/in/gabriel-h-oliveira">Gabriel Oliveira</a>
- <a href="#">Guilherme Filartiga Pereira da Silva</a>
- <a href="#">Thiago Limongi Faria dos Reis</a>
- <a href="#">Gabriel Luiz Fagundes</a>

## 📜 Descrição

Este projeto tem como objetivo analisar e mitigar as perdas durante a colheita de cana-de-açúcar, utilizando técnicas de programação Python com conexão a banco de dados Oracle e análise de dados com a biblioteca pandas. O sistema implementa um CRUD para registrar ocorrências de perda por tipo, data, fazenda e valor estimado, possibilitando um diagnóstico detalhado das causas e permitindo a tomada de decisão baseada em dados.

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Nesta pasta ficarão os arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>config</b>: Posicione aqui arquivos de configuração que são usados para definir parâmetros e ajustes do projeto.

- <b>document</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>scripts</b>: Posicione aqui scripts auxiliares para tarefas específicas do seu projeto. Exemplo: deploy, migrações de banco de dados, backups.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código

### Pré-requisitos

- Python 3.10+
- Biblioteca `oracledb`
- Biblioteca `pandas`

### Instalação

```bash
# Clonar o repositório
git clone https://github.com/1TIAOR/sugarcane-loss-management.git
cd sugarcane-loss-management

# Criar ambiente virtual
python -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
```

### Execução

1. Configure o arquivo `config/db_config.py` com seu usuário e senha Oracle.
2. Execute o script de migração do banco:

```bash
python scripts/create_table.py
```

3. Execute o sistema principal:

```bash
python src/main.py
```

## 🗃 Histórico de lançamentos

- 0.1.0 - 12/10/2025
  - Versão inicial com CRUD funcional e conexão Oracle

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
