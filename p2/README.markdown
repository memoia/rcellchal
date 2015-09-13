Problem 2
---------

You can create a symlink to the application with ``make``, but this is
kind of silly. Executing ``./tail.py -h`` (to get help options) should
work just fine!

### Summary

Write a clone of the tail program available in unix/linux systems but
only support a very small subset of the flags/options/features it
supports. Pick and choose the complexity/scope based on the time you
have and the options you like to support. Support at least the basic
functionality you get with no options.

### Some thoughts

Things get more complicated when we involve more than one file stream.
There's a nice cross-platform directory monitoring library called
[watchdog](https://pythonhosted.org/watchdog/), and in most cases it'd
be better not to re-invent the wheel. For the purpose of this exercise,
I want to have a self-contained file that doesn't need external dependencies.

### Bugs

* When monitoring files for changes, if the length doesn't change (but,
  say, a character changes), the change isn't shown.
* Standard in monitoring should not be trusted; could really use some work.
