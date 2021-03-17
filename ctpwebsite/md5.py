import hashlib

print(hashlib.md5('true'.encode(encoding='UTF-8')).hexdigest())