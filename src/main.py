import oracledb
import json
import os
from config.db_config import DB_USER, DB_PASSWORD, DB_DSN

colheitas = []

def conectar_banco():
    return oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)

def criar_tabela():
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE colheita_cana (
                id_colheita NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                produtor_nome VARCHAR2(100),
                fazenda_nome VARCHAR2(100),
                hectares_colhidos NUMBER,
                perda_estimativa_percentual NUMBER,
                metodo_colheita VARCHAR2(20) -- 'manual' ou 'mecanica'
            )
        """)
        print("Tabela criada com sucesso.")

def adicionar_colheita():
    try:
        produtor = input("Nome do produtor: ").strip()
        fazenda = input("Nome da fazenda: ").strip()
        hectares = float(input("Hectares colhidos: "))
        perda = float(input("% de perda estimada: "))
        safra = input("Safra (ex: 2023/2024): ").strip()
        mecanizada = input("Colheita mecanizada? (S/N): ").strip().upper()
        metodo = "mecanica" if mecanizada == "S" else "manual"

        with conectar_banco() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO colheita_cana (produtor_nome, fazenda_nome, hectares_colhidos, perda_estimativa_percentual, metodo_colheita)
                VALUES (:1, :2, :3, :4, :5)
            """, (produtor, fazenda, hectares, perda, metodo))
            conn.commit()

        print("✅ Colheita cadastrada com sucesso.")
    except Exception as e:
        print(f"Erro ao inserir: {e}")

def listar_colheitas():
    try:
        with conectar_banco() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM colheita_cana")
            registros = cursor.fetchall()

            if not registros:
                print("Nenhuma colheita registrada.")
                return

            print("\n--- COLHEITAS REGISTRADAS ---")
            for row in registros:
                colheita = {
                    "ID": row[0],
                    "Produtor": row[1],
                    "Fazenda": row[2],
                    "Hectares": row[3],
                    "Perda (%)": row[4],
                    "Método": row[5]
                }
                colheitas.append(colheita)
                print(colheita)

    except Exception as e:
        print(f"Erro ao listar: {e}")

def salvar_json():
    try:
        with open("document/colheitas.json", "w", encoding="utf-8") as f:
            json.dump(colheitas, f, indent=4, ensure_ascii=False)
        print("📁 Dados salvos em colheitas.json")
    except Exception as e:
        print(f"Erro ao salvar JSON: {e}")

def salvar_txt():
    try:
        with open("document/colheitas.txt", "w", encoding="utf-8") as f:
            for item in colheitas:
                linha = f"ID: {item['ID']}, Produtor: {item['Produtor']}, Fazenda: {item['Fazenda']}, Hectares: {item['Hectares']}, Perda: {item['Perda (%)']}%, Método: {item['Método']}\n"
                f.write(linha)
        print("📄 Dados salvos em colheitas.txt")
    except Exception as e:
        print(f"Erro ao salvar TXT: {e}")

def menu():
    while True:
        print("\n🌾 Menu - Sistema de Colheita de Cana")
        print("1. Adicionar nova colheita")
        print("2. Listar colheitas")
        print("3. Salvar colheitas em JSON")
        print("4. Salvar colheitas em TXT")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_colheita()
        elif opcao == "2":
            listar_colheitas()
        elif opcao == "3":
            salvar_json()
        elif opcao == "4":
            salvar_txt()
        elif opcao == "5":
            print("👋 Encerrando o sistema.")
            break
        else:
            print("⚠️ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    os.makedirs("document", exist_ok=True)
    menu()