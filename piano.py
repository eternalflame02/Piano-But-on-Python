
import tkinter as tk
from music21 import note, stream

# Create a tkinter window
window = tk.Tk()
window.title("Piano App")

# Create a stream to store the notes
s = stream.Stream()

# Define a function to play a note
def play_note(note_name):
    n = note.Note(note_name)
    s.append(n)
    s.show('midi')

# Create a frame for the white keys
white_key_frame = tk.Frame(window, bg='white')
white_key_frame.pack(side=tk.TOP)

# Create a frame for the black keys
black_key_frame = tk.Frame(window, bg='black')  
black_key_frame.pack(side=tk.TOP)

# Create a frame for the white keys
white_key_frame = tk.Frame(window, bg='white')
white_key_frame.pack(side=tk.TOP)

# Create a frame for the black keys
black_key_frame = tk.Frame(window, bg='black')
black_key_frame.pack(side=tk.TOP)

# Create tiles for each note
for octave in range(4, 7):
    for note_name in ['C', 'D', 'E', 'F', 'G', 'A', 'B']:
        note_full_name = note_name + str(octave)
        if note_name in ['C', 'D', 'E', 'F', 'G', 'A', 'B']:
            if note_name in ['C', 'F']:
                button = tk.Button(black_key_frame, text=note_full_name, command=lambda n=note_full_name: play_note(n), relief="solid", bd=2, bg='black', fg='white', width=5, height=3)
                button.pack(side=tk.LEFT)
            else:
                button = tk.Button(black_key_frame, text=note_full_name, command=lambda n=note_full_name: play_note(n), relief="solid", bd=2, bg='black', fg='white', width=5, height=3)
                button.pack(side=tk.LEFT, padx=(5, 0))
        else:
            button = tk.Button(white_key_frame, text=note_full_name, command=lambda n=note_full_name: play_note(n), relief="solid", bd=2, width=10, height=3)
            button.pack(side=tk.LEFT)
# Start the tkinter mainloop
window.mainloop()
