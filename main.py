def hash_md5_func(text):
    import hashlib
    textUtf8 = text.encode("utf-8")
    hash_object = hashlib.md5(textUtf8)
    hash_text = hash_object.hexdigest()

    return hash_text


def hash_sha1_func(text):
    import hashlib
    textUtf8 = text.encode("utf-8")
    hash_object = hashlib.sha1(textUtf8)
    hash_text = hash_object.hexdigest()

    return hash_text


import hashlib


def ripemd160(data):
    return hashlib.new("ripemd160", data)


print(hash("qwertyu"))

import zlib

s = b'Xewirovanie'
# using zlib.crc32() method
t = zlib.crc32(s)

print(t)
