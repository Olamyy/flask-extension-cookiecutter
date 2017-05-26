#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask

"""
test_flask_extension
----------------------------------

Tests for `flask_extension` module.
"""


import sys
import unittest
from contextlib import contextmanager
from click.testing import CliRunner

from flask_extension import flask_extension
from flask_extension import cli



class TestFlask_extension(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        app.debug = True
        self.app = app

    def tearDown(self):
        self.app = None

    def test_00_something(self):
        pass


    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'flask_extension.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
