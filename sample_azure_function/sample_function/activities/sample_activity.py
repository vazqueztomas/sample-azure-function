from azure.functions import func

def sample_activity_function(message: str) -> str:
    return f"Hello, {message}"