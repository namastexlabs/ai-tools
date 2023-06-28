import os


def format_tool_name(tool_name):
    # replace spaces with underscores and make lowercase for file names
    file_name = tool_name.replace(" ", "_").lower()

    # title case and remove spaces for class names
    class_name = tool_name.replace(" ", "").title()

    return file_name, class_name


# Ask the user for the name of the new tool
tool_name = input("Enter the name of the new tool: ")

# Get the formatted names
file_name, class_name = format_tool_name(tool_name)

# Define the directory structure
structure = {
    f"tools/{file_name}": ["models", "tests", "use_cases"],
}

# Define the boilerplate code
model_code = f"""class {class_name}Model:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def display_attributes(self):
        print(f"Attribute 1: {{self.attribute1}}, Attribute 2: {{self.attribute2}}")
"""

use_case_code = f"""from tools.{file_name}.models.{file_name}_model import {class_name}Model

def run_{file_name}_use_case(attribute1, attribute2):
    # Create an instance of {class_name}Model
    {file_name} = {class_name}Model(attribute1, attribute2)

    # Call the method of {class_name}Model
    {file_name}.display_attributes()
"""

test_code = f"""import unittest
from unittest.mock import patch, MagicMock

from tools.{file_name}.use_cases.{file_name}_use_case import run_{file_name}_use_case

class Test{class_name}UseCase(unittest.TestCase):
    @patch("tools.{file_name}.use_cases.{file_name}_use_case.{class_name}Model")
    def test_run_{file_name}_use_case(self, mock_model):
        # Arrange
        mock_instance = MagicMock()
        mock_model.return_value = mock_instance

        attribute1 = "test1"
        attribute2 = "test2"

        # Act
        run_{file_name}_use_case(
            attribute1,
            attribute2,
        )

        # Assert
        mock_model.assert_called_once_with(attribute1, attribute2)
        mock_instance.display_attributes.assert_called_once()


if __name__ == "__main__":
    unittest.main()
"""

# Create the directories and files
for base, dirs in structure.items():
    for dir in dirs:
        os.makedirs(f"{base}/{dir}", exist_ok=True)

    with open(f"{base}/models/{file_name}_model.py", "w") as file:
        file.write(model_code)
    with open(f"{base}/use_cases/{file_name}_use_case.py", "w") as file:
        file.write(use_case_code)
    with open(f"{base}/tests/{file_name}_test.py", "w") as file:
        file.write(test_code)

print(f"Created new tool '{tool_name}'")
