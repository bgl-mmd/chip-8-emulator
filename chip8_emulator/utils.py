def hex_to_int(key: str):
    try:
        return int(key, 16)
    except ValueError:
        raise ValueError("value must be a valid hexadecimal string")


def increase_hex(value: str):
    try:
        return hex(int(value, 16) + 1)
    except ValueError:
        raise ValueError("value must be a valid hexadecimal string")
