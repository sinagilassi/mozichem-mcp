# MoziChem-MCP

A collection of Model Context Protocol (MCP) servers for chemical engineering and chemistry applications, built on top of the powerful [MoziChem framework](https://github.com/sinagilassi/mozichem-hub). This repository provides specialized MCP tools that enable AI assistants to perform complex chemical calculations, thermodynamic modeling, and process engineering tasks.

## 🧪 Overview

MoziChem-MCP bridges the gap between AI language models and chemical engineering calculations by providing structured access to thermodynamic models, equation of state calculations, phase equilibrium computations, and other essential chemical engineering tools through the Model Context Protocol.

> **Important Notes:**
> This repository is actively maintained and will be updated with new MCP servers and features in the future. Stay tuned for additions to support more chemical engineering domains.

## 🚀 Features

### Current MCP Servers

- **🌡️ EOS Models MCP** (`eos-models-mcp`)
  - Equation of State calculations using various models (Peng-Robinson, Soave-Redlich-Kwong, Redlich-Kwong, van der Waals)
  - Fugacity calculations for pure components and mixtures
  - Thermodynamic property predictions
  - Phase behavior analysis

- **⚖️ Flash Calculations MCP** (`flash-calculations-mcp`)
  - Vapor-liquid equilibrium calculations
  - Multi-component phase equilibrium
  - Temperature and pressure flash calculations
  - Bubble point and dew point calculations

## 📦 Installation

### Prerequisites

- Python 3.13 or higher
- [uv](https://docs.astral.sh/uv/) package manager (recommended)

### Install from Source

```bash
# Clone the repository
git clone https://github.com/sinagilassi/mozichem-mcp.git
cd mozichem-mcp

# Install using uv (recommended)
uv sync

# Or install using pip
pip install -e .
```

### Install from PyPI (when available)

```bash
pip install mozichem-mcp
```

## 🔧 Usage

### Running MCP Servers

Each MCP server can be run independently:

#### EOS Models MCP Server

```bash
# Using the installed command
mozichem-mcp-eos-models

# Or run directly with Python
python -m mozichem_mcp.mcp.eos_models
```

#### Flash Calculations MCP Server

```bash
# Using the installed command
mozichem-mcp-flash-calculation

# Or run directly with Python
python -m mozichem_mcp.mcp.flash_calculation
```

### Integration with AI Assistants

These MCP servers are designed to work with AI assistants that support the Model Context Protocol, such as:

- Claude Desktop
- Other MCP-compatible AI tools

#### Example Configuration for Claude Desktop

Add to your Claude Desktop configuration:

```json
{
  "mcpServers": {
    "mozichem-eos": {
      "command": "mozichem-mcp-eos-models",
      "args": []
    },
    "mozichem-flash": {
      "command": "mozichem-mcp-flash-calculation",
      "args": []
    }
  }
}
```

### Example Calculations

Once integrated with an AI assistant, you can perform calculations like:

```text
"Calculate the fugacity of methane at 300K and 10 bar using the Peng-Robinson equation of state"

"Perform a flash calculation for a mixture of 40% methane and 60% ethane at 250K and 20 bar"
```

## 📚 Documentation

### Chemical Engineering Applications

- **Process Design**: Use for preliminary process calculations and design
- **Research**: Integrate with computational workflows for chemical engineering research
- **Education**: Enhance learning with interactive thermodynamic calculations
- **Industry**: Support engineering decisions with reliable thermodynamic data

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request to improve the project.

## 📝 License

This project is licensed under the MIT License. You are free to use, modify, and distribute this software in your own applications or projects. However, if you choose to use this app in another app or software, please ensure that my name, Sina Gilassi, remains credited as the original author. This includes retaining any references to the original repository or documentation where applicable. By doing so, you help acknowledge the effort and time invested in creating this project.

## ❓ FAQ

For any questions, contact me on [LinkedIn](https://www.linkedin.com/in/sina-gilassi/).

## 👨‍💻 Authors

- [@sinagilassi](https://www.github.com/sinagilassi)

---

⭐ **Star this repository** if you find it useful for your chemical engineering projects!

🐛 **Report issues** or 💡 **suggest new features** in the [Issues](https://github.com/sinagilassi/mozichem-mcp/issues) section.
