#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys; sys.path.append(sys.path[0] + '/../melopy/')

from melopy import *

if __name__ == "__main__":
    song = Melopy('twinkle', 50, wave_type="square")

    song.tempo = 160

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

# Licensed under The MIT License (MIT)
# See LICENSE file for more
