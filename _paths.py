# -*- coding: utf-8 -*-
"""
Paths for the different folders.
"""
from pathlib import Path
import uuid


PATH_ROOT = Path(__file__).parents[0]

PATH_TEST = PATH_ROOT / 'tests'
PATH_LOG = PATH_ROOT / 'logs'

# unique export id
EXPORT_ID = uuid.uuid4()


if __name__ == '__main__':
    print('Root directory is:', PATH_ROOT)
    print('test:', PATH_TEST)
