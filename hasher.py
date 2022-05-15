#!/usr/bin/env python3
import hashlib

input_hash = input("Enter your hash string :  ")

hash_md5 = hashlib.md5()           #key of hashing
hash_md5.update(input_hash.encode())       #merging the key with the text
print("Hash md5     :  " + hash_md5.hexdigest())            ##print as hexdigest

hash_sh1 = hashlib.sha1()
hash_sh1.update(input_hash.encode())
print("Hash sha1    :  " +hash_sh1.hexdigest())

hash_sh224 = hashlib.sha224()
hash_sh224.update(input_hash.encode())
print("Hash sha224  :  " +hash_sh224.hexdigest())


hash_sh256 = hashlib.sha256()
hash_sh256.update(input_hash.encode())
print("Hash sha256  :  " +hash_sh256.hexdigest())

hash_sh384 = hashlib.sha384()
hash_sh384.update(input_hash.encode())
print("Hash sha384  :  " +hash_sh384.hexdigest())

hash_sh22 = hashlib.sha512()
hash_sh22.update(input_hash.encode())
print("Hash sha512  :  " + hash_sh22.hexdigest())




