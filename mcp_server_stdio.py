from mcp.server.fastmcp import FastMCP
from typing import Dict, Any, Union
import httpx
from urllib.parse import urlencode

mcp = FastMCP("Conversion", port=8080)

BASE_API = "http://localhost:8000/convert"

async def make_request(url: str) -> Dict[str, Any]:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url=url)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None

def format(response: Dict[str, Any]) -> str:
    keys = list(response.keys())
    values = list(response.values())
    formatted_text = f"{values[0]} {keys[0]} are equal to {values[1]} {keys[1]}"
    return formatted_text


@mcp.tool()
async def meters_to_miles(meters: Union[float, int]) -> str:
    """
    Convert meters to miles

    Parameters:
        meters (float): the meters quantity to convert (e.g. 1.0, 2.5) 
    """
    url = f"{BASE_API}/meters"
    params = {"m": meters}
    encoded_url_with_params = f"{url}?{urlencode(params)}"
    response = await make_request(encoded_url_with_params)
    return format(response)

@mcp.tool()
async def kg_to_pounds(kg: Union[float, int]) -> str:
    """
    Convert kg to pounds

    Parameters:
        kg (float): the kg quantity to convert (e.g. 1.0, 2.5) 
    """
    url = f"{BASE_API}/kg"
    params = {"kg": kg}
    encoded_url_with_params = f"{url}?{urlencode(params)}"
    response = await make_request(encoded_url_with_params)
    return format(response)


if __name__ == "__main__":
    print("MCP running")
    # IMPORTANT
    # For STDIO-based servers: Never write to standard output (stdout).
    # Writing to stdout will corrupt the JSON-RPC messages and break your server.
    # For HTTP-based servers: Standard output logging is fine since it doesn’t interfere with HTTP responses.
    # Best Practices: Use a logging library that writes to stderr or files.
    mcp.run(transport="stdio")