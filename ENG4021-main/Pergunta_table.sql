-- SQL de criação da tabela para armazenar perguntas do quiz cultural
-- Esta estrutura segue o modelo `Pergunta` definido no arquivo models.py.

CREATE TABLE IF NOT EXISTS QuizCultural_pergunta (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    texto TEXT NOT NULL,
    categoria TEXT NOT NULL DEFAULT '',
    opcao_a TEXT NOT NULL,
    opcao_b TEXT NOT NULL,
    opcao_c TEXT NOT NULL,
    opcao_d TEXT NOT NULL,
    resposta_correta CHAR(1) NOT NULL
);
