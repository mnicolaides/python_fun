"""module doc string goes here"""
from dataclasses import dataclass
from typing import Optional, Union, List
import logging

logger = logging.getLogger(__name__)

@dataclass
class VentilatorMode: 
    """description of class"""
    body_systems: List[str]
    code: Optional[str]
    display: Optional[str]
    system_url: Optional[str]
    value: Optional[Union[int, float]]

    def __init__(self) -> None:
        self.body_systems = []
        self.code = None
        self.display = None
        self.system_url = None
        self.value = None    

    def Process(self, body_systems) -> None:
        """doc string goes here"""
        self.body_systems = body_systems


@dataclass
class Ventilator(VentilatorMode):
    """description of class"""

    def __init__(self) -> None:
        """doc string goes here"""
        VentilatorMode.__init__(self)
        self.body_systems = []


class Tester:
    """description of class"""
    
    @staticmethod
    def get_ventilator() -> None:
        """doc string goes here"""
        vent = Ventilator()
        vent.body_systems.append('Hello')

        for bs in vent.body_systems:
            logger.debug('bs is %s', bs)

