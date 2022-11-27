import re

def validate(data):
    # (latitude, longitude)
    pattern = r'\(' + r'[\+-]?(90(\.0+)?|[1-8]\d(\.[0-9]+)?|\d(\.[0-9]+)?), [\+-]?(180(\.0+)?|1[0-7]\d(\.[0-9]+)?|[1-9]\d(\.[0-9]+)?|\d(\.[0-9]+)?)' + r'\)'
    return re.search(pattern, data)

for i in range(int(input().strip())):
    if validate(input().strip()):
        print("Valid")
    else:
        print("Invalid")
