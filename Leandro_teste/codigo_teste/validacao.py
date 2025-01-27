
from flask import Flask, render_template, redirect, request, flash, url_for
import json

@app.route('/validar', methods=['POST'])
def validar():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        try:
            conn = conectar_bd()
            cursor = conn.cursor(dictionary=True)
            query = "SELECT * FROM usuarios WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            user = cursor.fetchone()
        except mysql.connector.Error as e:
            print(f"Erro no banco de dados: {e}")
            user = None
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
        
        if user:
            session['user_id'] = user['id']
            session['user_role'] = user['role']
    
    
            if user['role'] == 'rh':
                return redirect('/rh')
            elif user['role'] in ['vendedor', 'gerente']:
                return redirect('/vendas')
            else:
                return render_template('login.html', error='Papel do usuário inválido!')
        else:
            return render_template('login.html', error='Credenciais inválidas!')