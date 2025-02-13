import sqlite3

def database_connection():
    database = sqlite3.connect("data/database.db")
    cursor = database.cursor()
    return database, cursor

def get_transacoes():
    database, cursor = database_connection()
    cursor.execute("SELECT * FROM transacoes")
    data = cursor.fetchall()
    transacoes = []
    for itens in data:
        transacoes.append(
            {
                "descricao":itens[1],
                "valor":itens[2],
                "tipo":itens[3],
                "data":itens[4]
            }
        )
    return transacoes
    
def add_transacao(descricao,valor,tipo,data):
    database, cursor = database_connection()
    try:
        cursor.execute("INSERT INTO transacoes (descricao, valor, tipo, data) VALUES (?,?,?,?)",(descricao,valor,tipo,data))
        database.commit()
        return True
    except Exception as e:
        print(e)
    
get_transacoes()
    

    
    
# database, cursor = database_connection()
# cursor.execute("""
#                CREATE TABLE IF NOT EXISTS transacoes (
#                    id INTEGER PRIMARY KEY,
#                    descricao TEXT,
#                    valor FLOAT,
#                    tipo TEXT,
#                    data TEXT)""")
# database.commit()