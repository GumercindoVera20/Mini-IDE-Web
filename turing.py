def simular_mt(cadena):
    if not set(cadena).issubset({"a", "b"}):
        return "Cadena inválida (caracteres no válidos)", []

    cinta = list(cadena)
    estado = "q0"
    i = 0
    pasos = []

    while True:
        if i >= len(cinta):
            pasos.append((estado, ''.join(cinta), i))
            return "Cadena inválida", pasos

        simbolo = cinta[i]
        pasos.append((estado, ''.join(cinta), i))

        if estado == "q0":
            if simbolo == "a":
                cinta[i] = "X"
                i += 1
                estado = "q1"
            elif simbolo == "Y":
                estado = "qf"
            elif simbolo == "b":
                return "Cadena inválida", pasos
            else:
                return "Cadena inválida", pasos

        elif estado == "q1":
            if simbolo == "a":
                i += 1
            elif simbolo == "b":
                cinta[i] = "Y"
                i -= 1
                estado = "q2"
            elif simbolo == "Y":
                i += 1
            else:
                return "Cadena inválida", pasos

        elif estado == "q2":
            if cinta[i] != "X":
                i -= 1
            else:
                i += 1
                estado = "q0"

        elif estado == "qf":
            # Verificar si quedan b sin marcar
            if any(c in ["a", "b"] for c in cinta):
                return "Cadena inválida", pasos
            else:
                return "Cadena válida", pasos