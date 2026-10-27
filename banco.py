import sqlite3

def conectar():
    return sqlite3.connect('sistema_farmacia.db')

def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()
    conexao.execute("PRAGMA foreign_keys = ON;")

    cursor.execute(''' CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        CPF TEXT UNIQUE NOT NULL
    )''')
    
    cursor.execute(''' CREATE TABLE IF NOT EXISTS produto(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        estoque INTEGER NOT NULL
    )''')

    cursor.execute(''' CREATE TABLE IF NOT EXISTS vendas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER NOT NULL,
        produto_id INTEGER NOT NULL,
        quantidade INTEGER NOT NULL,
        total REAL NOT NULL,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id),
        FOREIGN KEY (produto_id) REFERENCES produto(id)
    )''')
    conexao.commit()
    conexao.close()
