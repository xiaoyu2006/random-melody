from midiutil import MIDIFile
from .utils import prompt
from .methods import METHODS, gen_prompt

def entry():
    tempo = prompt('Tempo', 100, lambda i: int(i))

    midi = MIDIFile(1)
    midi.addTempo(0, 0, tempo)
        
    method = prompt(gen_prompt(), 0, lambda i: METHODS[int(i)])
    method(midi)

    with open(
            prompt('Write to file', 'output.midi', 
                   lambda name: name if name.endswith('.midi') else name + '.midi'
            ),
            'wb'
        ) as output_file:
        midi.writeFile(output_file)
