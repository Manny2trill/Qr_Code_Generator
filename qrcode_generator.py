import qrcode

# Generate a QR code
link = ""
data = ""

# encode the data
img = qrcode.make(data)

# print and savs the image
print = (type(img))
img.save("QrcodeGitHub1.jpg")