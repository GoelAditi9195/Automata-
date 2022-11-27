import re

for i in range(int(input().strip())):
    data = str(input().split())
    match = re.search(r'[A-Z]{5}[0-9]{4}[A-Z]', data)
    if match:
        print("YES")
    else:
        print("NO")
