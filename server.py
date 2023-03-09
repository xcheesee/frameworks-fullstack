from flask import Flask, request, render_template # Importa a biblioteca

app = Flask(__name__) # Inicializa a aplicação

@app.route('/') # Cria uma rota
def main():
  
  #http://127.0.0.1:5000/?primeira=6&segunda=7
  
  parUm = request.args.get('primeira')
  parDois = request.args.get('segunda')
  nota1 = request.args.get("nota1")
  nota2 = request.args.get("nota2")
  stringBrabg = ""
  if nota1 is not None and nota2 is not None:
    nota1 = float(nota1)
    nota2 = float(nota2)
    media = (nota1 + nota2) / 2
    situacao = "reprovado" if  media < 5 else "aprovado" if media >= 7 else "dp"
    stringBrabg = f'Nota 1: {str(nota1)} \n Nota 2: {str(nota2)} \n Media: {str((nota1 + nota2) / 2)} \n  Situacao: {situacao}'

  return render_template("index.html", stringBrabg=stringBrabg)

if __name__ == '__main__':
  app.run() # Executa a aplicação