from utils import increase_hex, hex_to_int


class Memory:
    def __init__(self):
        self.data = [hex(0)] * 4096
    
    def load_program(self, program: bytes):
        chip8_program_counter = "0x200"
        for b in program:
            self[chip8_program_counter] = hex(b)
            chip8_program_counter = increase_hex(chip8_program_counter)

    def __getitem__(self, key: str):
        return self.data[hex_to_int(key)]

    def __setitem__(self, key, value):
        self.data[hex_to_int(key)] = value
    
    def __repr__(self):
        return repr(self.data)

class Register:
    def __init__(self):
        self.data[hex(0)] * 16
    
    def __getitem__(self, key: int):
        self.data[key]
    
    def __setitem__(self, key, value):
        self.data[key] = value
