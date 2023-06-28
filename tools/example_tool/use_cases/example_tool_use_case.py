from tools.example_tool.models.example_tool_model import Example_ToolModel


def run_example_tool_use_case(input, parameters):
    # Create an instance of Example_ToolModel
    example_tool = Example_ToolModel(input, parameters)
    output = example_tool.run()
    return output
