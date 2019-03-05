from melopy.melopy import Melopy

song = Melopy("song", wave_type="piano")

part1notes = ['C', 'G', 'A', 'G', 'F', 'E', 'D', 'C']
part2notes = ['G', 'F', 'E', 'D']


def twinkle(notes):
    for i in range(len(notes)):
        song.add_quarter_note(notes[i])
        if i % 4 == 3:
            song.add_quarter_rest()
        else:
            song.add_quarter_note(notes[i])


twinkle(part1notes)
twinkle(part2notes)
twinkle(part2notes)
twinkle(part1notes)
song.render()
song.play()
