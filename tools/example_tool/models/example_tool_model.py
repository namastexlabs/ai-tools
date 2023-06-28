from typing import Dict, Optional


class Example_ToolModel:
    def __init__(self, input: str, parameters: Dict[str, bool]):
        self.input = input
        self.parameters = parameters

    def run(self) -> Optional[str]:
        # Check for 'uppercase' parameter
        if self.parameters.get("uppercase", False):
            self.input = self.input.upper()

        # Check for 'remove_punctuation' parameter
        if self.parameters.get("remove_punctuation", False):
            self.input = "".join(e for e in self.input if e.isalnum() or e.isspace())

        return self.input
