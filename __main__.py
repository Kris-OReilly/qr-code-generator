import qrcode

# asks user for URL input
data = input("Paste in your URL to generate a QR code:")

# Create a QR code object
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction
    box_size=10,  # controls how many pixels each “box” of the QR code is
    border=4,  # controls how many boxes thick the border should be
)

# add the data to the QR code
qr.add_data(data)
qr.make(fit=True)

# create an image from the QR code instance
img = qr.make_image(fill='black', back_color='white')

# save the image to a file
img.save("qrcode.png")

print("QR code generated and saved as qrcode.png")

