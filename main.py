# main.py

import logging
from tools.example_tool.use_cases.example_use_case import run_example_use_case

# Set up logging
logging.basicConfig(level=logging.INFO)


def main():
    # Run your application code here
    run_example_use_case("value1", "value2")


if __name__ == "__main__":
    main()
