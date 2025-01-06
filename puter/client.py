import requests
import json
from typing import List, Dict, Any, Union
from rich.console import Console

console = Console(highlight=False)

class PuterAI:
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("api key is required")
        self.url = "https://api.puter.com/drivers/call"
        self.api_key = api_key
        self.headers = {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "authorization": f"Bearer {api_key}",
            "content-type": "application/json;charset=UTF-8",
            "origin": "https://app.onecompiler.com",
            "referer": "https://app.onecompiler.com/",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site"
        }

    def create_completion(self, 
                         messages: List[Dict[str, str]], 
                         model: str = "gpt-4o-mini",
                         driver: str = "openai-completion",
                         stream: bool = False) -> Union[Dict[str, Any], str]:
        """create a chat completion"""
        payload = {
            "interface": "puter-chat-completion",
            "driver": driver,
            "test_mode": False,
            "method": "complete",
            "args": {
                "messages": messages,
                "model": model,
                "stream": stream
            }
        }
        
        if stream:
            return self._stream_request(payload)
        return self._send_request(payload)

    def _stream_request(self, payload: Dict[str, Any]) -> str:
        try:
            response = requests.post(
                self.url,
                headers=self.headers,
                json=payload,
                stream=True
            )
            
            if response.status_code == 200:
                full_response = ""
                for line in response.iter_lines():
                    if line:
                        try:
                            data = json.loads(line.decode())
                            if "text" in data:
                                console.print(data["text"], end="")
                                full_response += data["text"]
                        except json.JSONDecodeError:
                            continue
                return full_response
        except Exception as e:
            console.print(f"error: {str(e)}", style="red")
        return ""

    def _send_request(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        try:
            response = requests.post(
                self.url,
                headers=self.headers,
                json=payload
            )
            
            if response.status_code == 200:
                return response.json()
            
            error_msg = {
                401: "invalid api key",
                403: "forbidden - check your api key",
                429: "too many requests",
                500: "server error"
            }.get(response.status_code, f"request failed: {response.text}")
            return {"error": error_msg, "status": response.status_code}
            
        except requests.RequestException as e:
            return {"error": f"network error: {str(e)}", "status": 0}
        except Exception as e:
            return {"error": f"unexpected error: {str(e)}", "status": -1} 