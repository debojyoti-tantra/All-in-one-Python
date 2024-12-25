import barcode
from barcode.writer import ImageWriter

bar = barcode.get_barcode_class("code39")  # class for making barcodes in the form of png
Bar = bar("1234567890123", writer=ImageWriter())  # give data to the barcode
Bar.save("barcode")  # save and give the name to the barcode