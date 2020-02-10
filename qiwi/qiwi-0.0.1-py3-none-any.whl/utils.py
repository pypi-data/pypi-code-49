import time
import json

from typing import Dict, Mapping, Sequence


def resolve_params(params: Dict) -> Dict:
    return {
        k: v if isinstance(v, str) else str(v) for k, v in params.items() if v is not None
    }


def to_json(obj):
    def recursive_to_str(o):
        if isinstance(o, str):
            return o

        if isinstance(o, Mapping):
            new_mapping = o.__class__(
                {k: recursive_to_str(v) for k, v in o.items()}
            )

            return new_mapping

        if isinstance(o, Sequence):
            new_sequence = o.__class__(
                map(recursive_to_str, o)
            )

            return new_sequence

        return str(o)

    return json.dumps(recursive_to_str(obj), separators=(',', ':'), ensure_ascii=True)


def generate_tx_id():
    # You can change this values to yours
    return int(
        (time.time() + 420) * 11110000 + 420
    )
