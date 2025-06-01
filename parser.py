from collections import defaultdict

def analizar_sintactico(tokens):
    errores = []
    arbol = []

    # Definir los tipos de tokens válidos para cada parte de la expresión
    tokens_validos = {
        "identificador": ["ID"],
        "operador": ["ASIG"],
        "valor": ["NUM", "ID"],
        "fin": ["FIN"]
    }

    # Si todos los tokens son válidos, continuar con el análisis
    lineas = defaultdict(list)
    for token in tokens:
        lineas[token["linea"]].append(token)

    for linea_num, tokens_linea in sorted(lineas.items()):
        i = 0
        if len(tokens_linea) == 0:
            continue

        # Primero verificar si hay un punto y coma y si hay tokens después de él
        tiene_punto_y_coma = False
        posicion_punto_y_coma = -1
        for i, token in enumerate(tokens_linea):
            if token["tipo"] == "FIN":
                tiene_punto_y_coma = True
                posicion_punto_y_coma = i
                if i < len(tokens_linea) - 1:
                    # Si hay tokens después del punto y coma, reportar error y detener el análisis de esta línea
                    token_invalido = tokens_linea[i + 1]
                    errores.append({
                        "linea": linea_num,
                        "mensaje": f"No se permite ningún carácter después del punto y coma (';'). Se encontró: '{token_invalido['valor']}'",
                        "posicion": token_invalido["posicion"],
                        "longitud": len(token_invalido["valor"])
                    })
                    continue
                break

        # Si se encontró un error después del punto y coma, continuar con la siguiente línea
        if tiene_punto_y_coma and posicion_punto_y_coma < len(tokens_linea) - 1:
            continue

        # Verificar que la línea tenga la estructura básica correcta (ID = VALOR;)
        if len(tokens_linea) < 4:
            # Manejo de errores de estructura
            mensaje_error = ""
            posicion_error = 0
            longitud_error = 1

            if len(tokens_linea) == 0:
                mensaje_error = "Falta un identificador al inicio de la línea"
                posicion_error = 0
            else:
                # Verificar cada componente y su secuencia
                if tokens_linea[0]["tipo"] == "ASIG":
                    mensaje_error = "Falta identificador antes de '='"
                    posicion_error = tokens_linea[0]["posicion"] - 1
                elif len(tokens_linea) >= 2 and tokens_linea[0]["tipo"] == "ID" and tokens_linea[1]["tipo"] != "ASIG":
                    mensaje_error = f"Falta '=' después del identificador '{tokens_linea[0]['valor']}'"
                    posicion_error = tokens_linea[0]["posicion"] + len(tokens_linea[0]["valor"])
                elif len(tokens_linea) >= 2 and tokens_linea[1]["tipo"] == "ASIG" and len(tokens_linea) == 2:
                    mensaje_error = "Falta un valor después del signo '='"
                    posicion_error = tokens_linea[1]["posicion"] + 1
                elif len(tokens_linea) >= 3 and tokens_linea[1]["tipo"] == "ASIG":
                    # Si tenemos ID = VALOR pero falta el punto y coma
                    if tokens_linea[2]["tipo"] in ["NUM", "ID"]:
                        mensaje_error = f"Falta ';' después del valor '{tokens_linea[2]['valor']}'"
                        posicion_error = tokens_linea[2]["posicion"] + len(tokens_linea[2]["valor"])
                    else:
                        mensaje_error = "Falta un valor después del signo '='"
                        posicion_error = tokens_linea[1]["posicion"] + 1
                else:
                    mensaje_error = "Falta un identificador al inicio de la línea"
                    posicion_error = 0

            errores.append({
                "linea": linea_num,
                "mensaje": mensaje_error,
                "posicion": posicion_error,
                "longitud": longitud_error
            })
            continue

        # Verificar que los tokens sean del tipo correcto en el orden esperado
        if tokens_linea[0]["tipo"] != "ID":
            errores.append({
                "linea": linea_num,
                "mensaje": "Se esperaba un identificador válido",
                "posicion": tokens_linea[0]["posicion"],
                "longitud": len(tokens_linea[0]["valor"])
            })
            continue

        if tokens_linea[1]["tipo"] != "ASIG":
            errores.append({
                "linea": linea_num,
                "mensaje": "Se esperaba el signo '='",
                "posicion": tokens_linea[1]["posicion"],
                "longitud": len(tokens_linea[1]["valor"])
            })
            continue

        if tokens_linea[2]["tipo"] not in ["NUM", "ID"]:
            errores.append({
                "linea": linea_num,
                "mensaje": "Se esperaba un número o identificador válido",
                "posicion": tokens_linea[2]["posicion"],
                "longitud": len(tokens_linea[2]["valor"])
            })
            continue

        if tokens_linea[3]["tipo"] != "FIN":
            errores.append({
                "linea": linea_num,
                "mensaje": "Se esperaba ';' al final de la expresión",
                "posicion": tokens_linea[3]["posicion"],
                "longitud": len(tokens_linea[3]["valor"])
            })
            continue

        # Si llegamos aquí, la estructura es correcta
        arbol.append({
            "linea": linea_num,
            "expresion": f"{tokens_linea[0]['valor']} = {tokens_linea[2]['valor']};"
        })

    return arbol, errores