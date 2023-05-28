'''
@author: @krishpranav
@filename: types.py
@COPYRIGHT: MIT-License 2023 Krisna Pranav, NanoBlocks 
'''

from __future__ import annotations
import base58

class PublicKey:
    LENGTH = 32
    
    def __init__(self, value: bytearray | bytes | int | str | list[int]):
        if isinstance(value, str):
            try:
                self.byte_value = base58.b58decode(value)
            except ValueError:
                raise ValueError("Invalid public key.")
        elif isinstance(value, int):
            self.byte_value = bytes([value])
        else:
            self.byte_value = bytes(value)
            
        def __repr__(self) -> str:
            return str(self)