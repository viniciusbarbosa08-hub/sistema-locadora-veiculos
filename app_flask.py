from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Função para conectar ao banco de dados
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',       
        password='admin123',       
        database='locadora_veiculos'
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True) # dictionary=True é o segredo para o HTML entender!
    
    # Fazemos um JOIN para buscar o Nome do Cliente e o Modelo do Carro, não apenas os IDs
    query = """
        SELECT l.id, c.nome AS cliente_nome, v.modelo AS veiculo_modelo, 
               l.data_inicio, l.data_fim 
        FROM locacoes l
        JOIN clientes c ON l.clientes_id = c.id
        JOIN veiculos v ON l.veiculos_id = v.id
    """
    cursor.execute(query)
    locacoes_db = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    # Envia os dados do banco para o arquivo HTML
    return render_template('index.html', locacoes=locacoes_db)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    v_id = request.form.get('veiculo_id')
    c_id = request.form.get('cliente_id')
    d_inicio = request.form.get('data_inicio')
    d_fim = request.form.get('data_fim')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO locacoes (veiculos_id, clientes_id, data_inicio, data_fim, valor_total) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (v_id, c_id, d_inicio, d_fim, 0.0))
    conn.commit()
    
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/excluir/<int:id>', methods=['POST'])
def excluir(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM locacoes WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))
@app.route('/editar/<int:id>', methods=['POST'])
def editar(id):
    nova_data = request.form.get('nova_data_fim')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE locacoes SET data_fim = %s WHERE id = %s", (nova_data, id))
    conn.commit()
    
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)