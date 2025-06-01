from flask import Flask, render_template, request, jsonify
from lexer import analizar_lexico
from parser import analizar_sintactico
from turing import simular_mt

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analizar", methods=["POST"])
def analizar():
    codigo = request.json.get("codigo", "")
    tokens, errores_lexicos = analizar_lexico(codigo)
    arbol, errores_sintacticos = analizar_sintactico(tokens)

    # Agrupar tokens por línea
    tokens_por_linea = {}
    for token in tokens:
        linea = token["linea"]
        if linea not in tokens_por_linea:
            tokens_por_linea[linea] = []
        tokens_por_linea[linea].append(token)

    return jsonify({
        "tokens_por_linea": tokens_por_linea,
        "errores_lexicos": errores_lexicos,
        "arbol": arbol,
        "errores_sintacticos": errores_sintacticos
    })

@app.route("/turing", methods=["POST"])
def turing():
    cadena = request.json.get("cadena", "")
    resultado, pasos = simular_mt(cadena)
    return jsonify({"resultado": resultado, "pasos": pasos})

if __name__ == "__main__":
    app.run(debug=True)