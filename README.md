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
- "%s" string interpolation back for Py3
- "{identifier}" string interpolation for Py3
- New token Comment.Hashbang
    * For all languages with # comments
    * First lines following the form #!path arg
- Command line option for pygmentize to select a style definition from file

