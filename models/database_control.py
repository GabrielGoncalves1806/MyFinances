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
                "id":itens[0],
                "description":itens[1],
                "value":itens[2],
                "type":itens[3],
                "date":itens[4],
                "category":itens[5]
            }
        )
    return transaction

def get_category(id=None,name=None):
    database, cursor = database_connection()
    if id:
        cursor.execute("SELECT * FROM categorias WHERE id = ?",(id,))
        category_data = cursor.fetchone()
        return {
            "id":category_data[0],
            "nome":category_data[1],
            "cor":category_data[2]
        }
    elif name:
        cursor.execute("SELECT * FROM categorias WHERE nome = ?",(name.lower(),))
        category_id = cursor.fetchone()
        return category_id[0]
    else:
        cursor.execute("SELECT * FROM categorias")
        data = cursor.fetchall()
        category = []
        for itens in data:
            category.append(
                {
                    "nome":itens[1],
                    "cor":itens[2],
                }
            )
        return category

def add_category(name,color):
    database, cursor = database_connection()
    try:
        cursor.execute("INSERT INTO categorias (nome, cor) VALUES (?,?)",(name,color))
        database.commit()
        return True
    except Exception as e:
        print(e)
    
def add_transaction(description,value,type,date,category_id):
    database, cursor = database_connection()
    try:
        cursor.execute("INSERT INTO transacoes (descricao, valor, tipo, data, id_categoria) VALUES (?,?,?,?,?)",(description,value,type,date,category_id))
        database.commit()
        return True
    except Exception as e:
        print(e)
def get_profile_data():
    database, cursor = database_connection()
    cursor.execute("SELECT * FROM profile")
    data = cursor.fetchone()
    return {
        "id":data[0],
        "name":data[1],
        "meta_gastos":data[2],
        "total_gastos":data[3],
        "total_receita":data[4]
    }
    
    
    
# Tabela do perfil  
# database, cursor = database_connection()
# cursor.execute("""
#                CREATE TABLE IF NOT EXISTS profile (
#                    id INTEGER PRIMARY KEY,
#                    name TEXT,
#                    meta_gastos FLOAT,
#                    total_gastos FLOAT,
#	                 total_receita FLOAT
#                )
#                """
# )
# database.commit()

# Tabela das categorias
# database, cursor = database_connection()
# cursor.execute("""
#                CREATE TABLE IF NOT EXISTS categorias (
#                    id INTEGER PRIMARY KEY,
#                    nome TEXT,
#                    cor TEXT
#                )
#                """
# )
# database.commit()

# Tabela das transações
# database, cursor = database_connection()
# cursor.execute("""
#                CREATE TABLE IF NOT EXISTS transacoes (
#                    id INTEGER PRIMARY KEY,
#                    descricao TEXT,
#                    valor FLOAT,
#                    tipo TEXT,
#                    data TEXT)""")
# database.commit()