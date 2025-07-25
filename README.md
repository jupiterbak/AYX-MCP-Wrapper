# AYX-MCP-Wrapper

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![MCP Protocol](https://img.shields.io/badge/MCP-Protocol-green.svg)](https://modelcontextprotocol.io/)

<a href="https://glama.ai/mcp/servers/@jupiterbak/AYX-MCP-Wrapper">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/@jupiterbak/AYX-MCP-Wrapper/badge" alt="AYX-MCP-Wrapper MCP server" />
</a>

## ⚠️ DISCLAIMER

**This is NOT an official implementation.**

This project is a personal initiative and is not affiliated with, endorsed by, or supported by any company. Even if the maintainer is an employee of a related company, this project is developed independently without any official backing or support.

---

A Model Context Protocol (MCP) server that provides a comprehensive interface to Alteryx Servers. This wrapper enables AI assistants and other MCP clients to interact with Alteryx Server for managing workflows, collections, users, schedules, credentials, and more.

## Features

- **Advanced Search**: Find users, workflows, and assets with flexible search options
- **Workflow Operations**: Execute, transfer, and manage workflows with full control
- **Workflow Assets**: Download workflow packages and extract XML for analysis
- **Job Monitoring**: Track and manage workflow execution jobs in real-time
- **Collections Management**: Create, update, delete, and organize collections
- **User Management**: Manage users, their assets, and permissions efficiently
- **Schedule Management**: Create and manage workflow schedules and automation
- **Credential Management**: Handle server credentials and secure connections


## Prerequisites

- **Python 3.10+** - Modern Python with type hints support
- **Alteryx Server** - With API access enabled
- **OAuth2 Credentials** - Client ID and Secret for authentication

## Installation

### Quick Start with uv (Recommended)

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install the MCP server
uv pip install mcp-server-alteryx
```

### Using pip

```bash
pip install mcp-server-alteryx
```

### From Source

```bash
git clone https://github.com/jupiterbak/AYX-MCP-Wrapper.git
cd AYX-MCP-Wrapper
uv sync
uv run pip install -e .
```

## Configuration

### Environment Variables

Set up your Server credentials using environment variables:

```bash
# Required: Server API URL
export ALTERYX_API_HOST="https://your-server.com/webapi/"

# Required: OAuth2 Client Credentials
export ALTERYX_CLIENT_ID="your-client-id"
export ALTERYX_CLIENT_SECRET="your-client-secret"

# Optional: SSL Verification (default: true)
export ALTERYX_VERIFY_SSL="1"

# Optional: temporary folder
export ALTERYX_TEMP_DIRECTORY="your-temp-directory"

# Optional: Logging level
export LOG_LEVEL="INFO"
```

### Configuration File

Alternatively, create a `.env` file in your project root:

```env
ALTERYX_API_HOST=https://your-server.com/webapi/
ALTERYX_CLIENT_ID=your-client-id
ALTERYX_CLIENT_SECRET=your-client-secret
ALTERYX_VERIFY_SSL=1
ALTERYX_TEMP_DIRECTORY=your-temp-directory
LOG_LEVEL=INFO
```

## Usage

### Claude Desktop Integration

To use this MCP server with Claude Desktop, add the following configuration to your Claude Desktop settings:

```json
{
  "mcpServers": {
    "alteryx": {
      "command": "uvx",
      "args": ["mcp-server-alteryx", "--transport", "stdio"],
      "env": {
        "ALTERYX_API_HOST": "https://your-server.com/webapi/",
        "ALTERYX_CLIENT_ID": "your-client-id",
        "ALTERYX_CLIENT_SECRET": "your-client-secret",
        "ALTERYX_VERIFY_SSL": "1",
        "ALTERYX_TEMP_DIRECTORY": "your-temp-directory"
      }
    }
  }
}
```
```

However, we recommend using it in combination with the "Sequential Thinking" tool:

```json
{   "mcpServers": {
  "sequential-thinking": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-sequential-thinking"
      ]
    },
    "alteryx": {
      "command": "uvx",
      "args": ["mcp-server-alteryx", "--transport", "stdio"],
      "env": {
        "ALTERYX_API_HOST": "http://localhost/webapi/",
        "ALTERYX_CLIENT_ID": "your-client-id",
        "ALTERYX_CLIENT_SECRET": "your-client-secret",
        "ALTERYX_VERIFY_SSL": "1",
        "ALTERYX_TEMP_DIRECTORY": "your-temp-directory"
      }
    }
  }
}
```

**Configuration Options:**
- `command`: The uvx executable to use
- `args`: Command line arguments for the MCP server
- `env`: Environment variables for Server authentication

**Transport Options:**
- `stdio`: Standard input/output (recommended for Claude Desktop)
- `sse`: Server-Sent Events
- `streamable-http`: HTTP streaming

### Cursor Integration

For Cursor IDE integration, add to your Cursor settings:

```json
{
  "mcpServers": {
    "alteryx": {
      "command": "uvx",
      "args": ["mcp-server-alteryx", "--transport", "stdio"],
      "env": {
        "ALTERYX_API_HOST": "https://your-alteryx-server.com/webapi/",
        "ALTERYX_CLIENT_ID": "your-client-id",
        "ALTERYX_CLIENT_SECRET": "your-client-secret",
        "ALTERYX_TEMP_DIRECTORY": "your-temp-directory"
      }
    }
  }
}
```

### Command Line Interface

The MCP server can be run with different transport options:

```bash
# Using stdio transport (default)
uvx run src.main --transport stdio

# Using Server-Sent Events (SSE)
uvx run src.main --transport sse

# Using HTTP streaming
uvx run src.main --transport streamable-http

# Set log level
uvx run src.main --log-level DEBUG

# Run with custom configuration
uvx run src.main --transport stdio --log-level INFO
```

## Available Tools

The MCP server provides comprehensive tools organized by functionality:

### Collections Management

| Function | Description | Parameters |
|----------|-------------|------------|
| `get_all_collections()` | Retrieve all accessible collections | None |
| `get_collection_by_id(collection_id)` | Get specific collection details | `collection_id: str` |
| `create_collection(name)` | Create a new collection | `name: str` |
| `update_collection_name_or_owner(collection_id, name, owner_id)` | Update collection properties | `collection_id: str, name: str, owner_id: str` |
| `add_workflow_to_collection(collection_id, workflow_id)` | Add workflow to collection | `collection_id: str, workflow_id: str` |
| `remove_workflow_from_collection(collection_id, workflow_id)` | Remove workflow from collection | `collection_id: str, workflow_id: str` |
| `add_schedule_to_collection(collection_id, schedule_id)` | Add schedule to collection | `collection_id: str, schedule_id: str` |
| `remove_schedule_from_collection(collection_id, schedule_id)` | Remove schedule from collection | `collection_id: str, schedule_id: str` |
| `delete_collection(collection_id)` | Delete a collection | `collection_id: str` |

### Workflow Operations

| Function | Description | Parameters |
|----------|-------------|------------|
| `get_all_workflows()` | Retrieve all accessible workflows | None |
| `get_workflow_by_id(workflow_id)` | Get specific workflow details | `workflow_id: str` |
| `update_workflow_name_or_comment(workflow_id, name, comment)` | Update workflow properties | `workflow_id: str, name: str, comment: str` |
| `transfer_workflow(workflow_id, new_owner_id)` | Transfer workflow ownership | `workflow_id: str, new_owner_id: str` |
| `get_workflow_jobs(workflow_id)` | Get jobs for a workflow | `workflow_id: str` |
| `start_workflow_execution(workflow_id, input_data)` | Start workflow execution and return job ID | `workflow_id: str, input_data: List[InputData]` |
| `execute_workflow_with_monitoring(workflow_id, input_data)` | Execute workflow and monitor completion | `workflow_id: str, input_data: List[InputData]` |
| `download_workflow_package_file(workflow_id, output_directory)` | Download workflow package | `workflow_id: str, output_directory: str` |
| `get_workflow_xml(workflow_id)` | Extract workflow XML | `workflow_id: str` |

### User Management

| Function | Description | Parameters |
|----------|-------------|------------|
| `get_all_users()` | Retrieve all accessible users | None |
| `get_user_by_id(user_id)` | Get specific user details | `user_id: str` |
| `get_user_by_email(email)` | Find user by email | `email: str` |
| `get_user_by_name(name)` | Find user by name | `name: str` |
| `get_user_by_first_name(first_name)` | Find user by first name | `first_name: str` |
| `get_all_user_assets(user_id)` | Get all assets owned by user | `user_id: str` |
| `get_user_assets_by_type(user_id, asset_type)` | Get specific asset types | `user_id: str, asset_type: str` |
| `update_user_details(user_id, first_name, last_name, email)` | Update user information | `user_id: str, first_name: str, last_name: str, email: str` |
| `transfer_all_assets(user_id, new_owner_id, transfer_workflows, transfer_schedules, transfer_collections)` | Transfer user assets | `user_id: str, new_owner_id: str, transfer_workflows: bool, transfer_schedules: bool, transfer_collections: bool` |
| `deactivate_user(user_id)` | Deactivate a user | `user_id: str` |
| `reset_user_password(user_id)` | Reset user password | `user_id: str` |

### Schedule Management

| Function | Description | Parameters |
|----------|-------------|------------|
| `get_all_schedules()` | Retrieve all accessible schedules | None |
| `get_schedule_by_id(schedule_id)` | Get specific schedule details | `schedule_id: str` |
| `deactivate_schedule(schedule_id)` | Deactivate a schedule | `schedule_id: str` |
| `activate_schedule(schedule_id)` | Activate a schedule | `schedule_id: str` |
| `update_schedule_name_or_comment(schedule_id, name, comment)` | Update schedule properties | `schedule_id: str, name: str, comment: str` |
| `change_schedule_owner(schedule_id, new_owner_id)` | Change schedule ownership | `schedule_id: str, new_owner_id: str` |

### Job Monitoring

| Function | Description | Parameters |
|----------|-------------|------------|
| `get_all_job_messages(job_id)` | Get messages for a specific job | `job_id: str` |
| `get_job_by_id(job_id)` | Get job details | `job_id: str` |
| `get_job_output_data(job_id)` | Get output data files from completed job | `job_id: str` |

### Credentials & Connections

| Function | Description | Parameters |
|----------|-------------|------------|
| `get_all_credentials()` | Retrieve all accessible credentials | None |
| `get_credential_by_id(credential_id)` | Get specific credential details | `credential_id: str` |
| `lookup_connection(connection_id)` | Lookup DCM connection | `connection_id: str` |
| `get_connection_by_id(connection_id)` | Get connection details | `connection_id: str` |

## Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/jupiterbak/AYX-MCP-Wrapper.git
cd AYX-MCP-Wrapper

# Install dependencies
uv sync

# Install in development mode
uv run pip install -e .
```


## Contributing

We welcome contributions! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Related Projects

- <a href="https://modelcontextprotocol.io/" target="_blank" rel="noopener noreferrer">Model Context Protocol</a> - The MCP specification
- <a href="https://claude.ai/download" target="_blank" rel="noopener noreferrer">Claude Desktop</a> - Claude Desktop application

---

**Made with ❤️ for the community** 