#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import sys

from .tools import logger, run_process, wrap_run


@wrap_run
def run(args):
    proc_args = ["wasmer", "run", "--dir=.", "--enable-all"]+args[1:]
    return_code = run_process(proc_args, check=False)
    return return_code.returncode


if __name__ == '__main__':
    run()
