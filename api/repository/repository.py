import psycopg2
from conexao import get_db_connection


def search_operadoras(query):
    """
    Realiza uma busca textual na tabela de operadoras do banco de dados.
    Retorna os registros mais relevantes com base na consulta.
    """
    try:
        # Conectar ao banco de dados
        conn = get_db_connection()
        cursor = conn.cursor()

        # Consulta SQL para buscar apenas no nome_fantasia 
        sql = """
        SELECT id_operadora, registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero,
               complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, representante,
               cargo_representante, regiao_comercializacao, data_registro_ans, created_at
        FROM operadoras
        WHERE nome_fantasia ILIKE %s
        """
        
        # Executa a consulta com o parâmetro fornecido
        cursor.execute(sql, (f"%{query}%",))
        rows = cursor.fetchall()

     
        colunas = [desc[0] for desc in cursor.description]
        
     
        operadoras = [dict(zip(colunas, row)) for row in rows]

        return operadoras
    except Exception as e:
        print(f"Erro ao buscar operadoras: {e}")
        return []
    finally:
    
        if cursor:
            cursor.close()
        if conn:
            conn.close()