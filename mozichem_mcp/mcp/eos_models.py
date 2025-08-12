# import libs
from mozichem_hub import __version__
from mozichem_hub.prebuilt import create_mozichem_mcp, get_mozichem_mcp


def main():
    """Entry point for EOS Models MCP server (stdio only)."""

    # Version
    print(f"[bold green]Mozichem Hub Version: {__version__}[/bold green]")

    # List available MCPs
    mcp_names = get_mozichem_mcp()
    print(f"[bold cyan]Available MCPs:[/bold cyan] {mcp_names}")

    # Build and run the MCP server
    thermo_models_mcp = create_mozichem_mcp(name="eos-models-mcp")
    thermo_models_mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
