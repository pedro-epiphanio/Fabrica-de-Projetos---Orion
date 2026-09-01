import tkinter as tk
import cv2
from tkinter import filedialog
import maquinas

janela = tk.Tk()

janela.title("Orion - Machinfo")
janela.geometry("1920x1080")


boas_vindas = tk.Label(
    janela,
    text="Bem-vindo!",
    font=("Arial", 30)
).place(relx=0.5, rely=0.3, anchor="center")


o_que_fazer = tk.Label(
    janela,
    text="Selecione o arquivo com o QrCode da máquina desejada!",
    font=("Arial", 20)
).place(relx=0.5, rely=0.4, anchor="center")


def clicar():
    arquivo = filedialog.askopenfilename(
        filetypes=[
            ("Imagens", "*.png *.jpg *.jpeg *.bmp"),
            ("Todos os arquivos", "*.*")
        ]
    )

    if not arquivo:
        return

    imagem = cv2.imread(arquivo)

    if imagem is None:
        print("Erro: não foi possível abrir a imagem.")
        return

    detector = cv2.QRCodeDetector()

    texto, pontos, _ = detector.detectAndDecode(imagem)

    if texto == "Hunter H600":

        print("QR Code encontrado:")
        print(texto)

        print("Código:", maquinas.MAQUINAS["Hunter H600"]["codigo"])
        print("Tipo:", maquinas.MAQUINAS["Hunter H600"]["tipo"])

    else:
        print("QR Code não encontrado.")


botao = tk.Button(
    janela,
    text="Selecionar arquivo",
    command=clicar,
    font=("Arial", 17)
).place(
    relx=0.5,
    rely=0.55,
    anchor="center",
    width=300,
    height=100
)


janela.mainloop()
