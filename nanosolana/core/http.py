'''
@author: @krishpranav
@filename: http.py
@COPYRIGHT: MIT-License 2023 Krisna Pranav, NanoBlocks 
- https://github.com/michaelhly/solana-py/blob/master/src/solana/system_program.py
'''

from __future__ import annotations
from .. import __version__
from publickey import PublicKey
from core.types import RPCResponse
from typing import Any
import sys
import asyncio
import base64
import httpx

class HTTPClient:
    def __init__(self, endpoint: str):
        self.endpoint = endpoint
        version = sys.version_info
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": (
                "NanoSolana (https://github.com/NanoOfficial/nanosolana)"
                f"{__version__}) Python{version[0]} {version[1]}"
            ),
        }
        self.request_id = 0
        self.client = httpx.Client()

    def send(self, data: dict[str, Any]) -> RPCResponse:
        res = self.client.post(
            url=self.endpoint, headers=self.headers, json=data
        )
        return res.json()

    def build_data(self, method: str, params: list[Any]) -> dict[str, Any]:
        self.request_id += 1
        params: list[Any] = [
        ]