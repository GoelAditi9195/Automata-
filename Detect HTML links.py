import re
for i in range(int(input().strip())):
    data = input().strip()
    matches = re.findall(r'[^<]*<a href="([^"]+)".*?>(?:[^<]<\w+>)*([^<]*?)(?:<\/\w+>)*<\/a>', data)
    if matches: 
        for m in matches: 
            print("{0},{1}".format(m[0].strip(), m[1].strip()))
