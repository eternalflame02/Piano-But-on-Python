import tkinter as tk
import numpy as np
import sounddevice as sd

# Define the frequency of each note
notes_freq = {
    "C4": 261.63,
    "D4": 293.66,
    "E4": 329.63,
    "F4": 349.23,
    "G4": 392.00,
    "A4": 440.00,
    "B4": 493.88,
    "C5": 523.25
}


# Define the GUI window
root = tk.Tk()
root.title("Piano But on Python")

# Define the piano keys
piano_keys = []
for note in notes_freq:
    key = tk.Button(root, text=note, width=5, height=10, bg='black', fg='white', font=("arial", 18, "bold"))
    key.pack(side=tk.LEFT, padx=2, pady=2)
    piano_keys.append(key)


# Define the function that plays a note when a key is pressed
def play_note(note):
    duration = 0.7  # seconds
    volume = 0.3  # between 0 and 1
    samples = np.arange(duration * 44100) / 44100
    waveform = np.sin(2 * np.pi * notes_freq[note] * samples)
    sd.play(volume * waveform, samplerate=44100)


# Bind each key to its corresponding note and function
piano_keys[0].configure(command=lambda: play_note("C4"))
piano_keys[1].configure(command=lambda: play_note("D4"))
piano_keys[2].configure(command=lambda: play_note("E4"))
piano_keys[3].configure(command=lambda: play_note("F4"))
piano_keys[4].configure(command=lambda: play_note("G4"))
piano_keys[5].configure(command=lambda: play_note("A4"))
piano_keys[6].configure(command=lambda: play_note("B4"))
piano_keys[7].configure(command=lambda: play_note("C5"))


root.mainloop()