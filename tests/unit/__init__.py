# -*- coding: utf-8 -*-
#                     The LLVM Compiler Infrastructure
#
# This file is distributed under the University of Illinois Open Source
# License. See LICENSE.TXT for details.

from . import test_command
from . import test_clang
from . import test_runner
from . import test_report
from . import test_driver
from . import test_intercept


def load_tests(loader, suite, pattern):
    suite.addTests(loader.loadTestsFromModule(test_command))
    suite.addTests(loader.loadTestsFromModule(test_clang))
    suite.addTests(loader.loadTestsFromModule(test_runner))
    suite.addTests(loader.loadTestsFromModule(test_report))
    suite.addTests(loader.loadTestsFromModule(test_driver))
    suite.addTests(loader.loadTestsFromModule(test_intercept))
    return suite
