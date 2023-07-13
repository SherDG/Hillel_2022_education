import re

text = 'geeks for geeks. Mytext is awesome 545346346'

# result = re.search(r"\d{9}", text)
# result = re.findall(r"\d{9}", text)

result = re.split(r"\s", text)

# result1 = re.match(r"\d{9}", text)
# print(len(result))
# print(result)

for element in result:
    res = re.match(r'\d{9}', element)
    if res:
        print(f"res: {res}")

# assert re.match(r"545346346", text)




# match = re.search(r'.', text)
# print(match)

# match = re.search(r'for', text)
# print(match)

# using \
match = re.search(r'\.', text)
print(match)