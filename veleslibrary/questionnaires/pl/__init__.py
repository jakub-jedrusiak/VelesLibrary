"""
This file contains some open, free-to-use questionnaires in Polish.
If you want to add your own questionnaire, go ahead and add it to this file.
For other languages, use appropriate folder or the main file for English.

Every questionnaire should be a function taking name, questionOptions and pageOptions as arguments.
The default name should be uppercase abbreviation of the questionnaire name.
The function itself should be a lowercase abbreviation of the questionnaire name.
Every function should have a docstring with APA-style citation of the questionnaire
and info what it measures. See the example below. The default return value should be a PageModel.

I'd be greatful if you could also write a documentation for the questionnaire.
See the repo: https://github.com/jakub-jedrusiak/VelesDocs
"""

from .tipi import tipi
from .rses import rses
