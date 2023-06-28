import unittest
from unittest.mock import patch, MagicMock

from tools.example_tool.use_cases.example_tool_use_case import run_example_tool_use_case

class TestExample_ToolUseCase(unittest.TestCase):
    @patch("tools.example_tool.use_cases.example_tool_use_case.Example_ToolModel")
    def test_run_example_tool_use_case(self, mock_model):
        # Arrange
        mock_instance = MagicMock()
        mock_model.return_value = mock_instance

        attribute1 = "test1"
        attribute2 = "test2"

        # Act
        run_example_tool_use_case(
            attribute1,
            attribute2,
        )

        # Assert
        mock_model.assert_called_once_with(attribute1, attribute2)
        mock_instance.display_attributes.assert_called_once()


if __name__ == "__main__":
    unittest.main()
