import qrcode


def get_qrcode(url="https://google.com", name="default"):
    qr = qrcode.make(data=url)
    qr.save(stream=f"{name}.png")

    return f"QR-code was created! Open the {name}.png"

url = input("Введите url, для которого нужен QR-код: ")
name = input("Введите название для картинки: ")

get_qrcode(url, name)

int1= input("Картинка с QR-кодом готова и находится в этой же папке, забирайте")