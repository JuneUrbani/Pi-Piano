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
    def send_note(self,note,duration,amount):
        self.output.note_on(note, amount) # + 36
        time.sleep(duration/1000.0)
        
    def set_instrument(self,instrument):
        self.output.set_instrument(instrument)
    
    # Plays midi file from csv
    def play_midi(self,file):
        note_file = file
        # If the file passed is a midi, convert to csv first
        if file[:-4] == '.mid':
            os.system("python midi_convert.py " + file[:-4])
            time.sleep(5)
            note_file = file[:-4] + '.csv'
        # Play through csv file of notes
        with open("music/" + note_file) as f:
            previous_time = 0
            previous_row = []
            reader = csv.reader(f)
            for row in reader:
                if previous_row == []:
                    previous_row = row
                else:
                    self.send_note(int(previous_row[1]), int(row[0]) - previous_time, int(previous_row[2]))
                    previous_row = row
                    previous_time = int(row[0])
        
    def read_first_notes(self):
        self.notes_played = []
        # Get first 10 notes played, this will likely need to be increased as we gather more songs
        while len(self.notes_played) < 10:
            # Getting Inputs
            if self.input.poll():
                # No way to find number of messages in queue so we specify a high max value
                midi_val = self.input.read(1000)
                # Determine note
                self.notes_played.append(midi_val[0][0][1])
            # Wait short amount of time, 0ms will cause throttling
            pygame.time.wait(10)
        print(self.notes_played)
            
p = pipiano(3,2)
p.read_first_notes()
p.play_midi("Wellerman.csv")