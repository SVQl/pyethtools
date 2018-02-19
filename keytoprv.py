#!/usr/bin/python
# -*- coding: utf-8 -*-
import sha3
from ecdsa import SigningKey,SECP256k1
def private_to_address(key):
    keccak = sha3.keccak_256()
    public = keccak.update(SigningKey.from_string(key.decode('hex'),curve=SECP256k1).get_verifying_key().to_string())
    return "0x{}".format(keccak.hexdigest()[24:])
