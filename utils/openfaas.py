import requests

INVOKE_FUNCTION = "/function/"


def invoke_function(
    host: str, function_name: str, body: Dict[str, Any]
) -> Dict[str, Any]:
    """Invoking function synchronously, will block until function completes and returns"""
    url = host + INVOKE_FUNCTION + function_name
    response = requests.post(url, body)
    if response.ok:
        return response.json()
    else:
        return ""
