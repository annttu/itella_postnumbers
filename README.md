Itella postnumbers
==================

A simple Python library to fetch and parse Itella's poorly formatted postnumber and postoffice data to python data structure.

Usage
=====

    >>> from itella_postnumbers import postnumbers
    >>> postnumbers.get_mapping()
    [{'id': '090', 'region_swe': 'Södra Savolax', 'short_swe': '', 'name_swe': 
    'Heinävesi', 'short': '', 'region': 'Etelä-Savo', 'type': 'HEINÄVESI',
    'name': 'Heinävesi', 'ponotid': 'PONOT2014112479700HEINÄVESI'}, ... ]

Author
======

* Antti Jaakkola

License
=======

The MIT License (MIT)

Copyright (c) 2014 Antti Jaakkola

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
