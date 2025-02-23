import qrcode


def generate_qr_code():
    url = input("Enter the website URL: ")
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.show()
    img.save("qrcode.png")
    print("QR code saved as 'qrcode.png'")


if __name__ == "__main__":
    generate_qr_code()
