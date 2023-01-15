# -*- coding: utf-8 -*-

import sys
import os
print(os.path.abspath(os.path.join(os.path.dirname('__main__'))))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname('__main__'))))

import importscript