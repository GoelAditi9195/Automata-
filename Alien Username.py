import re

for i in range(int(input().strip())):
    data = input().strip()
    match = re.search(r'^[_.][0-9]+[A-Za-z]*[_]?$', data)
    if match:
        print("VALID")
    else:
        print("INVALID")
