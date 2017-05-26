#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask

"""
test_{{ cookiecutter.extension_slug }}
----------------------------------

Tests for `{{ cookiecutter.extension_slug }}` module.
"""

{% if cookiecutter.use_pytest == 'y' -%}
import pytest
{% else %}
import sys
import unittest
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'click' %}
from contextlib import contextmanager
from click.testing import CliRunner
{%- endif %}

from {{ cookiecutter.extension_slug }} import {{ cookiecutter.extension_slug }}
{%- if cookiecutter.command_line_interface|lower == 'click' %}
from {{ cookiecutter.extension_slug }} import cli
{%- endif %}


{% if cookiecutter.use_pytest == 'y' -%}
@pytest.fixture
def response():
    """Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument.
    """
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


{%- if cookiecutter.command_line_interface|lower == 'click' %}
def test_command_line_interface():
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert '{{ cookiecutter.extension_slug }}.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output

{%- endif %}
{% else %}
class Test{{ cookiecutter.extension_slug|title }}(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        app.debug = True
        self.app = app

    def tearDown(self):
        self.app = None

    def test_00_something(self):
        pass

{% if cookiecutter.command_line_interface|lower == 'click' %}
    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert '{{ cookiecutter.extension_slug }}.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

{%- endif %}
{%- endif %}
