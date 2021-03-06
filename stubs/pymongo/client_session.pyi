# Stubs for pymongo.client_session (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from bson.binary import Binary
from bson.int64 import Int64
from bson.timestamp import Timestamp
from pymongo.mongo_client import MongoClient
from pymongo.read_concern import ReadConcern
from pymongo.read_preferences import _ServerMode
from pymongo.write_concern import WriteConcern
from typing import Any, Dict, Mapping, Optional

class SessionOptions:
    def __init__(
        self,
        causal_consistency: bool = ...,
        default_transaction_options: Optional[TransactionOptions] = ...) -> None: ...
    @property
    def causal_consistency(self) -> bool: ...
    @property
    def default_transaction_options(self) -> Optional[TransactionOptions]: ...

class TransactionOptions:
    def __init__(
        self,
        read_concern: Optional[ReadConcern] = ...,
        write_concern: Optional[WriteConcern] = ...,
        read_preference: Optional[_ServerMode] = ...) -> None: ...
    @property
    def read_concern(self) -> ReadConcern: ...
    @property
    def write_concern(self) -> WriteConcern: ...
    @property
    def read_preference(self) -> _ServerMode: ...

class _TransactionContext:
    def __init__(self, session: ClientSession) -> None: ...
    def __enter__(self) -> _TransactionContext: ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...

class ClientSession:
    def __init__(self, client: MongoClient, server_session: ServerSession, options: Any, authset: Any, implicit: Any) -> None: ...
    def end_session(self) -> None: ...
    def __enter__(self) -> ClientSession: ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
    @property
    def client(self) -> MongoClient: ...
    @property
    def options(self) -> SessionOptions: ...
    @property
    def session_id(self) -> Dict[str, Binary]: ...
    @property
    def cluster_time(self) -> Mapping[str, Timestamp]: ...
    @property
    def operation_time(self) -> Timestamp: ...
    def start_transaction(
        self,
        read_concern: Optional[ReadConcern] = ...,
        write_concern: Optional[WriteConcern] = ...,
        read_preference: Optional[_ServerMode] = ...) -> _TransactionContext: ...
    def commit_transaction(self) -> None: ...
    def abort_transaction(self) -> None: ...
    def advance_cluster_time(self, cluster_time: Mapping[str, Timestamp]) -> None: ...
    def advance_operation_time(self, operation_time: Timestamp) -> None: ...
    @property
    def has_ended(self) -> bool: ...

class ServerSession:
    def __init__(self) -> None: ...
    def timed_out(self, session_timeout_minutes: int) -> bool: ...
    @property
    def transaction_id(self) -> Int64: ...
    def inc_transaction_id(self) -> None: ...
