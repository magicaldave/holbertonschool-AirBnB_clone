#!/usr/bin/python3
"""module test_user
Unittest for user.py file
"""


import inspect
import unittest
from unittest import mock
import models
import pep8
from models.state import State
from models.engine.file_storage import FileStorage
import inspect


class TestBaseModelDocs(unittest.TestCase):
    """Unittest for BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.base_funcs = inspect.getmembers(State, inspect.isfunction)

    def test_pep8_conformance(self):
        """test for pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['models/state.py', 'tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the presence of a module docstring"""
        self.assertTrue(len(State.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the presence of a class docstring"""
        self.assertTrue(len(State.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        self.assertTrue(len(State.__init__.__doc__) >= 1)
        self.assertTrue(len(State.__str__.__doc__) >= 1)
        self.assertTrue(len(State.save.__doc__) >= 1)
        self.assertTrue(len(State.to_dict.__doc__) >= 1)
