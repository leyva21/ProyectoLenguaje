import re
import tkinter as tk

grammar_rules = [

    # UwU-int Suma , UwU-float x, UwU-var nombre
    # UwU-int y = 5
    # UwU-var nombre = "PepeDralp"
    # UwU-float x = 2.9
    # UwU-print(nombre) , UwU-print("letras")

    (r"^\s*(UwU-)(int|var|float)\s+[a-zA-Z_][a-zA-Z_]*\s*$", "Declaración de variable"),
    (r"^\s*(UwU-)(int)\s+[a-zA-Z]\s+[=]\s+[0-9_]*\s*$", "Declaración de variable 2"),
    (r"^\s*(UwU-)(var)\s+[a-zA-Z_]+\s+=\s*\"?[a-zA-Z_]+\"?\s*$", "Declaración de variable 3"),
    (r"^\s*(UwU-)(float)\s+[a-zA-Z_]+\s+=\s*[\d+\.\d+]+\s*$", "Declaración de variable 4"),
    (r"^\s*(UwU-print)\s+\(\s*\"?[a-zA-Z_]+\"?\s*\)\s*$", "Declaración de variable 5"),

    # UwU-if(x>9): C UwU-else: C
    # UwU-if(x==9): C UwU-else: C
    # UwU-if(nombre=="letras"): C UwU-else: C

    (r"^\s*(UwU-if\s*\(\s*([a-zA-Z_]+|[a-zA-Z_]+==\"[a-zA-Z_]+\")\s*[><=!]{1,2}\s*\d+\s*\):\s*C\s*UwU-else:\s*C\s*)", "Bloque condicional if-else"),
    (r"^\s*UwU-if\s*\(\s*([a-zA-Z_]+|[a-zA-Z_]+==\"[a-zA-Z_]+\")\s*[><=!]{1,2}\s*\d+\s*\):\s*C\s*UwU-else:\s*C\s*", "Bloque condicional if-else"),
    (r"^\s*UwU-if\s*\(\s*([a-zA-Z_]+==\"[a-zA-Z_]+\")\s*\)\s*:", "Declaración de if-else"),

    # UwU-for(x=3 : x >= 3 : x++)
    # UwU-for(int x=3 : x <= 3 : x++)
    # UwU-for(x = y : x >= y : y--)

    (r"^\s*UwU-for\s*\(\s*(\w+)\s*=\s*(\w+)\s*:\s*(\w+)\s*([><]=)\s*(\d+)\s*:\s*(\w+)(\+\+|\-\-)?\s*\)\s*", "Declaración de bucle for"),
    (r"^\s*UwU-for\s*\(\s*int\s+\w+\s*=\s*\d+\s*:\s*\w+\s*<\s*=\s*\d+\s*:\s*\w+\+\+\s*\)\s*$", "Declaración de bucle for"),
    (r"^\s*UwU-for\s*\(\s*\w+\s*=\s*\w+\s*:\s*\w+\s*>=\s*\w+\s*:\s*\w+\-\-\s*\)\s*$", "Declaración de bucle for"),

    # UwU-def nombre()

    (r"^\s*UwU-def\s+\w+\s*\(\s*\)\s*$", "Declaración de función")

]

def validar_declaracion(declaracion):
    stack = []
    for char in declaracion:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return "Error en la declaración. Paréntesis/Corchetes/Llaves no balanceados."
            top = stack.pop()
            if (char == ')' and top != '(') or (char == '}' and top != '{') or (char == ']' and top != '['):
                return "Error en la declaración. Paréntesis/Corchetes/Llaves no coinciden."

    if stack:
        return "Error en la declaración. Paréntesis/Corchetes/Llaves no balanceados."
    
    for pattern, regla in grammar_rules:
        if re.match(pattern, declaracion):
            return regla + " válida."
    return "Error en la declaración."

def validar():
    declaracion = entrada.get()
    resultado = validar_declaracion(declaracion)
    resultado_label.config(text=resultado)


ventana = tk.Tk()
ventana.title("Validador")

etiqueta = tk.Label(ventana, text="Ingrese una declaración (variable, condicional, ciclo o funcion):")
etiqueta.pack()

ancho_ventana = 400
alto_ventana = 400
ventana.geometry(f"{ancho_ventana}x{alto_ventana}")

entrada = tk.Entry(ventana, width=50)
entrada.pack()


resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

boton_validar = tk.Button(ventana, text="Validar", command=validar)
boton_validar.pack()

ventana.mainloop()
