chords_list = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

input_chords = input('Input chords: ')
input_step = int(input('Input step: '))

user_chords = [word for word in input_chords.split()]
print(user_chords)

new = ''
for chord in user_chords:
    if chord in chords_list:
        index = chords_list.index(chord)
        if index + input_step >= len(chords_list):
            x = (index + input_step) - len(chords_list)
            new += chords_list[x]

        else:
            new += chords_list[index+input_step]

print(new)
