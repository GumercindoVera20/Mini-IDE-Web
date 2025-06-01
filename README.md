# Mini IDE Web - Analizador Léxico y Sintáctico 🚀

## Datos del Estudiante y Materia 📚
- **Estudiante:** Gumercindo Vera Santiago
- **Materia:** Lenguajes y Autómatas I
- **Profesor:** Kevin David Molina Gomez
- **Universidad:** Instituto Tecnológico de Minatitlán
- **Semestre:** 6

## Instrucciones para Ejecutar el Proyecto ⚡

### Requisitos Previos 📋
- Python 3.x instalado
- Flask (framework web)

### Pasos para Ejecutar 🔧
1. Instalar las dependencias:
   ```bash
   pip install flask
   ```

2. Ejecutar el servidor Flask:
   ```bash
   python app.py
   ```

3. Abrir el navegador web y acceder a:
   ```
   http://localhost:5000
   ```

## Estructura del Proyecto 📁
```
Mini IDE Web/
├── app.py           # Servidor Flask
├── lexer.py         # Analizador léxico
├── parser.py        # Analizador sintáctico
├── static/          # Archivos estáticos (CSS, JS)
├── templates/       # Plantillas HTML
└── README.md        # Documentación
```

## Características del IDE Web 💻
- ⚡ Análisis en tiempo real
- 🔍 Resaltado de errores
- 🎨 Interfaz web intuitiva
- 🎯 Detección de múltiples errores por línea
- 📝 Mensajes de error descriptivos

## Explicación del Lenguaje Personalizado 🔤

### Tokens 🎯
El lenguaje reconoce los siguientes tokens:

| Token | Descripción | Ejemplo |
|-------|-------------|---------|
| ID | Identificadores (inician con letra, seguidos de letras o números) | variable, x1, contador |
| NUM | Números enteros | 123, 45, 0 |
| ASIG | Operador de asignación | = |
| FIN | Fin de instrucción | ; |
| SUMA | Operador de suma | + |
| REST | Operador de resta | - |
| MUL | Operador de multiplicación | * |
| DIV | Operador de división | / |
| LPAREN | Paréntesis izquierdo | ( |
| RPAREN | Paréntesis derecho | ) |

### Gramática 📖
El lenguaje sigue una gramática simple de asignación:
```
instruccion → ID = expresion;
expresion → NUM | ID
```

### Manejo de Errores ⚠️

#### Errores Léxicos ❌
- Caracteres especiales no permitidos (?, ¡, ', ¿, -)
- Caracteres no reconocidos
- Símbolos inválidos

#### Errores Sintácticos 🚫
- Falta de identificador al inicio
- Falta del operador de asignación (=)
- Falta de valor después del signo =
- Falta del punto y coma al final (;)
- Caracteres después del punto y coma
- Estructura incorrecta de la instrucción

## Ejemplos 📝

### Entradas Válidas ✅
```
x = 5;
contador = 42;
resultado = variable;
```

### Entradas Inválidas ❌
```
# Error: Carácter después del punto y coma
x = 5; 2

# Error: Falta el punto y coma
y = 10

# Error: Falta el operador de asignación
z 20;

# Error: Identificador inválido
123x = 5;

# Error: Caracteres especiales no permitidos
valor? = 30;

# Error: Falta valor después del =
contador = ;
```

### Ejemplos Visuales 📸

#### Ejemplo 1: Análisis Léxico
![Ejemplo de Análisis Léxico](<Captura de pantalla 2025-06-01 111412.png>)
*Ejemplo de análisis mostrando entradas válidas e inválidas del analizador léxico*

#### Ejemplo 2: Análisis Sintáctico
![Ejemplo de Análisis Sintáctico](<Captura de pantalla 2025-06-01 111455.png>)
*Ejemplo de análisis mostrando entradas válidas e inválidas del analizador Sintáctico*

#### Ejemplo 3: Máquina de Turing
![Ejemplo de Máquina de Turing](<Captura de pantalla 2025-06-01 111514.png>)
![Ejemplo de Máquina de Turing](<Captura de pantalla 2025-06-01 111529-1.png>)
*Ejemplo de una cadena válida e inválida en la máquina de Turing (aabbb)*

## Máquina de Turing 🤖
La máquina de Turing incluida en este proyecto es un simulador que verifica si una cadena tiene el mismo número de letras 'a' seguidas del mismo número de letras 'b'.

### ¿Qué hace? 🤔
Por ejemplo, si ingresas "aabb":
1. 🔍 Primero revisa que solo haya letras 'a' y 'b'
2. 🔢 Luego cuenta que el número de 'a's sea igual al número de 'b's
3. 📋 También verifica que todas las 'a's estén antes que las 'b's
4. ✨ Si todo es correcto, acepta la cadena

### Ejemplos Simples 📋

✅ Cadenas que acepta:
```
ab      (1 'a' y 1 'b')
aabb    (2 'a's y 2 'b's)
aaabbb  (3 'a's y 3 'b's)
```

❌ Cadenas que no acepta:
```
ba      (está al revés: primero debe ir 'a' y luego 'b')
aab     (tiene dos 'a's pero solo una 'b')
abab    (las 'a's y 'b's están mezcladas)
abc     (no se permite la letra 'c')
```

### ¿Cómo funciona? ⚙️
La máquina lee la cadena de izquierda a derecha y:
1. 📝 Va marcando cada 'a' que lee
2. 🔢 Cuenta las 'b's y las marca
3. ✅ Al final revisa que haya marcado el mismo número de cada una

## Autor 👨‍💻
Gumercindo Vera Santiago
