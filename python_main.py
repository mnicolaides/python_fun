from typing import List
from python_playground import VentilatorMode, Ventilator
import logging

logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


def main():

    body_systems: List = []
    body_systems.append("You stink")

    ventilator: Ventilator = Ventilator()
    ventilator.Process(body_systems)

    for bs in ventilator.body_systems:
        logger.debug('bs is %s', bs)

    body_systems = 1
    logging.debug(body_systems)

if __name__ == "__main__":
    main()