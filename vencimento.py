from datetime import datetime, timedelta
import sqlite3


def verificar_vencidos():
    
    conexao = sqlite3.connect('farmacia_med.db')
    cursor = conexao.cursor()

    data_atual = datetime.now().strftime("%d-%m-%Y")
    limite = (datetime.now() + timedelta(days=30)).strftime("%d-%m-%Y")

    try:
        cursor.execute(
            """
            SELECT id, nome, data_vencimento, estoque 
            FROM produto 
            WHERE data_vencimento <= ?
            ORDER BY data_vencimento ASC
        """,
            (limite,),
        )

        produtos = cursor.fetchall()

        print("\n--- ALERTA DE VENCIMENTO (Próximos 30 dias ou Vencidos) ---")
        if not produtos:
            print("Nenhum produto prestes a vencer ou vencido.")
        else:
            for p in produtos:
                status = "VENCIDO!" if p[2] < data_atual else "Próximo do vencimento"
                print(
                    f"[{status}] ID: {p[0]} | Nome: {p[1]} | Validade: {p[2]} | Estoque: {p[3]}"
                )

    finally:
        conexao.close()