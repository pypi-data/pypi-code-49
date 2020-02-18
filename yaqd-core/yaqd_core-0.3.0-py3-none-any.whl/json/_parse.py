__all__ = ["gen_objects"]


def gen_objects(data: bytes):
    while data:
        data = data.strip()
        if not data or data[0] not in b"{[":
            # data is invalid json object/array, let calling process handle as it sees fit
            yield data
            return
        square = 1 if data[0:1] == b"[" else 0
        curly = 1 if data[0:1] == b"{" else 0
        i = 1
        while i < len(data) and (square or curly):
            if data[i : i + 1] == b"[":
                square += 1
            elif data[i : i + 1] == b"]":
                square -= 1
            elif data[i : i + 1] == b"{":
                curly += 1
            elif data[i : i + 1] == b"}":
                curly -= 1
            i += 1
        yield data[:i]
        data = data[i:]
