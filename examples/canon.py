#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.path.append(sys.path[0] + '/../melopy/')

import melopy

if __name__ == "__main__":
    m = melopy.Melopy('canon', 50)
    melody = []

    for start in ['d4', 'a3', 'b3m', 'f#3m', 'g3', 'd3', 'g3', 'a3']:
        if start.endswith('m'):
            scale = melopy.generate_scale("minor", start[:-1])
        else:
            scale = melopy.generate_scale("major", start)

        scale.insert(0, scale[0][:-1] + str(int(scale[0][-1]) - 1))

        [melody.append(note) for note in scale]

    m.add_melody(melody, 0.2)
    m.add_rest(0.4)
    m.add_note('d4', 0.4)
    m.add_rest(0.1)
    m.add_note(['d4', 'a4', 'd5'], 0.8)

    m.render()
    m.play()

# Licensed under The MIT License (MIT)
# See LICENSE file for more
