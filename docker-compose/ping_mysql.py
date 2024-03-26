import mysql.connector

try:
    conn = mysql.connector.connect(
        host="mysql",
        user="root",
        password="example"
    )
    print("Conexão com o MySQL bem-sucedida!")
    conn.close()
except Exception as e:
    print("Erro ao conectar ao MySQL:", e)
