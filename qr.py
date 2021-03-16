import qrcode

# This code will generate a .png file with the QR Code of the website entered

site = input("Enter web address for QR code generation\n")

image = qrcode.make(site)
image.save(f'qr{site}.png', 'png')
