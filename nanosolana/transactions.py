'''
@author: @krishpranav
@filename: transactions.py
@COPYRIGHT: MIT-License 2023 Krisna Pranav, NanoBlocks 
'''

from __future__ import annotations
from dataclasses import dataclass
from base58 import b58decode
from keypair import Keypair
from publickey import PublicKey
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
from core.message import (
    Message,
    MessageHeader,
    CompiledInstruction,
    encode_length
)

PACKET_DATA_SIZE = 1232