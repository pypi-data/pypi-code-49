from .args_integration import OptionProcedure, Option


class SecretKeyProcedure(OptionProcedure):
    known_count = (True, 1)


std_options = [
    Option("secret-key", "", SecretKeyProcedure)
]
