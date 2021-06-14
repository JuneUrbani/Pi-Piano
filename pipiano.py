import csv
import pygame
import pygame.midi
import sys
import time
import os

class pipiano():
    def __init__(self,in_port,out_port):
        self.midi_map = ['C','C#','D','D#','E','F','F#','G','Ab','A','Bb','B']
        # Set up pygame
        pygame.init()
        pygame.midi.init()
        # Set ports
        self.in_port = in_port
        self.out_port = out_port
        # Open midi devices
        self.input = pygame.midi.Input(self.in_port)
        self.output = pygame.midi.Output(self.out_port)
        
    # Sends the number note and the duration till the next note in milliseconds
    def send_note(note,duration,amount):
        self.output.note_on(note + 36, amount)
        time.sleep(duration/1000.0)
        
    def set_instrument(instrument):
        self.output.set_instrument(instrument)
    
    # Plays midi file from csv
    def play_midi(file):
        note_file = file
        # If the file passed is a midi, convert to csv first
        if '.mid' in file:
            os.system("python midi_convert.py " + file[:-4])
            time.sleep(5)
            note_file = file[:-4] + '.csv'
        # Play through csv file of notes
        with open("music/" + note_file, newline='') as f:
            previous_time = 0
            previous_row = []
            reader = csv.reader(f)
            for row in reader:
                if previous_row == []:
                    previous_row = row
                else:
                    self.send_note(previous_row[1], row[0] - previous_time, previous_row[2])
                    previous_row = row
                    previous_time = row[0]
        
    '''def read_notes():
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
            pygame.time.wait(10)'''
            
p = pipiano(3,2)
p.play_midi("Wellerman.mid")