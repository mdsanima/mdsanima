MDSANIMA
========

[![Latest version on PyPI](https://img.shields.io/pypi/v/mdsanima.svg)](https://pypi.org/project/mdsanima)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/mdsanima.svg)](#Installation)
[![Downloads](https://pepy.tech/badge/mdsanima)](https://pepy.tech/project/mdsanima)

The package contains modules that will help in calculating rendering time.

The package also includes a module for print your text with an animation counting up or down.

## Instalation
MDSANIMA pacage only works on Python 3

    python -m pip install mdsanima

or

    python3 -m pip install mdsanima

## Usage

    from mdsanima import render_time
    from mdsanima import count_down
    from mdsanima import count_up

    render_time(2400, 21, 1, 30)
    count_down('Your text ', 20, 0.1)
    count_up('Your text ', 500, 0.001)

## License
Mdsanima is released under the terms of the [MIT License](http://www.opensource.org/licenses/MIT).