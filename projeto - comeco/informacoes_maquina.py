import tkinter as tk
from tkinter import filedialog
from maquinas import MAQUINAS
import sys
janela = tk.Tk()

janela.title("Orion - Machinfo")
janela.geometry("1920x1080")

#ATENÇÃO AOS COMENTARIOS!!!!!!!!!!!!!!!!!!!!
#maquina_selecionada = sys.argv[1] #descomentar apos teste

for nome, maquina in MAQUINAS.items():
    if "Hunter H600" == nome: #colocar maquina_selecionada no lugar de "Hunter H600", apos testes
        #print("Deu certo")
        codigo_maquina = tk.Label(
        janela,
        text=f"Código: {maquina["codigo"]}",
        font=("Arial", 17)
        ).place(relx=0.1, rely=0.1, anchor="nw")

        tipo_maquina = tk.Label(
            janela,
            text=f"Tipo: {maquina["tipo"]}",
            font=("Arial", 17)
        ).place(relx=0.1, rely=0.14, anchor="nw")

        marca = tk.Label(
            janela,
            text=f"Marca: {maquina["marca"]}",
            font=("Arial", 17)
        ).place(relx=0.1, rely=0.18, anchor="nw")

        modelo = tk.Label(
            janela,
            text=f"Modelo: {maquina["modelo"]}",
            font=("Arial", 17)
        ).place(relx=0.1, rely=0.22, anchor="nw")

        ano = tk.Label(
            janela,
            text=f"Ano: {maquina["ano"]}",
            font=("Arial", 17)
        ).place(relx=0.1, rely=0.26, anchor="nw")

        horas = tk.Label(
                    janela,
                    text=f"Horas Trabalhadas: {maquina["horas"]}",
                    font=("Arial", 17)
        ).place(relx=0.1, rely=0.3, anchor="nw")

        status = tk.Label(
                janela,
                text=f"Status: {maquina["status"]}",
                font=("Arial", 17)
        ).place(relx=0.1, rely=0.34, anchor="nw")


        garantia = tk.Label(
                janela,
                text=f"Tempo de garantia: {maquina["garantia"]}",
                font=("Arial", 17)
        ).place(relx=0.1, rely=0.38, anchor="nw")

        eficiencia = tk.Label(
                janela,
                text=f"Eficiência: {maquina["eficiencia_declarada"]}",
                font=("Arial",17),
        ).place(relx=0.1, rely=0.42, anchor="nw")

        cod_finame = tk.Label(
                janela,
                text=f"Código Finame: {maquina["codigo_finame"]}",
                font=("Arial",17),
        ).place(relx=0.1, rely=0.46, anchor="nw")

        texto_formatado = "\n".join(maquina["plantadeiras_compativeis"])
        plantadeiras_compativeis = tk.Label(
                janela,
                text=f"Plantadeiras compatíveis: {texto_formatado}",
                font=("Arial",17),
        ).place(relx=0.5, rely=0.1, anchor="nw")






        





        break


























































janela.mainloop()