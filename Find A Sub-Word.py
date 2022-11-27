import re

data = []
for i in range(int(input().strip())):
    data.append(input().strip())

for i in range(int(input().strip())):
    query = input().strip()
    matches_count = 0
    for e in data:
        matches = re.findall(r'[A-Za-z_]'+query+r'[A-Za-z_]', e)
        matches_count += len(matches)

    print(matches_count)
