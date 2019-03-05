#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .exceptions import MelopyGenericError
from .utility import iterate

SCALE_STEPS = {
    "major": [2, 2, 1, 2, 2, 2, 1],
    "melodic_minor": [2, 1, 2, 2, 2, 2, 1],
    "harmonic_minor": [2, 1, 2, 2, 2, 1, 2],
    "chromatic": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    "major_pentatonic": [2, 2, 3, 2],
    "minor_pentatonic": [3, 2, 2, 3]
}


def _get_mode(steps, mode):
    """ Gets the correct mode step list by rotating the list """
    mode = mode - 1
    res = steps[mode:] + steps[:mode]
    return res


def generate_scale(scale, note, mode=1, r_type="list", octaves=True):  # scale, start, type
    """
    Generate a scale
    scale (string): major,  melodic_minor, harmonic_minor, chromatic, major_pentatonic
    note: start note
    """
    if scale in SCALE_STEPS:
        steps = _get_mode(SCALE_STEPS[scale], mode)
        return iterate(note, steps, r_type, octaves)
    else:
        raise MelopyGenericError("Unknown scale type:" + str(scale))

# Licensed under The MIT License (MIT)
# See LICENSE file for more
