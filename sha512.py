from hashlib import sha512

text='U'
hexa_hash=sha512(text.encode()).hexdigest()
print('Hexa hash:' + hexa_hash)

dec_hash=int(hexa_hash,16)
print('Decimal hash:' + str(dec_hash))

print(dec_hash)