import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("250x300")
janela.configure(bg= "#DDA0DD")

def fechar_janela(): #fecha a janela
    janela.destroy()

def limpa():
    valor.delete(0, tk.END)
    valor2.delete(0, tk.END)
    result.config(text= "Resultado")

def somar():
    num1 = float(valor.get())
    num2 = float(valor2.get())
    total = num1 + num2
    result.config(text= f"Resultado da Soma: {total}")

def sub():
    num1 = float(valor.get())
    num2 = float(valor2.get())
    total = num1 - num2
    result.config(text= f"Resultado da Subtração: {total}")

def mult():
    num1 = float(valor.get())
    num2 = float(valor2.get())
    total = num1 * num2
    result.config(text= f"Resultado da Multiplicação: {total}")

def div():
    num1 = float(valor.get())
    num2 = float(valor2.get())
    total = num1 / num2
    result.config(text= f"Resultado da Divisão: {total}")



juntos = tk.Frame(janela, bg= "#DDA0DD")
juntos.pack(pady=10)

prim_valor = tk.Label(juntos, text= "Primeiro Valor", font = ("Arial", 10), bg= "#DDA0DD")
prim_valor.pack(pady= 10, side= "left")

valor =  tk.Entry(juntos, font= ("Arial, 10"))
valor.pack(pady= 10, side= "left")

juntos2 = tk.Frame(janela, bg= "#DDA0DD")
juntos2.pack(pady=5)

segun_valor = tk.Label(juntos2, text= "Segundo Valor", font= ("Arial", 10), bg= "#DDA0DD")
segun_valor.pack(pady= 10, side= "left")

valor2 = tk.Entry(juntos2, font= ("Arial", 10))
valor2.pack(pady= 10, side= "left")


botoes = tk.Frame(janela, bg= "#DDA0DD")
botoes.pack(pady=5)

mais= tk.Button(botoes, text= " + ", font= ("Arial", 10), bg= "#FFB6C1", command= somar)
mais.pack(pady= 10, side= "left")

menos = tk.Button(botoes, text= " - ", font= ("Arial", 10), bg= "#87CEEB", command= sub)
menos.pack(pady= 10, side= "left")

vezes = tk.Button(botoes, text= " X ", font= ("Arial", 10), bg= "#7FFFD4", command= mult )
vezes.pack(pady= 10, side= "left")

dividido = tk.Button(botoes, text= " % ", font= ("Arial", 10), bg= "#FFE4B5", command= div)
dividido.pack(pady= 10, side= "left")


result = tk.Label(janela, text= "Resultado", font = ("Arial", 10), bg= "#DDA0DD")
result.pack(pady= 10)


butom = tk.Frame(janela, bg= "#DDA0DD")
butom.pack(pady=5)

limpar = tk.Button(butom, text= " Limpar ", font= ("Arial", 10), bg= "#FFE4C4", command= limpa)
limpar.pack(pady= 10, side= "left")

fechar = tk.Button(butom, text= " Fechar ", font= ("Arial", 10), bg= "#FF0000", command= fechar_janela)
fechar.pack(pady= 10, side= "left")




janela.mainloop()