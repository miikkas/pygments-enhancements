"""
    Regex parser for Python 3 string.format(...) formatting syntax.

    https://docs.python.org/3/library/string.html#format-string-syntax
"""

import re

si = r'\{' '((\w+)((\.\w+)|(\[[^\]]+\]))*)?' '(\![sra])?' '(\:(.?[<>=\^])?[-+ ]?#?0?(\d+)?,?(\.\d+)?[bcdeEfFgGnosxX%]?)?' '\}'
_si = re.compile(si)

def main():
    should_match = [
        # [number | identifier]
        "{}",
        "{0}",
        "{9}",
        "{a}",
        "{abcd_1}",
        "{öäåü}",
        # [number | identifier] [ "." attribute | "[" key "]" ]*
        "{0.a}",
        "{9.abcd_1}",
        "{a.a}",
        "{a.abcd_1}",
        "{0[0]}",
        "{9[a]}",
        "{a[abcd_1]}",
        "{abcd_1[abcd_1].abcd_1}",
        "{a.b.c[d].e[f].g.h[i][j]}",
        # with conversion
        "{dog!a}",
        "{cat!s}",
        "{bird!r}",
    ]
    should_not_match = [
        "",
        "{",
        "{ }",
    ]

    print("Running tests for {} strings that should match.".format(len(should_match)))
    for sm in should_match:
        if re.match(_si, sm) is None:
            print("{test_string} - incorrect non-match!".format(test_string=sm))
    print("Done.")

    print("Running tests for {} strings that shouldn't match.".format(len(should_not_match)))
    for snm in should_not_match:
        if re.match(_si, snm) is not None:
            print("{test_string} - incorrect match!".format(test_string=snm))
    print("Done.")

if __name__ == "__main__":
    main()
