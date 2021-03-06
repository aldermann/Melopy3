#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import log

from .exceptions import MelopyGenericError


def key_to_frequency(key):
    """Returns the frequency of the note (key) keys from A0"""
    return 440 * 2 ** ((key - 49) / 12.0)


def key_to_note(key, octaves=True):
    """Returns a string representing a note which is (key) keys from A0"""
    notes = ['a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#']
    octave = (key + 8) // 12
    note = notes[(key - 1) % 12]

    if octaves:
        return note.upper() + str(octave)
    else:
        return note.upper()


def note_to_frequency(note, default=4):
    """Returns the frequency of a note represented by a string"""
    return key_to_frequency(note_to_key(note, default))


def note_to_key(note, default=4):
    """Returns the key number (keys from A0) from a note represented by a string"""
    indices = {
        'C': 0,
        'D': 2,
        'E': 4,
        'F': 5,
        'G': 7,
        'A': 9,
        'B': 11
    }

    octave = default

    if note[-1] in '012345678':
        octave = int(note[-1])

    tone = indices[note[0].upper()]
    key = 12 * octave + tone

    if len(note) > 1 and note[1] == '#':
        key += 1
    elif len(note) > 1 and note[1] == 'b':
        key -= 1

    return key - 8;


def frequency_to_key(frequency):
    return int(12 * log(frequency / 440.0) / log(2) + 49)


def frequency_to_note(frequency):
    return key_to_note(frequency_to_key(frequency))


def b_return(output, t):
    """Returns a selected output assuming input is a list"""
    if isinstance(output, list):
        if t.lower() == "list":
            return output
        elif t.lower() == "tuple":
            return tuple([i for i in output])
        elif t.lower() == "dict":
            o = {}
            for i in range(len(output)):
                o[i] = output[i]
            return o
        elif t.lower() == "string":
            return ''.join(output)
        elif t.lower() == "stringspace":
            return ' '.join(output)
        elif t.lower() == "delemiter":
            return ','.join(output)
        else:
            raise MelopyGenericError("Unknown type: " + t)
    else:
        raise MelopyGenericError("Input to bReturn is not a list! Input: " + str(output))


def iterate(start, pattern, r_type="list", octaves=True):
    """Iterates over a pattern starting at a given note"""
    start_key = note_to_key(start)
    ret = [start_key]

    for step in pattern:
        ret.append(ret[-1] + step)
    for i, item in enumerate(ret):
        ret[i] = key_to_note(ret[i], octaves)
    return b_return(ret, r_type)

# Licensed under The MIT License (MIT)
# See LICENSE file for more
