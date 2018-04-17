The calculations module
#######################

Introduction
------------

I wrote this function to be able to both perform calculations in Python *and*
print the results. Existing tools do not easily let you do that.
Spreadsheets display results but not the formula. And interactive shells like
IPython let me do calculations but if I assign the result to a variable I have
to perform an extra action to show it.

I already wrote a tool like this to generate LaTeX output called texcalc_.
Since that has to produce LaTeX it need to walk the parse tree. This tool is
much simpler.

.. _texcalc: https://github.com/rsmith-nl/texcalc

How it works
------------

The ``do`` function in the ``calculations`` module takes three arguments;

* an expression to be evaluated,
* a comment to be printed after the result and
* a ``dict`` of local variables. The latter is best left at the default.

Using the function is simple.

.. code-block:: python

    from calculations import do

    do('L = 1.2', 'm')
    do('B = 0.5', 'm')
    do('B = 0.23', 'm')
    do('volume = L * B * H', 'm³')

Running this code produces::

    L = 1.2 m
    B = 0.5 m
    H = 0.23 m
    volume = L * B * H = 0.138 m³


Disclaimer
----------

This is just a module for doing relatively simple calculations plus
assignments. Handling data structures like lists and dictionaries is beyond
its scope. Also, it is not equipped to handle e.g. ``numpy`` arrays.
