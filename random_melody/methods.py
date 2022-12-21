import random
from .utils import prompt

def simple_random(midi):
    time = 0
    duration = .5
    ln = prompt('Lowest note', 60, lambda i: int(i))
    rn = prompt('Highest note', 72, lambda i: int(i))
    n = prompt('Total notes', 8, lambda i: int(i))
    for _ in range(n):
        midi.addNote(0, 0, random.randint(ln, rn), time, duration, 100)
        time += duration


def select_from_notes(midi):
    time = 0
    duration = .5
    notes = prompt(
        'Notes', '60 62 64 65 67 69 71 72', 
        lambda s: tuple(map(int, s.split()))
    )
    n = prompt('Total notes', 8, lambda i: int(i))
    for _ in range(n):
        midi.addNote(0, 0, random.choice(notes), time, duration, 100)
        time += duration

METHODS=(simple_random, select_from_notes)

def gen_prompt():
    result = 'Select a method:\n'
    i = 0
    for m in METHODS:
        result += '{}. {}\n'.format(i, m.__name__)
        i += 1
    return result
