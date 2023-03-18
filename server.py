from flask import Flask, request, render_template # Importa a biblioteca

app = Flask(__name__) # Inicializa a aplicação

@app.route('/') # Cria uma rota
def main():
  nota1 = request.args.get("nota1")
  nota2 = request.args.get("nota2")
  if nota1 is not None and nota2 is not None:
    nota1 = float(nota1)
    nota2 = float(nota2)
    media = (nota1 + nota2) / 2.0
    situacao = "Reprovado" if  media < 5 else "Aprovado" if media >= 7 else "DP"

  return render_template("index.html", nota1=nota1, nota2=nota2, situacao=situacao, media=media)

if __name__ == '__main__':
  app.run() # Executa a aplicação