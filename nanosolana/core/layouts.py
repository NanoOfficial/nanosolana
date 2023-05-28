'''
@author: @krishpranav
@filename: layouts.py
@COPYRIGHT: MIT-License 2023 Krisna Pranav, NanoBlocks 
'''

from __future__ import annotations
from enum import IntEnum
from construct import (
    Bytes,
    Int32ul,
    Int64ul,
    PaddedString,
    Padding,
    Pass,
    Switch,
    Struct,
)
from publickey import PublicKey

class InstructionType(IntEnum):
    CREATE_ACCOUNT = 0
    ASSIGN = 1
    TRANSFER = 2
    CREATE_ACCOUNT_WITH_SEED = 3
    WITHDRAW_NONCE_ACCOUNT = 4 
    ASSIGN_WITH_SPEED = 5
    
    
SYSTEM_PROGRAM_ID: PublicKey = PublicKey("11111111111111111111111111111111")

PUBLIC_KEY_LAYOUT: Bytes = Bytes(32)

