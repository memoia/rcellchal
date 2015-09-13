Problem 2
---------

Requires [virtualenv](https://pypi.python.org/pypi/virtualenv) to be
installed and available on the PATH. Requires standard build
tools (i.e., build-essential or XCode), including gcc.

Installation:

``make``

Summary:

Write a clone of the tail program available in unix/linux systems but
only support a very small subset of the flags/options/features it
supports. Pick and choose the complexity/scope based on the time you
have and the options you like to support. Support at least the basic
functionality you get with no options.

Some thoughts:

Things get more complicated when we involve more than one file stream.
There's a nice cross-platform directory monitoring library called
[watchdog](https://pythonhosted.org/watchdog/). Let's use that so we
don't re-invent the wheel and produce more code that would otherwise
need to be tested.
