"""
All packages need this module, it can be empty,
but indicates that the directory contains a python package.
This file is exacuted when the package is imported.
"""
from .harmless.birds import Birds
from .dangerous.fish import Fish
"""
Import Mammals and Birds classes when animal package is imported.
The dot in from of the package name tells python to only look in the
current package (folder).
"""
