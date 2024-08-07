str = "egg" "fff"
print(str)

print("Hello\\World")

print("He said, \"Hello\"")

clean = '   spacious   '.strip()
print(clean) # spacious

text = "Hello world"
new_text = text.replace("world", "Python")
print(new_text) 

print('TestHook'.removeprefix('Test')) # Hook
print('TestHook'.removeprefix('Hook')) # TestHook

print('TestHook'.removesuffix('Test'))
print('TestHook'.removesuffix('Hook'))

url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
_, query = url_search.split('?')
print(query)

number = "12345"
print(number.isdigit())  # Виведе: True

text = "Number123"
print(text.isdigit())  # Виведе: False

#Translate
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

str = "This is string example"
print(str.translate(trantab))

price = 19.99
quantity = 3
total = f"Total: {price * quantity:.2f}"
print(total)

completion = 0.756
formatted = f"{completion:.1%}"
print(formatted)  # Виведе: '75.6%'

