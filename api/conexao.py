import psycopg2

def get_db_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            user="ans_user",
            password="Irene1982",
            dbname="intuitive"
        )
        print("Conexão bem-sucedida!")
        return connection
    except psycopg2.Error as e:
        print(f" Erro ao conectar ao banco de dados: {e}")
        return None



# Testando a conexao com o banco de dados
if __name__ == "__main__":
    conn = get_db_connection()
    if conn:
        conn.close()
        print("Conexão fechada.")
