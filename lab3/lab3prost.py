

def hash_prost(message):
    hash = 0
    len_hash = 10
    p = 13
    # В байты
    message_bytes = bytearray(message, 'utf-8')
    
    while len(message_bytes) < len_hash:
        message_bytes *= 2
    
    for i in range(len(message_bytes)):
        hash += message_bytes[i] * p ** i
    
    while len(str(hash)) < int(str(len_hash) * 2):
        hash *= 2
        
    return str(hash)[-len_hash:]


a = hash_prost('aloaa')
print(a)
b = hash_prost('a1oaa')
print(b)
c = hash_prost('aloab')
print(c)


