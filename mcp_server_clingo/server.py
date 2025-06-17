# ASP MCP Server
# A Model Context Protocol server for Answer Set Programming with Clingo

from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("ASP Server")

@mcp.tool()
async def execute_asp_code(
    asp_code: str, 
    additional_facts: str = "",
    max_models: int = 10,
    timeout: int = 30,
) -> str:
    """
    Execute ASP code using Clingo Python API and return the results.
    
    Args:
        asp_code: The ASP program to execute
        additional_facts: Additional facts to add to the program
        max_models: Maximum number of models to generate (0 for all)
        timeout: Timeout in seconds
        context: Optional context class providing functions that can be called during grounding using @ syntax
    """
    try:
        import clingo
        
        # Combine ASP code with additional facts
        full_program = asp_code
        if additional_facts.strip():
            full_program += "\n\n% Additional facts:\n" + additional_facts
        
        # Create a control object
        ctl = clingo.Control()
        
        # Add the program
        ctl.add("base", [], full_program)

        # Get context class if provided
        # todo: add context
        
        # Ground the program with context if provided
        ctl.ground([("base", [])])
        
        # Configure number of models to compute
        if max_models > 0:
            ctl.configuration.solve.models = max_models
        
        # Store models
        models = []
        
        # Define a callback for each model
        def on_model(model):
            # Get all atoms in the model
            atoms = []
            for atom in model.symbols(shown=True):
                atoms.append(str(atom))
            models.append(" ".join(atoms))
        
        # Solve with timeout using async solving
        with ctl.solve(on_model=on_model, async_=True) as handle:
            handle.wait(timeout)
            handle.cancel()
            handle = handle.get()
        
        # Return response
        if models:
            return models
        else:
            return "No models found (UNSAT)"
        
    except ImportError:
        return "Error: Clingo Python API not available. Please install clingo: pip install clingo"
    except Exception as e:
        return f"Error executing ASP code: {str(e)}"
