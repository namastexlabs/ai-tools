import os

tool_name = input("Please enter the tool name:\n")

# Define the base directories
base_dir = os.path.join("./tools", tool_name)
dirs = ["models", "use_cases", "repositories", "tests"]

# Create the directories
for dir in dirs:
    os.makedirs(os.path.join(base_dir, dir), exist_ok=True)

# Create the boilerplate files
for dir in dirs:
    with open(os.path.join(base_dir, dir, "README.md"), "w") as f:
        f.write(f"# This is the {dir} for {tool_name}")

    with open(os.path.join(base_dir, dir, "example.py"), "w") as f:
        f.write(
            f"""def main():
    print('This is the {dir} for {tool_name}')
  
if __name__ == '__main__':
    main()"""
        )

print(
    f"Created tool '{tool_name}' with default directories and boilerplate README and example.py files."
)
