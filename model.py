
import re
from typing import Callable, List, Tuple, Union

PatternResult = Tuple[Union[str, Callable[[str], str]], str]

def validar_cadena(cadena: str) -> str:
    validators: List[PatternResult] = [
        (
            lambda plate: f"Es una placa {'par' if plate.group(2) in '02468' else 'impar'}",
            r"^([A-NP-Z]{3}\d{2,4})([02468]|[13579])$",
        ),
        ("Es una hora normal", r"^(0?[0-9]|1[0-9]|2[0-3]):([0-5][0-9])$"),
        ("Es una hora reiniciada", r"^(0?[0-9]|1[0-1]):([0-5][0-9])[tT]$"),
        ("Es una hora abreviada", r"^(0?[0-9]|1[0-9]|2[0-3])$|^(0?[0-9]|1[0-1])[tT]$"),
    ]

    for validator, pattern in validators:
        match = re.match(pattern, cadena)
        if match:
            if callable(validator):
                return validator(match)
            else:
                return validator
    else:
        return "La cadena no es válida"