# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import absolute_import, division, print_function

import os

from _cffi_src.utils import build_ffi


with open(os.path.join(
    os.path.dirname(__file__), "hazmat_src/constant_time.h"
)) as f:
    types = f.read()

with open(os.path.join(
    os.path.dirname(__file__), "hazmat_src/constant_time.c"
)) as f:
    functions = f.read()

ffi = build_ffi(
    module_name="_constant_time",
    cdef_source=types,
    verify_source=functions
)
