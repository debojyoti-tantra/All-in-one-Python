from pyzbar.pyzbar import decode
from PIL import Image

decoded = decode(Image.open("main.png"))
print(decoded[0].data.decode("ascii"))