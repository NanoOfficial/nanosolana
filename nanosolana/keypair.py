'''
@author: @krishpranav
@filename: keypair.py
@COPYRIGHT: MIT-License 2023 Krisna Pranav, NanoBlocks 
'''

from __future__ import annotations
from publickey import PublicKey
from nacl.signing import SigningKey, SignedMessage
from nacl.public import PrivateKey as NaclPrivateKey
import base58

class PrivateKey(PublicKey):
    LENGTH = 64
    
class Keypair:
    def __init__(self, value: NaclPrivateKey | None = None) -> None:
        if value is None:
            self.key_pair = NaclPrivateKey.generate()
        elif isinstance(value, NaclPrivateKey):
            self.key_pair = value
        else:
            raise ValueError(
                "keypair initiliazation"
            )
            
    @classmethod
    def from_private_key(cls, private_key: str | bytes) -> Keypair:
        private_key = base58.b58decode(private_key)
        seed = private_key[:32]
        return cls(NaclPrivateKey(seed))
    