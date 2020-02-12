from typing import Tuple, Any, Dict

# The type of a standard *args parameter
POSITIONAL_ARGS_TYPE = Tuple[Any, ...]

# The type of a standard **kwargs parameter
KEYWORD_ARGS_TYPE = Dict[str, Any]

# The type of *args, **kwargs combined
VAR_ARGS_TYPE = Tuple[POSITIONAL_ARGS_TYPE, KEYWORD_ARGS_TYPE]
