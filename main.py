"""
MCP Server Entry Point for Render.com
"""
import os
import sys
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """Run the MCP server."""
    try:
        # Import the generated MCP server module
        import mcp_server

        logger.info("Starting MCP server...")

        # The MCP server should have a main() function that runs the server
        if hasattr(mcp_server, 'main'):
            # Run the MCP server's main function (it handles its own event loop)
            mcp_server.main()
        else:
            logger.error("No main() function found in mcp_server module")
            sys.exit(1)

    except ImportError as e:
        logger.error(f"Failed to import MCP server: {e}")
        logger.error("Make sure mcp_server.py exists in the root directory")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Error running MCP server: {e}")
        import traceback
        logger.error(traceback.format_exc())
        sys.exit(1)

if __name__ == "__main__":
    main()
