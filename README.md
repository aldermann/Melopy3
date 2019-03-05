## Melopy

http://jdan.github.io/Melopy

A python library for playing with sound.<br />
*by [Jordan Scales](http://jordanscales.com) and friends*

### Install it

You may need to use `sudo` for this to work.

    $ pip install Melopy3

### Load it

```python3
$ python3
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> import melopy
>>> melopy.generate_scale('major', 'C5')
['C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6']
>>>
```

### Development

To install locally:

    $ git clone git://github.com/aldermann/Melopy
    $ cd Melopy
    $ python3 setup.py install

For examples, check out the `examples` directory:

    $ python3 -m examples.canon

We have to execute the file as a module, or else it won't work in Python 3

To run the tests:

    $ python3 tests/melopy_tests.py

### Organization

Melopy is broken down into 3 subcategories - `melopy`, `scales`, and `utility`.

* `melopy.py` contains the Melopy class
    * this is used for creating a Melopy and adding notes to it, rendering, etc
* `scales.py` contains methods for generating scales
    * for instance, if you want to store the C major scale in an array
* `utility.py` contains methods for finding frequencies of notes, etc

### melopy.py

```python3
>>> from melopy import Melopy
>>> m = Melopy('mysong')
>>> m.add_quarter_note('A4')
>>> m.add_quarter_note('C#5')
>>> m.add_quarter_note('E5')
>>> m.render()
[==================================================] 100%
Done
>>> m.play()
```

### scales.py
The following scales can be generated
* major
* minor (natural minor)
* harmonic_minor
* melodic_minor
* major_pentatonic
* minor_pentatonic
* chromatic

```python3
>>> from melopy.scales import generate_scale
>>> generate_scale('major', 'C4')
['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']

>>> major_scale('C4','dict')
{0: 'C4', 1: 'D4', 2: 'E4', 3: 'F4', 4: 'G4', 5: 'A4', 6: 'B4', 7: 'C5'}

>>> generate_scale("major", "C4", r_type="tuple")
('C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5')
>>> generate_scale("minor", "D#5")
['D#5', 'F5', 'F#5', 'G#5', 'A#5', 'B5', 'C#6', 'D#6']
>>> generate_scale("major_pentatonic", "E4")
['E4', 'F#4', 'G#4', 'B4', 'C#5']
```

### utility.py

* key_to_frequency
* key_to_note
* note_to_frequency
* note_to_key
* frequency_to_key
* frequency_to_note

```python3
>>> from melopy.utility import *
>>> key_to_frequency(49)
440.0
>>> note_to_frequency('A4')
440.0
>>> note_to_frequency('C5')
523.2511306011972
>>> note_to_key('Bb5')
62
>>> key_to_note(65)
'C#6'
>>> key_to_note(304) # even something stupid
'C26'
>>> frequency_to_key(660)
56
>>> frequency_to_note(660)
'E5'
```
