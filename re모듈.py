import re

stringData = "My id number is [G203_5A]"

print(re.findall("a",stringData))

print(re.findall("A",stringData))

print(re.findall("i",stringData))

print(re.findall("[a-z]",stringData))

print(re.findall("[a-z]+",stringData))

print(re.findall("[0-9]",stringData))

print(re.findall("[0-9]+",stringData))

print(re.findall("[a-zA-Z0-9]",stringData))

print(re.findall("[a-zA-Z0-9]+",stringData))
#^ 부정
print(re.findall("[^a-zA-Z0-9]",stringData))

# 영문자 및 특수문자 모두 찾기
print(re.findall("[\w]+",stringData))

# 영문자 및 특수문자 아닌 문자 찾기
print(re.findall("[\W]+",stringData))