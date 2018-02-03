# Title:    passwordBruteForce.py
# Date:     31.01.2018
# Author:   Eskil Uhlving Larsen

import hashlib
import binascii

salt = "Saltet til Ola"
wanted_hash = 'ab29d7b5c589e18b52261ecba1d3a7e7cbf212c6'

# Every letter in the alphabet, both lower and uppercase
letters = 'abcdefghijklmnopqrstuvwxyz' + 'abcdefghijklmnopqrstuvwxyz'.upper()

# Goes through the letters, one by one, and puts three together to 'myPass'
for l1 in letters:
  for l2 in letters:
    for l3 in letters:
      myPass = '' + l1 +l2 +l3

      # Hashes 'myPass' and creates a hex from it
      derived_key = hashlib.pbkdf2_hmac("sha1", myPass.encode(), salt.encode(), 2048)
      myHash = binascii.hexlify(derived_key).decode()

      # Prints 'myPass' and it's hash
      print('{} : {}'.format(myPass, myHash))

      # Checks if the hash is the wanted_hash and stops for input
      if (myHash == wanted_hash):
        print(myPass)
        input()
