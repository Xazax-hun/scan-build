Build EYE
=========

It's a static analyzer wrapper for [Clang][CLANG]. The original `scan-build`
is written in Perl. This package contains reimplementation of that scripts
in Python. The reimplementation diverge from the original scripts in a few
places.

  [CLANG]: http://clang.llvm.org/

How to get
----------

Will be available soon from [the Python Package Index][PyPI].

  [PyPI]: https://pypi.python.org/pypi

How to build
------------

Should be quite portable on UNIX operating systems. It has been tested on
FreeBSD, GNU/Linux and OS X.

### Prerequisites

1. an ANSI **C compiler**, to compile the sources.
2. **python** interpreter (version 2.7, 3.2, 3.3, 3.4).

### Build commands

Please consider to use `virtualenv` or other tool to set up the working
environment.

    $ python setup.py build
    $ python setup.py install
    $ python setup.py test


How to use
----------

This package contains 3 executable scripts. One called `bear` which takes
a build command as argument and produce a compilation database file. Which
is a JSON file described [here][JCDB]. The second called `beye` which takes
a compilation database and run the analyzer against it and generates a report.
The third called `scan-build` which does what `bear` and `beye` together do.

After installation the usage is like this:

    $ scan-build <your build command>

It runs the analyzer and print out the location of the report at the end.
Use `--help` to know more about the commands.

  [JCDB]: http://clang.llvm.org/docs/JSONCompilationDatabase.html

Known problems
--------------

Compiler wrappers like ccache and distcc could cause duplicates or missing
items in the compilation database. Make sure you have been disabled before
you run `bear` or `scan-build`.

In case of duplicate entries, you might consider to edit the
`analyzer/bear.py` module to filter out wrapper calls (by path, or by file
name) or filter out the compiler calls (and collect the wrapper calls only).

Problem reports
---------------
If you find a bug in this documentation or elsewhere in the program or would
like to propose an improvement, please use the project's [github issue
tracker][ISSUES]. Please describing the bug and where you found it. If you
have a suggestion how to fix it, include that as well. Patches are also
welcome.

  [ISSUES]: https://github.com/rizsotto/Beye/issues