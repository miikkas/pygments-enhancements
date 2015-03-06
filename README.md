# pygments-enhancements
My own additions to the popular Pygments source code highlighter.

# lovelace.py
A Pygments style that tries to avoid the "angry fruit salad" effect by using
dim and desaturated colours.

# TODO
- New token Name.Customary
    * Python: self, args, kwargs
    * C, C++: argc, argv
- Move Python's None, True and False to Keyword.Constant
- "%s" string interpolation back for Py3 [DONE]
- "{identifier}" string interpolation for Py3 [DONE]
    * https://docs.python.org/3/library/string.html#format-string-syntax
- New token Comment.Hashbang [DONE]
    * For all languages with # comments
        * Python [DONE]
        * Ruby
        * Shell scripts
        * Perl
        * PHP
        * Tcl
        * Awk
    * First lines following the form #!path arg
    * Documentation: doc/docs/tokens.rst
- Command line option for pygmentize to select a style definition from file
- "<", "</" and ">" as Punctuation in HTML
