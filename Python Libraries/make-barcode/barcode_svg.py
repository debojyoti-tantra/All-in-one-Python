import barcode

bar = barcode.get_barcode_class("ean13")  # class for making barcodes in the form of svg
Bar = bar("1234567890123")  # give data to the barcode
Bar.save("barcode")  # save and give the name to the barcode