[![Build Status](https://travis-ci.org/dvc94ch/pycircuit.svg?branch=master)](https://travis-ci.org/dvc94ch/pycircuit)
# Circuit Description Library

## Getting started

`common_emitter.py`
```python
from pycircuit.circuit import *
from pycircuit.library import *


@circuit('Common Emitter', 'gnd', '12V', 'vin', 'vout')
def common_emitter_amplifer(self, gnd, vcc, vin, vout):
    nb, ne = nets('nb ne')
    Inst('Q', 'npn sot23')['B', 'C', 'E'] = nb, vout, ne

    # Current limiting resistor
    Inst('R', '1.2k')['~', '~'] = vcc, vout

    # Thermal stabilization (leads to a gain reduction)
    Inst('R', '220')['~', '~'] = ne, gnd
    # Shorts Re for AC signal (increases gain)
    Inst('C', '10uF')['~', '~'] = ne, gnd

    # Biasing resistors
    Inst('R', '20k')['~', '~'] = vcc, nb
    Inst('R', '3.6k')['~', '~'] = nb, gnd
    # Decoupling capacitor
    Inst('C', '10uF')['~', '~'] = vin, nb


if __name__ == '__main__':
    from pycircuit.formats import *
    from pycircuit.build import Builder

    Builder(common_emitter_amplifer()).compile()
```


![Schematic](https://user-images.githubusercontent.com/741807/34790831-53fb6d02-f643-11e7-895e-2c12e81b69c7.png)

# License
ISC License

Copyright (c) 2017, David Craven

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE
OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.
