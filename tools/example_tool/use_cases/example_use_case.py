from tools.example_tool.models.example_model import ExampleModel


def run_example_use_case(attribute1, attribute2):
    # Create an instance of ExampleModel
    example = ExampleModel(attribute1, attribute2)

    # Call the method of ExampleModel
    example.display_attributes()
