import re

data = " ".join([input().strip() for i in range(int(input().strip()))])

for i in range(int(input().strip())):
    print(len(re.findall(input()[:-2]+"(ze|se)", data)))
