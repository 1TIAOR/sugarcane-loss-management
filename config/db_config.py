import oracledb

DB_USER = "rm567008"
DB_PASSWORD = "051099"
DB_DSN = "oracle.fiap.com.br:1521/ORCL"

def get_connection():
    try:
        connection = oracledb.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            dsn=DB_DSN
        )
        return connection
    except oracledb.Error as e:
        print("Erro ao conectar ao banco Oracle:", e)
        return None