# Simple Hex decode
import base64
#replace xxxxxxxxxxx with something that is base 64
hex_stuff ='xxxxxxxxxxx'
ascii_string = str(base64.b16decode(hex_stuff))[2:-1]
print (ascii_string)

