'''
@author: @krishpranav
@filename: types.py
@COPYRIGHT: MIT-License 2023 Krisna Pranav, NanoBlocks 
'''


from typing import TypedDict, Literal, Any

class RPCError(TypedDict):
    status_code: int
    message: str
    
class RPCResponse(TypedDict):
    jsonrpc: Literal["2.0"]
    id: int
    result: Any
    error: RPCError

