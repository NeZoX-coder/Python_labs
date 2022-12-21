def hash_ne_prost(message):
    hash = 0
    len_hash = 32
    p = 13
    # В байты
    message_bytes = bytearray(message, 'utf-8')
    
    while len(message_bytes) < len_hash:
        message_bytes *= 2
    
    for i in range(len(message_bytes)):
        hash += message_bytes[i] * p ** i

    hash = hex(hash)

    while len(str(hash)) < int(str(len_hash) * 2):
        hash *= 2
    
    return str(hash)[-len_hash:]


a = hash_ne_prost('aloaa')
print(a)
b = hash_ne_prost('a1oaa')
print(b)
c = hash_ne_prost('aloab')
print(c)

