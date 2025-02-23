import qrcode

def make_qr(text, filename="myqr.png"):
    """Creates a QR code image."""
    img = qrcode.make(text)
    img.save(filename)
    print(f"QR code saved as {filename}")

data = input("Enter text/URL: ")
make_qr(data)