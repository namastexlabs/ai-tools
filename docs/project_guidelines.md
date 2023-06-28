# Project Guidelines

## Table of Contents

  1. [Introduction](#introduction)
  2. [Project Structure](#project-structure)
  3. [Documentation](#documentation)

## Introduction <a name="introduction"></a>

We follow the **N.E.U.R.O.N.** principles for the developments of tools. These principles are based on some famous principles, but are more specific for our tools.

The principles are as follows:

### **N**on-repetitive (DRY Principle)

  > Each piece of knowledge or logic should exist in one place only in the system. Repetition should lead to abstraction or reusability strategies.

### **E**xtensibility

  > Components should be open for extension but closed for modification. This enables the addition of new features without changing existing code.

### **U**nity of Dependencies

  > High-level modules should not depend on low-level ones. Instead, they should all depend on abstractions, encouraging decoupling and exchangeability of components.

### **R**obust yet Simple

  > Tools should prioritize simplicity without compromising robustness or scalability. Avoid unnecessary complexity in code design.

### **O**utcome Predictability

  > Each tool should have well-defined inputs and outputs, and given the same parameters, results should be consistent. This ensures reliability and trust in the tools.

### **N**on-negotiable Testing

  > Each tool should come with its own test suite to validate that the component functions as expected. This promotes confidence during refactoring and ensures the tool's integrity.

## Project Structure <a name="project-structure"></a>
  
 Here is a high-level example of how the project structure might look like when applying the NEURON guidelines:

```bash
namastex_toolkit
  ├── tools
  │   ├── tokenizer
  │   │   ├── models
  │   │   ├── use_cases
  │   │   ├── tests
  │   ├── transcriptor
  │   │   ├── models
  │   │   ├── use_cases
  │   │   ├── tests
  │   └── ...
  ├── config
  ├── lib
  ├── docs
  ├── scripts
  ├── .gitignore
  └── README.md
```

**tools:** Contains all the source code for your project organized by features/toolsets. Each toolset will have its own folder.

Each feature/toolset directory is further divided into:

- **models:** This directory contains all data models or entities related to the toolset.
- **use_cases:** This directory contains all the business logic and rules for the toolset.
- **tests:** This directory contains all the unit tests, integration tests, and end-to-end tests for the toolset.

**config:** Contains configuration files, such as environment variables.

**lib:** Contains any shared code that can be used across different toolsets.

**docs:** Contains all documentation related to the project.

**scripts:** Contains scripts for build, deployment, and other automation tasks.

**README.md:** An overview of the project, including setup and usage instructions, contribution guidelines, etc.

This structure adheres to the NEURON principles by ensuring that each toolset is clearly isolated (N), is designed for extensibility (E), follows dependency inversion (U), is simple and robust (R), guarantees predictable outcomes (O), and includes a robust testing suite (N). It also adheres to clean architecture by ensuring that business rules and external concerns are clearly separated.

## Documentation <a name="documentation"></a>

Documentation is a crucial part of any project. It helps developers understand the project's purpose, how to set it up, and how to use it. It also helps with onboarding new developers and maintaining the project in the long run.

Here are some guidelines for writing documentation:

- **Tools:** Each toolset should have its own documentation page. This page should include an overview of the toolset, its purpose, and how to use it. It should also include a link to the toolset's repository.
