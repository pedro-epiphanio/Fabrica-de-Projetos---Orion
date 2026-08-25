import qrcode

codigo_maquina = "MAQ001"

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

qr.add_data(codigo_maquina)
qr.make(fit=True)

imagem = qr.make_image(
    fill_color="black",
    back_color="white"
)

imagem.save(f"qrcode_{codigo_maquina}.png")

print(f"QR Code criado para a máquina: {codigo_maquina}")
