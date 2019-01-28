import hashlib

obj = hashlib.md5(b"555555555555")    #加盐
obj.update("alex".encode("utf-8"))  # 加密的必须是字节
miwen = obj.hexdigest() #6a89b5b541444af45a7927d42f43757d
print(miwen)