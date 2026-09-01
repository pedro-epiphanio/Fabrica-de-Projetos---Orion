import qrcode

texto = "Hunter H600"

qr = qrcode.make(texto)

qr.save("meu_qrcode.png")

print("QR Code criado com sucesso!")
