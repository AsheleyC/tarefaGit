#Fazendo com o professor

import tkinter as tk #as = apelido

lista = []

#Criar função para add os itens na lista
def adicionar_item():
    item = entrada.get() #get = pega o nome digitado
    if item:
        lista.append(item)
        entrada.delete(0, tk.END) #limpar campo de entrada
        atualizar_lista()

#Função para atualizar lista
def atualizar_lista():
    texto_lista = "\n ".join(f"{i}-{item}" for i, item in enumerate(lista))if lista else "nenhum item a ser adicionado"
    r2.config(text= texto_lista)

janela = tk.Tk()
janela.configure(bg="#AB82FF")
janela.geometry("500x500") 
janela.title("Lista de Itens") 

rotulo = tk.Label(janela, text="Digite um item: ", font= ("Arial", 25), bg="#AB82FF" ) 
rotulo.pack(pady=10, anchor= "w", padx=10 )

entrada = tk.Entry(janela, width=50, font=("Times New Roman Bold", 12), relief= "solid") #whidth = largura.
entrada.pack(pady=5, anchor="w", padx= 20)

btn_add = tk.Button(janela, text = "Adicionar", font=("Times New Roman Bold", 10), relief= "solid", command= adicionar_item)
btn_add.pack(pady=10, anchor="e", padx = 20) # anchor =  direção "norte, sul..."

r2 = tk.Label(janela, text= "", font = ("Times New Roman Bold", 10), width=55, height=20, justify="left", relief= "solid") #height = altura
r2.pack(pady=10, anchor="nw", padx = 10) #justify = alinha como no word; relief = coloca borda


janela.mainloop()
