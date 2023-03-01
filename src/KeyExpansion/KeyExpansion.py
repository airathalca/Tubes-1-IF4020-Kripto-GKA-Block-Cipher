import sys
from Constants import BYTES_LENGTH


class KeyExpansion:
    def __init__(self, external_key: bytes) -> None:
        self.external_key = external_key

    def get_internal_key(self, index: int) -> bytes:
        # TODO: Definisikan key scheduling untuk mendapatkan internal key
        return index.to_bytes(BYTES_LENGTH, sys.byteorder)