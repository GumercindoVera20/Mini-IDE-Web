import re

def analizar_lexico(codigo):
    # Solo aceptamos estos patrones como válidos
    patron = [
        ("ESPACIO", r"[ \t]+"),  # Espacios y tabs primero
        ("NUM", r"\d+"),  # Números enteros
        ("ID", r"[a-zA-Z][a-zA-Z0-9]*"),  # Solo letras y números
        ("ASIG", r"="),  # Signo igual
        ("SUMA", r"\+"),  # Suma
        ("REST", r"-"),  # Resta
        ("MUL", r"\*"),  # Multiplicación
        ("DIV", r"/"),  # División
        ("LPAREN", r"\("),  # Paréntesis izquierdo
        ("RPAREN", r"\)"),  # Paréntesis derecho
        ("FIN", r";"),  # Punto y coma
        ("CARACTER_ESPECIAL", r"[?¡'¿-]"),  # Caracteres especiales no permitidos
        ("ERROR", r".")  # Cualquier otro carácter se marca como error
    ]
    
    tokens = []
    errores = []
    
    # Procesar el código línea por línea
    lineas = codigo.splitlines()
    if not lineas:
        lineas = ['']
        
    for num_linea, linea in enumerate(lineas, 1):
        pos = 0
        while pos < len(linea):
            # Intentar coincidir con cada patrón
            encontrado = False
            for tipo, patron_regex in patron:
                match = re.match(patron_regex, linea[pos:])
                if match:
                    valor = match.group()
                    
                    # Si es un carácter especial no permitido
                    if tipo == "CARACTER_ESPECIAL":
                        errores.append({
                            "tipo": "Error léxico",
                            "valor": valor,
                            "linea": num_linea,
                            "posicion": pos,
                            "mensaje": f"Carácter especial no permitido: '{valor}'"
                        })
                        pos += len(valor)  # Avanzar la posición
                        encontrado = True
                        break
                    # Si es un error (otro carácter no permitido)
                    elif tipo == "ERROR":
                        errores.append({
                            "tipo": "Error léxico",
                            "valor": valor,
                            "linea": num_linea,
                            "posicion": pos,
                            "mensaje": f"Carácter no permitido: '{valor}'"
                        })
                        pos += len(valor)  # Avanzar la posición
                        encontrado = True
                        break
                    # Si es un espacio, lo ignoramos
                    elif tipo != "ESPACIO":
                        tokens.append({
                            "tipo": tipo,
                            "valor": valor,
                            "linea": num_linea,
                            "posicion": pos
                        })
                    pos += len(valor)
                    encontrado = True
                    break
            
            if not encontrado:
                pos += 1  # Avanzar un carácter si no se encontró ningún patrón

    return tokens, errores