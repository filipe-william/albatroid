from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    noticias = ['noticia_2025-02-08.html']  # Lista de notícias
    return render_template('paginas/aba da comunidade documentos.html', noticias=noticias)

@app.route('/noticia/<filename>')
def noticia(filename):
    return render_template('noticias/' + filename)

if __name__ == '__main__':
    app.run(debug=True)
