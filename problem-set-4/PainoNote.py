NOTES = ("C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B")


def start():
    notes = []

    note_str = input("Notes: ")
    semi_tones = int(input("Semitones: "))

    for note in note_str.split(" "):
        next_note = getNextNote(note, semi_tones)
        notes.append(next_note)

    print(" ".join(notes))


def getNextNote(note, semi_tones):
    index = NOTES.index(note)

    if index < len(NOTES) - 1:
        index += semi_tones

    elif index + semi_tones >= len(NOTES) - 1:
        index = 0
        index += semi_tones - 1

    return NOTES[index]


if __name__ == "__main__":
    start()
