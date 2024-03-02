import winsound
import time

# Define the notes and their frequencies
notes = {
    'C': 261.63,
    'C#': 277.18,
    'D': 293.66,
    'D#': 311.13,
    'E': 329.63,
    'F': 349.23,
    'F#': 369.99,
    'G': 392.00,
    'G#': 415.30,
    'A': 440.00,
    'A#': 466.16,
    'B': 493.88
}

# Define major and minor chords
major_chords = {
    'C': ['C', 'E', 'G'],
    'D': ['D', 'F#', 'A'],
    'G': ['G', 'B', 'D'],
    'A': ['A', 'C#', 'E'],
}

minor_chords = {
    'Cm': ['C', 'D#', 'G'],
    'Dm': ['D', 'F', 'A'],
    'Em': ['E', 'G', 'B'],
    'Am': ['A', 'C', 'E'],
}

# Function to play the chord
def play_chord(chord):
    for note in chord:
        winsound.Beep(int(notes[note]), 500) # Play each note for 500 milliseconds
        time.sleep(0.2) # Add a short delay between notes

# Function to display chord diagram
def display_chord_diagram(chord):
    print("Chord:", chord)
    print("Diagram:")
    # Here you would print a visual representation of the chord, but I'll just print the notes for simplicity
    print("Notes:", ', '.join(chord))
    print("Sound:")
    print("[sound icon]")

# Main function
def main():
    # Let's play and display some chords
    chord_to_play = input("Please enter a Major Chord: ")
    print("Playing and displaying the chord:", chord_to_play)
    display_chord_diagram(major_chords[chord_to_play])
    play_chord(major_chords[chord_to_play])

    chord_to_play = input("Please enter a Minor Chord: ")
    print("\nPlaying and displaying the chord:", chord_to_play)
    display_chord_diagram(minor_chords[chord_to_play])
    play_chord(minor_chords[chord_to_play])

# Run the program
if __name__ == "__main__":
    main()
