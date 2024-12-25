import qrcode
import qrcode.constants

# create a instant of QRcode class
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=8,
    border=3,
)

# add data in QRCode
qr.add_data("https://debojyotitantra.vercel.app")
qr.make(fit=True)

# create a image of qrcode
img = qr.make_image(fill="black", back_color="yellow")

# save the image
img.save("main2.png")