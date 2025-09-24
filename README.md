# MCP Server Demo

A demo implementation of a **Model Context Protocol (MCP)** server using **FastAPI** and the **[mcp-sdk for Python](https://modelcontextprotocol.io/docs/getting-started/intro)**. This server is designed as a lightweight reference implementation to support advanced agentic RAG systems and other MCP-based architectures.

This custom MCP server is designed to work with this [project](https://github.com/stefano-chen/Advanced_Agentic_RAG_custom_MCP)

---

## Table of Contents

- [About](#about)  
- [Features](#features)  
- [Architecture & Components](#architecture--components)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
  - [Running the Server](#running-the-server)  
- [Usage & Endpoints](#usage--endpoints)  
- [Integration with Agentic RAG](#integration-with-agentic-rag)  
- [Configuration & Customization](#configuration--customization)  
- [Project Structure](#project-structure)  
- [Contributing](#contributing)  
- [License](#license)  

---

## About

MCP Server Demo is a reference server for the **Model Context Protocol (MCP)**, built in Python using the mcp-sdk.\
It's intended for experimentation, learning, and integration with more complex systems (e.g. agentic RAG setups).

---

## Features

- HTTP interface (via FastAPI) to accept MCP requests  
- STDIO mode for simpler or local testing  
- Minimal dependencies and clear code paths  

---

## Architecture & Components

| Component | Description |
|---|---|
| `api_server.py` | Primary HTTP interface (FastAPI) handling service endpoints |
| `mcp_server_http.py` | Custom MCP server using the HTTP transport mode |
| `mcp_server_stdio.py` | Custom MCP server using the STDIO transport mode |
| `requirements.txt` | Dependencies and version constraints |


## Getting Started

### Prerequisites

- Python 3.9+  
- `pip`  
- (Optional) Virtual environment tool, e.g. `venv` or `virtualenv`

### Installation
1. Clone the repo:
    ```bash
        git clone https://github.com/stefano-chen/Advanced_Agentic_RAG.git
        cd Advanced_Agentic_RAG
    ```
2. Create and activate a venv:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate      # macOS / Linux
    .\.venv\Scripts\activate       # Windows (PowerShell / cmd)
    ```
3. Install requirements:
    ```bash
    pip install -r requirements.txt
    ```
4. Launch the FastAPI server
    ```bash
    fastapi run api_server.py
    ```
    This will launch the MCP server on the default port 8000. The MCP server will interact with this service using the endpoints

5. Running the MCP server in HTTP mode
    ```bash
    python mcp_server_http.py
    ```
    This will allow external LLM to access the MCP server via HTTP protocol