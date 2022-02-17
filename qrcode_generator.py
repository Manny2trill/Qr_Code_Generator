import qrcode

# Generate a QR code
link = "Altiro.Shop"
data = "Altiro.Shop"

# encode the data
img = qrcode.make(data)

# print and savs the image
print = (type(img))
img.save("Altiro.jpg")