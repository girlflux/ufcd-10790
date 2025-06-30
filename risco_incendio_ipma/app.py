from flask import Flask, render_template, request, flash, redirect, url_for
from ipma import mapa_dados


app = Flask(__name__)
app.secret_key = 'risco-de-incendio'

def tratar_erro(mensagem):
    '''Função lida com erros, mostra uma mensagem flash e redirecciona para a rota index.'''
    flash(mensagem, "erro")
    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html', mapa_dados = mapa_dados)

if __name__ == "__main__":
    app.run(debug=True)