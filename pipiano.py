import pygame
import pygame.midi
import sys
import time
import os

class pipiano:
    self.midi_map = ['C','C#','D','D#','E','F','F#','G','Ab','A','Bb','B']
    def pipiano(in_port,out_port):
        # Set up pygame
        pygame.init()
        pygame.midi.init()
        # Set ports
        self.in_port = in_port
        self.out_port = out_port
        # Open midi devices
        self.input = pygame.midi.Input(self.in_port)
        self.output = pygame.midi.Output(self.out_port)
        
    def send_note(note,duration):
        self.output.note_on(note + 36, 127)
        time.sleep(duration)
        self.output.note_off(note + 36, 127)
        
    def set_instrument(instrument):
        self.output.set_instrument(instrument)
        
    def read_notes():
        while True:
            # Getting Inputs
            if self.input.poll():
                # No way to find number of messages in queue so we specify a high max value
            midi_val = self.input.read(1000)
                # Determine note
                key_id = (midi_val[0][0][1] - 36)
                note = self.midi_map[key_id % 12]
                # Determine location on keyboard, assume C7 is center
                note = note + str(key_id / 12 + 4)
                # Alternate: Determine location on keyboard, assume C3 is center
                #note = note + str((midi_val[0][0][1] - 36) / 12)
                print(str(note + " : " + str(midi_val[0][0][2] / 75)) + " [" + str(key_id) + "]")
         
            # Wait short amount of time, 0ms will cause throttling
            pygame.time.wait(10)