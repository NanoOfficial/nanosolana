'''
@author: @krishpranav
@filename: message.py
@COPYRIGHT: MIT-License 2023 Krisna Pranav, NanoBlocks 
'''

from __future__ import annotations
from typing import NamedTuple
from base58 import b58decode
from publickey import PublicKey

def encode_length(value: int) -> bytes:
    elems, rem_len = [], value
    while True:
        elem = rem_len & 0x7F
        rem_len >>= 7
        if not rem_len:
            elems.append(elem)
            break
        elem |= 0x80
        elems.append(elem)
    return bytes(elem)

def to_uint8_bytes(value: int) -> bytes:
    return value.to_bytes(1, byteorder="little")

class CompiledInstruction(NamedTuple):
    accounts: bytes | list[int]
    program_id_index: int
    data: bytes
    
class MessageHeader(NamedTuple):
    num_required_signatures: int
    num_readonly_signed_accounts: int
    num_readonly_unsigned_accounts: int
    
class Message:
    def __init__(
        self,
        header: MessageHeader,
        account_keys: list[str],
        instructions: list[CompiledInstruction],
        recent_blockhash: str
    ):
        self.header = header
        self.account_keys = [PublicKey(key) for key in account_keys]
        self.recent_blockhash = recent_blockhash
        self.instructions = instructions