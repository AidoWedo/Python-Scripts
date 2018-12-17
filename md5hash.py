# md5 hash generation
import hashlib
#replace 'Bob says hi' with something you want to convert to md5
text = 'Bob says hi'
m = hashlib.md5()
m.update(text.encode('UTF-8'))
print (m.hexdigest())
