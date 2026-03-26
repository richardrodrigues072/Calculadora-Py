import tkinter

valor_botoes = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

sinais_dir = ["÷", "×", "-", "+", "="]
sinais_topo = ["AC", "+/-", "%"]

colmn_count = len(valor_botoes[0]) #4
row_count = len(valor_botoes) #5

cinza_claro = "#D4D4D2"
cinza_escuro = "#505050"
preto = "#1c1c1c"
laranja = "#ff9500"
branco = "#f0f0f0"

#janela

janela = tkinter.Tk() #cria janela
janela.title("Calculadora Py")
janela.resizable(False, False)

tela = tkinter.Frame(janela)
rotulo = tkinter.Label(tela, text="0", font=("Arial", 45), background=preto,
                        foreground=branco, anchor="e", width=colmn_count)

rotulo.grid(row=0, column=0, columnspan=colmn_count, sticky="we")

for row in range(row_count):
    for column in range(colmn_count):
        value = valor_botoes[row][column]
        botao = tkinter.Button(tela, text=value, font=("Arial", 30),
                                width=colmn_count-1, height=1,
                                command=lambda value=value: botao_clickado(value))
        
        if value in sinais_topo:
            botao.config(foreground=preto, background=cinza_claro)
        elif value in sinais_dir:
            botao.config(foreground=branco, background=laranja)
        else:
            botao.config(foreground=branco, background=cinza_escuro)
        botao.grid(row=row+1, column=column)

tela.pack()

A = "0"
operator = None
B = None

def clear_all():
    global A, B , operator
    A = "0"
    operator = None
    B = None


def remover_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)



def botao_clickado(value):
    global sinais_dir, sinais_topo, rotulo, A, B, operator
    
    if value in sinais_dir:
        if value == "=":
            if A is not None and operator is not None:
                B = rotulo["text"]
                numA = float(A)
                numB = float(B)
                
                if operator == "+":
                    rotulo["text"] = remover_zero_decimal(numA + numB)
                elif operator == "-":
                    rotulo["text"] = remover_zero_decimal(numA - numB)
                elif operator == "×":
                    rotulo["text"] = remover_zero_decimal(numA * numB)
                elif operator == "÷":
                    rotulo["text"] = remover_zero_decimal(numA / numB)
                    
                    clear_all()
        elif value in "+-×÷":
            if operator is None:
                A = rotulo["text"]
                rotulo["text"] = "0"
                B = "0"        
        
            operator = value
    elif value in sinais_topo:
        if value == "AC":
            clear_all()
            rotulo["text"] = "0"
        elif value =="+/-":
            resultado = float(rotulo["text"]) * -1
            rotulo["text"] = remover_zero_decimal(resultado)
        elif value == "%":
            resultado = float(rotulo["text"]) / 100
            rotulo["text"] = remover_zero_decimal(resultado)
    else:
        if value == ".":
            if value not in rotulo["text"]:
                rotulo["text"] += value
        elif value in "0123456789":
            if rotulo["text"] == "0":
                rotulo["text"] = value
            else:
                rotulo["text"] += value


# centralizar janel
janela.update()
janela_width = janela.winfo_width()
janela_height = janela.winfo_height()
screen_width = janela.winfo_screenwidth()
screen_height = janela.winfo_screenheight()

janela_x = int((screen_width/2) - (janela_width/2))
janela_y = int((screen_height/2) - (janela_height/2))

# formato "(w)x(h)+(x)+(y)"
janela.geometry(f"{janela_width}x{janela_height}+{janela_x}+{janela_y}")


janela.mainloop()
