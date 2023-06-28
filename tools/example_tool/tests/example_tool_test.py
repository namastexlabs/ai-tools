import unittest
from unittest.mock import patch, MagicMock

from tools.example_tool.use_cases.example_tool_use_case import run_example_tool_use_case


class TestExample_ToolUseCase(unittest.TestCase):
    @patch("tools.example_tool.use_cases.example_tool_use_case.Example_ToolModel")
    def test_run_example_tool_use_case(self, mock_model):
        # Arrange
        mock_instance = MagicMock()
        mock_model.return_value = mock_instance

        input = "test input"
        parameters = {"parameter1": True, "parameter2": False}

        expected_output = "expected output"
        mock_instance.run.return_value = expected_output

        # Act
        actual_output = run_example_tool_use_case(
            input,
            parameters,
        )

        # Assert
        mock_model.assert_called_once_with(input, parameters)
        mock_instance.run.assert_called_once()
        self.assertEqual(expected_output, actual_output)


if __name__ == "__main__":
    unittest.main()
