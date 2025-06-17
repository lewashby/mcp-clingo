# CLINGO MCP Server

A Model Context Protocol (MCP) server for executing [Answer Set Programming (ASP)](https://en.wikipedia.org/wiki/Answer_set_programming) logic using the [Clingo](https://potassco.org/clingo/) Python API.

A Model Context Protocol (MCP) server for Answer Set Programming (ASP) with Clingo. This server provides a standardized interface for executing ASP programs and handling context-dependent computations.

## Overview

The ASP MCP Server is designed to:

- Execute ASP programs using the Clingo Python API
- Provide a standardized interface for ASP program execution
- Support timeout and model limit configurations

## Tools

### `execute_asp_code`

Executes a provided ASP logic program using Clingo and returns the resulting models.

- **Required inputs:**
  - `asp_code` (string): The main ASP code to execute.

- **Optional inputs:**
  - `additional_facts` (string, default: `""`): Additional facts to append to the base program.
  - `max_models` (number, default: `10`): Maximum number of models to compute (`0` for all).
  - `timeout` (number, default: `30`): Timeout in seconds for model computation.

- **Returns:**
  - A list of models (as strings) if any were found.
  - `"No models found (UNSAT)"` if the program is unsatisfiable.
  - Error message string if Clingo is not installed or execution fails.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
