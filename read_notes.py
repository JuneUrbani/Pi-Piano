import pygame
import pygame.midi
import sys
import time

# Midi mapping notes
midi_map = ['C','C#','D','D#','E','F','F#','G','Ab','A','Bb','B']

# Set up pygame
pygame.init()
pygame.midi.init()
 
# Open specific midi devices
inp = pygame.midi.Input(3) #need to set this to your working MIDI i/f IDese it was 3
outp = pygame.midi.Output(2)

# run the event loop
while True:
    # Getting Inputs
    if inp.poll():
        # No way to find number of messages in queue so we specify a high max value
	midi_val = inp.read(1000)
        # Determine note
        key_id = (midi_val[0][0][1] - 36)
        note = midi_map[key_id % 12]
        # Determine location on keyboard, assume C7 is center
        note = note + str(key_id / 12 + 4)
        # Alternate: Determine location on keyboard, assume C3 is center
        #note = note + str((midi_val[0][0][1] - 36) / 12)
        print(str(note + " : " + str(midi_val[0][0][2] / 75)) + " [" + str(key_id) + "]")
 
    # Wait short amount of time, 0ms will cause throttling
    pygame.time.wait(10)