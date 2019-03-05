#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .exceptions import MelopyGenericError
from .utility import iterate

CHORD_INTERVALS = {
    'maj': [4, 3],
    'min': [3, 4],
    'aug': [4, 4],
    'dim': [3, 3],
    '7': [4, 3, 3],
    'maj7': [4, 3, 4],
    'min7': [3, 4, 3],
    'minmaj7': [3, 4, 4],
    'dim7': [3, 3, 3, 3]
}


def _get_inversion(chord, inversion):
    return chord[inversion:] + chord[:inversion]


def generate_chord(name, tonic, inversion=0, r_type='list', octaves=True):
    if name in CHORD_INTERVALS:
        steps = CHORD_INTERVALS[name]
        return _get_inversion(iterate(tonic, steps, r_type, octaves), inversion)
    else:
        raise MelopyGenericError("Unknown Chord:" + str(name))

# Licensed under The MIT License (MIT)
# See LICENSE file for more
