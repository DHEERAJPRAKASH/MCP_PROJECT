# Model Context Protocol (MCP) Multi-Agent Demo

This project demonstrates how to set up and communicate with custom Model Context Protocol (MCP) servers in Python. It showcases multi-agent orchestration using LangChain, Groq, and MCP adapters, enabling both local and remote tool integration.

## Features
- **Custom MCP Servers:** Math and Weather agents, each as independent MCP servers
- **Multi-Transport Communication:** Local (stdio) and remote (HTTP) transports
- **LangChain Integration:** Unified agent interface for tool invocation
- **Async Orchestration:** Efficient, non-blocking agent communication

## Components

### 1. `mathserver.py`
A custom MCP server providing math operations (add, multiply) via stdio transport.

### 2. `weather.py`
A custom MCP server providing weather information via HTTP transport - (Static content for demo).

### 3. `client.py`
A Python client that connects to both servers, discovers their tools, and invokes them using a LangChain agent powered by Groq.

## Setup Instructions

1. **Clone the repository**

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables:**
- Create a `.env` file with your `GROQ_API_KEY`:
  ```env
  GROQ_API_KEY=your_groq_api_key_here
  ```

4. **Run the servers:**
- Start the weather server (in one terminal):
  ```bash
  python weather.py
  ```
- The math server is started automatically by the client when needed.

5. **Run the client:**
```bash
python client.py
```

## Example Output
```
Math Response:  The answer is 900
Weather Response:  The weather in delhi is sunny
```

## Learning Outcomes
- How to build and register custom MCP servers
- How to enable communication between agents using stdio and HTTP
- How to orchestrate multi-agent workflows with LangChain

## Requirements
- Python 3.8+
- See `requirements.txt` for Python dependencies

## License
MIT
