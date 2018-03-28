
import unittest
from Utils.DateParser import *

class UtilitiesTest(unittest.TestCase):
    def setUp(self):
        ""

    def tearDown(self):
        ""

    def test_DateParser_ParseNames(self):
        targetTableName = "Person_UCH_CDW_20170620111203696_19000101000000000_20170620111203696"

        sourceTableName, start, end = DateParser.getDates(targetTableName)

        print()
        print(sourceTableName)
        print(start)
        print(end)