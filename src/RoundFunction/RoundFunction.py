from typing import Callable


class RoundFunction:
    def __init__(self) -> None:
        # TODO: Definisikan inner state untuk round function jika dibutuhkan
        pass

    def hash_function(self, key: bytes, content: bytes) -> bytes:
        # TODO: Definisikan hash function yang invertible
        return content

    def get_hash(self, key: bytes) -> Callable[[bytes], bytes]:
        return lambda content: self.hash_function(key, content)