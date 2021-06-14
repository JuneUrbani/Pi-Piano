import csv
import py_midicsv as pm
import sys

filename = sys.argv[1]

# Load the MIDI file and parse it into CSV format
csv_string = pm.midi_to_csv("music/" + str(filename) + ".mid")

with open("music/" + str(filename) + ".csv", "w") as f:
    f.writelines(csv_string)

# Parse the CSV output of the previous command back into a MIDI file
midi_object = pm.csv_to_midi(csv_string)

# Save the parsed MIDI file to disk
with open("music/" + str(filename) + ".mid", "wb") as output_file:
    midi_writer = pm.FileWriter(output_file)
    midi_writer.write(midi_object)
    
# Edit down the CSV file to only include info from the piano section with less clutter
track = [['NA','time','NA','NA','note','bool']]
with open("music/" + str(filename) + ".csv", newline='') as f:
    reader = csv.reader(f)
    found_instrument = False
    found_end_track = False
    for row in reader:
        # Check if we can throw out data
        if found_instrument and row[2] == ' Note_on_c':
            #print(row)
            track.append(row)
        try:
            if str(row[3]) == ' "Piano\\000"':
                found_instrument = True
            if str(row[2]) == ' End_track' and found_instrument:
                found_end_track = True
                print(row)
                break
        except:
            pass
for col in track:
    del col[3]
    del col[2]
    del col[0]
print(track)
  
with open("music/" + str(filename) + ".csv", 'w', newline='') as f:
    write = csv.writer(f)
    write.writerows(track)