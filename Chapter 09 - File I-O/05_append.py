s = "What i am writing here will be append in a file\nAnd how many time i run this program this string append at last in the txt file\n\n"

f = open("05_append.txt", "a")

f.write(s)

f.close()