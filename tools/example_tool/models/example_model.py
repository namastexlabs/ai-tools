import logging


class ExampleModel:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        self.logger = logging.getLogger(__name__)

    def display_attributes(self):
        self.logger.info(
            f"Attribute 1: {self.attribute1}, Attribute 2: {self.attribute2}"
        )
