from tools.example_tool.models.example_tool_model import Example_ToolModel

def run_example_tool_use_case(attribute1, attribute2):
    # Create an instance of Example_ToolModel
    example_tool = Example_ToolModel(attribute1, attribute2)

    # Call the method of Example_ToolModel
    example_tool.display_attributes()
