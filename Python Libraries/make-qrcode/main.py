import qrcode

myqr = qrcode.make("https://debojyotitantra.vercel.app")
myqr.save("main.png")