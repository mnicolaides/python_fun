import unittest
import logging
from python_playground import VentilatorMode, Ventilator
from typing import List

logger = logging.getLogger(__name__)

class UTester(unittest.TestCase):
    """docstring goes here"""

    def tester(self):
        """docstring goes here 035107"""

        vent = Ventilator()
        vent.body_systems.append('Hellow')
        vent.body_systems.append('Hello')
        bsr: List = []
        bsr.append('Goodbye')
        bsr.append('Ciao')
        vent.Process(bsr)

        for bs in vent.body_systems:
            logger.debug('bs is %s', bs)
            self.assertEqual(bs, 'Hello')

if __name__ == '__main__':
	unittest.main()