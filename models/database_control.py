import sqlite3

def database_connection():
    database = sqlite3.connect("data/database.db")
    cursor = database.cursor()
    return database, cursor

def add_transacao(descricao,valor,tipo,data):
    database, cursor = database_connection()
    try:
        cursor.execute("INSERT INTO transacoes (descricao, valor, tipo, data) VALUES (?,?,?,?,?)",(descricao,valor,tipo,data))
    except Exception as e:
        print(e)
    
    
    
    
    
    
# database, cursor = database_connection()
# cursor.execute("""
#                CREATE TABLE IF NOT EXISTS transacoes (
#                    id INTEGER PRIMARY KEY,
#                    descricao TEXT,
#                    valor FLOAT,
#                    tipo TEXT,
#                    data TEXT)""")
# database.commit()