import logging
import sys

from specs import Memory
from utils import increase_hex


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main(rom):
    memory = Memory()
    with open(rom, "rb") as f:
        rom_data = f.read()
    memory.load_program(rom_data)
    
    
    print(memory["0x1FF"])
    print(memory["0x200"])
    print(memory["0x201"])
    print(memory["0xFFE"])
    print(memory["0xFFF"])



main(sys.argv[1])
