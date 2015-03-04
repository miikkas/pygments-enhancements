# -*- coding: utf-8 -*-
"""
    pygments.styles.lovelace
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Lovelace by Miikka Salminen

    Pygments style by Miikka Salminen (https://github.com/miikkas)
    Created for Lovelace interactive learning environment, which uses Pygments
    for source code highlighting.

    :copyright: Copyright 2015 by Miikka Salminen.
    :license: MIT, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
    Number, Operator, Punctuation, Generic, Whitespace

class LovelaceStyle(Style):
    """
    The style used in Lovelace interactive learning environment. Tries to avoid
    the "angry fruit salad" phenomenom with desaturated, dim colours.
    """

    default_style = "#222222"

    styles = {
        Whitespace:          '#a89028',
        Comment:             'italic #888888',
        Comment.Preproc:     'noitalic #289870',
        Comment.Multiline:   '#888888',

        Keyword:             '#2838a0',
        Keyword.Constant:    'italic #387838',
        Keyword.Declaration: 'italic',
        Keyword.Type:        'italic',

        Operator:            '#666666',
        Operator.Word:       '#a048a0',

        Punctuation:         '#888888',
        
        Name.Attribute:      '#387838',
        Name.Builtin:        '#387838',
        Name.Builtin.Pseudo: 'italic',
        Name.Class:          '#287088',
        Name.Constant:       '#b85820',
        Name.Decorator:      '#287088',
        Name.Entity:         '#709030', # Same colour as String.Escape
        Name.Exception:      '#908828',
        Name.Function:       '#705038',
        Name.Label:          '#289870', # Same colour as Comment.Preproc
        Name.Namespace:      '#289870',
        Name.Tag:            '#2838a0', # Same colour as Keyword
        Name.Variable:       '#b04040',
        Name.Variable.Global:'#908828', # Same colour as Name.Exception

        String:              '#b03838',
        String.Char:         '#a048a0',
        String.Doc:          'italic #a06030',
        String.Escape:       '#709030',
        String.Interpol:     'underline',
        String.Other:        '#a048a0',
        String.Regex:        '#a048a0',

        Number:              '#444444',

        Generic.Deleted:     '#c02828',
        Generic.Emph:        'italic',
        Generic.Error:       '#c02828',
        Generic.Heading:     '#666666',
        Generic.Subheading:  '#444444',
        Generic.Inserted:    '#387838',
        Generic.Output:      '#666666',
        Generic.Prompt:      '#444444',
        Generic.Strong:      'bold',
        Generic.Traceback:   '#2830a0', # Same colour as Keyword

        Error:               'bg:#a048a0',
    }
