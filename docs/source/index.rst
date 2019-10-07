.. segcheck documentation master file, created by
   sphinx-quickstart on Sat Oct  5 10:00:20 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to segcheck's documentation!
====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

segcheck helps to find gaps and overlaps in linear segments.

.. raw:: html

     <svg height="125" width="300">
     <line x1="10"  y1="10" x2="50"  y2="10" style="stroke:rgb(0,0,0); stroke-width:5" />
     <line x1="70"  y1="30" x2="110" y2="30" style="stroke:rgb(0,0,0); stroke-width:5" />
     <line x1="110" y1="50" x2="170" y2="50" style="stroke:rgb(0,0,0); stroke-width:5" />
     <line x1="150" y1="70" x2="210" y2="70" style="stroke:rgb(0,0,0); stroke-width:5" />
     <line x1="10"  y1="0"  x2="10"  y2="80" style="stroke:rgb(0,0,0); stroke-width:1" />
     <line x1="50"  y1="0"  x2="50"  y2="80" style="stroke:rgb(0,0,0); stroke-width:1" />
     <line x1="70"  y1="0"  x2="70"  y2="80" style="stroke:rgb(0,0,0); stroke-width:1" />
     <line x1="110" y1="0"  x2="110" y2="80" style="stroke:rgb(0,0,0); stroke-width:1" />
     <line x1="150" y1="0"  x2="150" y2="80" style="stroke:rgb(0,0,0); stroke-width:1" />
     <line x1="170" y1="0"  x2="170" y2="80" style="stroke:rgb(0,0,0); stroke-width:1" />
     <line x1="210" y1="0"  x2="210" y2="80" style="stroke:rgb(0,0,0); stroke-width:1" />
     <!-- <text x="54"   y="95"  fill="black">&#8593;</text> -->
     <!-- <text x="154"  y="95"  fill="black">&#8593;</text> -->
     <text x="48"   y="115" fill="red">gap</text>
     <text x="136"  y="115" fill="red">overlap</text>
     <polyline points="50,90 50,95 70,95 70,90" style="fill:none;stroke:red;stroke-width:1" />
     <polyline points="150,90 150,95 170,95 170,90" style="fill:none;stroke:red;stroke-width:1" />
     </svg>

In order to determine gaps and overlaps segcheck uses the comparison operators greater than :obj:`< <operator.lt>` and less than :obj:`> <operator.gt>`. Therefore, any python object (e.g. :obj:`float`, :obj:`datetime.datetime` or :obj:`str`) that can be compared using these operators, can be used to define the begin and the end of a segment.

Installation
============

Running ``pip install segcheck`` will install segcheck.

Getting started
===============

.. automodule:: segcheck.core
   :members:

.. automodule:: segcheck.exceptions
   :members:

For developers
==============

Cloning the repository
----------------------

``git clone https://github.com/thomasschus/segcheck``

Building the docs
-----------------

Docs are built using Sphinx. Within the docs directory, run ``make html``.

Running the tests
-----------------

Within the tests directory run ``pytest`` or ``pytest -v`` for more verbose output.

Within the docs directory run ``make doctest``.

License
=======

MIT License

Copyright (c) 2019 Thomas Schuster

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
