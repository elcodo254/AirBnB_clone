#!/usr/bin/python3
"""Module that contains tests for the BaseModel class"""
import unittest
from datetime import datetime
import uuid from uui4

import models.base_model import BaseModel


class TestBaseModel_instatiation(unittest.TestCase):
    """The test for instantiation of BaseModel class"""

    def test_str_rep(self):
        """checks if string representation is appropriate"""
        bm = BaseModel()
        self.assertEqual(str(bm), f"[BaseModel] ({bm.id}) {bm.__dict__}")

    def test_idUnique(self):
        """Check if id is random and unique"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_idType(self):
        """Check that id is of type str"""
        bm = BaseModel()
        self.assertTrue(type(bm.id) is str)

    def test_created_atType(self):
        """Check attribute created_at is of type datetime"""
        bm = BaseModel()
        self.assertTrue(type(bm.created_at) is datetime)

    def test_updated_atType(self):
        """Check attribute updated_at is of type datetime"""
        bm = BaseModel()
        self.assertTrue(type(bm.updated_at) is datetime)


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""
