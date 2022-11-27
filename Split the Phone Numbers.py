import re

for i in range(int(input().strip())):
    data = input().strip()
    split_str = re.split(r'[\s-]', data)
    print('CountryCode='+split_str[0]+",LocalAreaCode="+split_str[1]+",Number="+split_str[2])
