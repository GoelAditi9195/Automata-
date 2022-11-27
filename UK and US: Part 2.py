import re

data = " ".join([input().strip() for i in range(int(input().strip()))])

for i in range(int(input().strip())):
    word = input().strip()
    word2 = re.sub("our", "or", word)
    print(len(re.findall(r'\b'+f'({word}|{word2})'+r'\b', data)))
