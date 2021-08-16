# String Methods

text = "hello, my name is mansi"
x = text.capitalize()
print(x)

text = "Hello, My Name Is Mansi"
x = text.casefold()
print(x)

text = "Pretty"
x = text.center(7)
print(x)

text = "I love to listen music, musical songs are therapeutic"
x = text.count("music")

text = "My name is Mansi"
x = text.encode()

text = "I love music."
x = text.endswith(".")

text = "M\ta\tn\ta\ts\ti"
x = text.expandtabs(4)

text = "My name is Manasi"
x = text.find("Manasi")

text = "For only {price:.2f} rupees!"
print(text.format(price = 77))

text = "Hello, my name is Riya."
x = text.index("my")
print(x)

text = "Company12"
x = text.isalnum()
print(x)

text = "CompanyX"
x = text.isalpha()
print(x)

text = "Company123"
x = text.isascii()
print(x)

txt = "\u0033"
x = txt.isdecimal()
print(x)

text = "172247"
x = text.isdigit()
print(x)

text = "Demo"
x = text.isidentifier()
print(x)

text = "hello world!"
x = text.islower()
print(x)

text = "565543"
x = text.isnumeric()
print(x)

text = "Hello! Are you #1?"
x = text.isprintable()
print(x)

text = "   "
x = text.isspace()
print(x)

text = "Hello, And Welcome To My World!"
x = text.istitle()
print(x)

text = "THIS IS NOW!"
x = text.isupper()
print(x)

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

text = "banana"
x = text.ljust(20)
print(x, "is my favorite fruit.")

txt = "Hello my FRIENDS"
x = txt.lower()
print(x)

txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))

text = "I could eat bananas all day"
x = text.partition("bananas")
print(x)

text = "I like bananas"
x = text.replace("bananas", "apples")
print(x)

text = "Mi casa, su casa."
x = text.rfind("casa")
print(x)

text = "Mi casa, su casa."
x = text.rindex("casa")
print(x)

text = "banana"
x = text.rjust(20)
print(x, "is my favorite fruit.")

text = "I could eat bananas all day, bananas are my favorite fruit"
x = text.rpartition("bananas")
print(x)

text = "apple, banana, cherry"
x = text.rsplit(", ")
print(x)

text = "     banana     "
x = text.rstrip()
print("of all fruits", x, "is my favorite")

text = "welcome to the jungle"
x = text.split()
print(x)

text = "Thank you for the music\nWelcome to the jungle"
x = text.splitlines()
print(x)

text = "Hello, welcome to my world."
x = text.startswith("Hello")
print(x)

text = "     banana     "
x = text.strip()
print("of all fruits", x, "is my favorite")

text = "Hello My Name Is PETER"
x = text.swapcase()
print(x)

text = "Welcome to my world"
x = text.title()
print(x)

# Use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
text = "Hello Sam!"
print(text.translate(mydict))

text = "Hello my friends"
x = text.upper()
print(x)

text = "50"
x = text.zfill(10)
print(x)




























