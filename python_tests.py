import unittest
import logging
from python_playground import StuffBase, Stuff
from typing import List

logger = logging.getLogger(__name__)

class UTester(unittest.TestCase):
    """docstring goes here"""

    def tester(self):
        """docstring goes here"""
        stuff = Stuff()
        stuff.body_systems.append('Hellow')
        stuff.body_systems.append('Hello')
        bsr: List = []
        bsr.append('Goodbye')
        bsr.append('Ciao')
        stuff.Process(bsr)

        for bs in stuff.body_systems:
            logger.debug('bs is %s', bs)
            self.assertEqual(bs, 'Hello')

if __name__ == '__main__':
	unittest.main()