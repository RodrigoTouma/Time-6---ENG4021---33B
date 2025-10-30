# TRIVIVA — Quiz Cultural

Este repositório contém o projeto do Grupo 6 para a disciplina **ENG4021 – Projeto Integrado de Software**. O tema escolhido pelo nosso grupo foi um **quiz cultural** focado em arte, música e cultura em geral. A aplicação foi desenvolvida utilizando o framework **Django** e segue as recomendações do professor Alexandre Meslin.

## 🧑‍💻 Integrantes do grupo

| Nome                | Matrícula (PUC-Rio) | Responsabilidade principal |
|---------------------|----------------------|----------------------------|
| **Matheus Raffaeli** | –                    | Modelagem de banco de dados e documentação (README) |
| **Rodrigo Touma**    | 2510583                    | Autenticação de usuários e integração frontend/backend |
| **Pedro Gabriel**    | –                    | Lógica do quiz, importação de perguntas e suporte técnico |

## 🌟 Objetivo do projeto

A proposta é criar um site de **quiz cultural** que permita ao usuário logar, navegar por perguntas cadastradas e realizar buscas por tema ou palavra‑chave. Os dados das perguntas são armazenados em um banco de dados SQLite via Django ORM, e podem ser gerenciados através da interface administrativa (Django Admin).

### Principais funcionalidades

* **Autenticação de usuários** com login obrigatório para acessar as páginas internas;
* **Cadastro de perguntas** via interface administrativa (/admin) com campos de enunciado, categoria e quatro alternativas;
* **Listagem de perguntas** com paginação e ordenação simples;
* **Busca de perguntas** por texto ou categoria;
* Templates baseados em **Bootstrap 5** para uma aparência limpa e responsiva.

## 🚀 Como executar

> **Pré‑requisitos:** Python 3.10+ instalado. Recomendamos a criação de um ambiente virtual (venv) para isolar as dependências.

1. Clone este repositório ou faça download do ZIP:
   ```bash
   git clone https://github.com/RodrigoTouma/Time-6---ENG4021---33B.git
   cd Time-6---ENG4021---33B/ENG4021-main/Triviva
   ```
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .\.venv\Scripts\activate    # Windows
   ```
3. Instale o Django (versão 5.2 ou superior):
   ```bash
   pip install django
   ```
4. Gere as migrações e crie o banco de dados SQLite:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Crie um usuário administrador para acessar o Django Admin:
   ```bash
   python manage.py createsuperuser
   ```
6. Execute o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```
7. Acesse `http://127.0.0.1:8000/accounts/login/` no navegador, faça login com seu usuário e navegue pelas páginas:
   * `/triviva/home/` – página inicial do quiz;
   * `/triviva/lista/` – lista de todas as perguntas;
   * `/triviva/buscar/?q=arte` – busca por perguntas contendo “arte”;
   * `/admin/` – interface administrativa para cadastrar novas perguntas.

## 🔧 Estrutura do projeto

* `ENG4021-main/Triviva` – diretório do projeto Django;
  * `QuizCultural` – aplicação responsável pelas funcionalidades do quiz;
  * `usuario` – aplicação de autenticação e templates de login;
* `QuizCultural/models.py` – define o modelo `Pergunta` com campos de enunciado, categoria, opções A–D e resposta correta;
* `QuizCultural/views.py` – contém a lógica para exibir a home page, listar perguntas e realizar buscas;
* `QuizCultural/templates/QuizCultural/` – templates HTML para a home e a lista de perguntas;
* `usuario/templates/registration/login.html` – template de login personalizado.

## 🖼️ Design e referências

O layout visual do site foi inspirado no [protótipo do Figma](https://www.figma.com/design/c9IyZjvJF7PwW9fRE3F6DP/Quiz-Cultural) elaborado pelo grupo. As cores e tipografia seguem o estilo moderno sugerido nas aulas de Identidade Visual.

## 📟 Contribuição e licenciamento

Este projeto é acadêmico e não pretende ser distribuído comercialmente. Pull requests e sugestões são bem‑vindos! Para mais detalhes sobre licenciamento, consulte o arquivo [`LICENSE`](LICENSE) caso exista.

---

Desenvolvido com ❤️ pelo grupo **TRIVIVA** para a disciplina ENG4021, sob orientação do Prof. Alexandre Meslin.
