import sqlite3

def database_connection():
    database = sqlite3.connect("data/database.db")
    cursor = database.cursor()
    return database, cursor

def get_transaction():
    database, cursor = database_connection()
    cursor.execute("SELECT * FROM transacoes")
    data = cursor.fetchall()
    transaction = []
    for itens in data:
        transaction.append(
            {
                "description":itens[1],
                "value":itens[2],
                "type":itens[3],
                "date":itens[4]
            }
        )
    return transaction
    
def add_transaction(description,value,type,date):
    database, cursor = database_connection()
    try:
        cursor.execute("INSERT INTO transacoes (descricao, valor, tipo, data) VALUES (?,?,?,?)",(description,value,type,date))
        database.commit()
        return True
    except Exception as e:
        print(e)
    
get_transaction()
    

    
    
# database, cursor = database_connection()
# cursor.execute("""
#                CREATE TABLE IF NOT EXISTS transacoes (
#                    id INTEGER PRIMARY KEY,
#                    descricao TEXT,
#                    valor FLOAT,
#                    tipo TEXT,
#                    data TEXT)""")
# database.commit()