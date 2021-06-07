import py_midicsv as pm

# Load the MIDI file and parse it into CSV format
csv_string = pm.midi_to_csv("music\Vocalise1.mid")

with open("music\Vocalise1.csv", "w") as f:
    f.writelines(csv_string)

# Parse the CSV output of the previous command back into a MIDI file
midi_object = pm.csv_to_midi(csv_string)

# Save the parsed MIDI file to disk
with open("music\Vocalise1.mid", "wb") as output_file:
    midi_writer = pm.FileWriter(output_file)
    midi_writer.write(midi_object)