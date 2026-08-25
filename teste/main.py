import tkinter as tk
from tkinter import messagebox, filedialog
import cv2

from banco_maquinas import MAQUINAS


# ============================================================
# MOSTRAR INFORMAÇÕES DA MÁQUINA
# ============================================================

def mostrar_maquina(codigo):

    codigo = codigo.strip().upper()

    maquina = MAQUINAS.get(codigo)

    if maquina is None:

        messagebox.showerror(
            "Máquina não encontrada",
            f"O código '{codigo}' não está cadastrado."
        )

        return

    janela = tk.Toplevel()
    janela.title("Informações da Máquina")
    janela.geometry("600x600")
    janela.resizable(False, False)

    # --------------------------------------------------------
    # TÍTULO
    # --------------------------------------------------------

    titulo = tk.Label(
        janela,
        text="INFORMAÇÕES DA MÁQUINA",
        font=("Arial", 20, "bold")
    )

    titulo.pack(pady=20)

    # --------------------------------------------------------
    # CÓDIGO
    # --------------------------------------------------------

    codigo_label = tk.Label(
        janela,
        text=f"Máquina: {maquina['codigo']}",
        font=("Arial", 16, "bold"),
        fg="#1b5e20"
    )

    codigo_label.pack(pady=5)

    # --------------------------------------------------------
    # INFORMAÇÕES
    # --------------------------------------------------------

    frame = tk.Frame(janela)

    frame.pack(
        padx=40,
        pady=20,
        fill="both",
        expand=True
    )

    informacoes = [

        ("Tipo", maquina["tipo"]),
        ("Marca", maquina["marca"]),
        ("Modelo", maquina["modelo"]),
        ("Ano", maquina["ano"]),
        ("Horas de operação", maquina["horas"]),
        ("Proprietário", maquina["proprietario"]),
        ("Localização", maquina["localizacao"]),
        ("Status", maquina["status"])

    ]

    for nome, valor in informacoes:

        linha = tk.Frame(frame)

        linha.pack(
            fill="x",
            pady=7
        )

        label_nome = tk.Label(
            linha,
            text=f"{nome}:",
            font=("Arial", 12, "bold"),
            width=20,
            anchor="w"
        )

        label_nome.pack(
            side="left"
        )

        label_valor = tk.Label(
            linha,
            text=str(valor),
            font=("Arial", 12),
            anchor="w"
        )

        label_valor.pack(
            side="left"
        )

    # --------------------------------------------------------
    # BOTÃO FECHAR
    # --------------------------------------------------------

    botao_fechar = tk.Button(
        janela,
        text="Fechar",
        font=("Arial", 12, "bold"),
        width=15,
        command=janela.destroy
    )

    botao_fechar.pack(pady=20)


# ============================================================
# LER QR CODE DE UMA IMAGEM
# ============================================================

def selecionar_arquivo():

    arquivo = filedialog.askopenfilename(

        title="Selecione a imagem do QR Code",

        filetypes=[
            ("Imagens", "*.png *.jpg *.jpeg *.bmp"),
            ("Todos os arquivos", "*.*")
        ]
    )

    # Usuário cancelou
    if not arquivo:
        return

    imagem = cv2.imread(arquivo)

    if imagem is None:

        messagebox.showerror(
            "Erro",
            "Não foi possível abrir o arquivo."
        )

        return

    detector = cv2.QRCodeDetector()

    codigo, pontos, _ = detector.detectAndDecode(imagem)

    if codigo:

        codigo = codigo.strip()

        mostrar_maquina(codigo)

    else:

        messagebox.showerror(
            "QR Code não encontrado",
            "Não foi possível encontrar um QR Code nessa imagem."
        )


# ============================================================
# ESCANEAR QR CODE PELA CÂMERA
# ============================================================

def escanear_qrcode():

    camera = cv2.VideoCapture(0)

    if not camera.isOpened():

        messagebox.showerror(
            "Erro",
            "Não foi possível acessar a câmera."
        )

        return

    detector = cv2.QRCodeDetector()

    codigo_encontrado = None

    while True:

        sucesso, imagem = camera.read()

        if not sucesso:
            break

        codigo, pontos, _ = detector.detectAndDecode(imagem)

        # Desenha o quadrado em volta do QR Code
        if pontos is not None:

            pontos = pontos.astype(int)

            for i in range(len(pontos[0])):

                ponto1 = tuple(pontos[0][i])

                ponto2 = tuple(
                    pontos[0][(i + 1) % len(pontos[0])]
                )

                cv2.line(
                    imagem,
                    ponto1,
                    ponto2,
                    (0, 255, 0),
                    3
                )

        cv2.putText(
            imagem,
            "Aponte para o QR Code",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.putText(
            imagem,
            "ESC = sair",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        cv2.imshow(
            "Scanner de QR Code",
            imagem
        )

        # Encontrou QR Code
        if codigo:

            codigo_encontrado = codigo.strip()

            break

        tecla = cv2.waitKey(1)

        # ESC
        if tecla == 27:
            break

    camera.release()

    cv2.destroyAllWindows()

    if codigo_encontrado:

        mostrar_maquina(codigo_encontrado)


# ============================================================
# JANELA PRINCIPAL
# ============================================================

def iniciar_programa():

    janela = tk.Tk()

    janela.title(
        "Sistema de Máquinas Agrícolas"
    )

    janela.geometry(
        "600x500"
    )

    janela.resizable(
        False,
        False
    )

    # --------------------------------------------------------
    # TÍTULO
    # --------------------------------------------------------

    titulo = tk.Label(
        janela,
        text="SISTEMA DE MÁQUINAS AGRÍCOLAS",
        font=("Arial", 21, "bold"),
        fg="#1b5e20"
    )

    titulo.pack(
        pady=(50, 15)
    )

    # --------------------------------------------------------
    # DESCRIÇÃO
    # --------------------------------------------------------

    descricao = tk.Label(
        janela,
        text=(
            "Selecione uma das opções abaixo\n"
            "para identificar a máquina."
        ),
        font=("Arial", 13)
    )

    descricao.pack(
        pady=10
    )

    # --------------------------------------------------------
    # BOTÃO CÂMERA
    # --------------------------------------------------------

    botao_camera = tk.Button(

        janela,

        text="📷  ESCANEAR PELA CÂMERA",

        font=("Arial", 14, "bold"),

        width=30,

        height=2,

        bg="#2e7d32",

        fg="white",

        activebackground="#1b5e20",

        activeforeground="white",

        command=escanear_qrcode
    )

    botao_camera.pack(
        pady=(30, 10)
    )

    # --------------------------------------------------------
    # BOTÃO ARQUIVO
    # --------------------------------------------------------

    botao_arquivo = tk.Button(

        janela,

        text="📁  SELECIONAR ARQUIVO",

        font=("Arial", 14, "bold"),

        width=30,

        height=2,

        bg="#1565c0",

        fg="white",

        activebackground="#0d47a1",

        activeforeground="white",

        command=selecionar_arquivo
    )

    botao_arquivo.pack(
        pady=10
    )

    # --------------------------------------------------------
    # BOTÃO SAIR
    # --------------------------------------------------------

    botao_sair = tk.Button(

        janela,

        text="Sair",

        font=("Arial", 11),

        width=12,

        command=janela.destroy
    )

    botao_sair.pack(
        pady=30
    )

    # --------------------------------------------------------
    # INICIA PROGRAMA
    # --------------------------------------------------------

    janela.mainloop()


# ============================================================
# EXECUÇÃO
# ============================================================

if __name__ == "__main__":

    iniciar_programa()
