import re
tags = set()
for i in range(int(input().strip())):
    data = input().strip()
    matches = re.findall(r'<\/?([a-z0-9]+).*?>', data)
    if matches:
        for m in matches:
            tags.add(m.strip())
tag_list = list(tags)
tag_list.sort()
for i in range(len(tag_list)-1):
    print(tag_list[i] + ';', end="")
print(tag_list[i+1])
