
def success_response(data=None, message="Success", code=200):
    """
    Generate a standardized success response.

    This helper function creates a structured JSON response for successful operations. 
    It includes a customizable status code, message, and optional data.

    Args:
        data (any, optional): The data payload for the response, default is None.
        message (str, optional): A custom success message, default is "Success".
        code (int, optional): The HTTP status code for the response, default is 200.

    Returns:
        dict: A dictionary containing the status code, message, and data.
    """

    return {
        "code": code,
        "message": message,
        "data": data
    }

def error_response(code=400, message="An error occurred", errors=None):
    """
    Generate a standardized error response.

    This helper function creates a structured JSON response for failed operations.
    It includes a customizable status code, error message, and a list of error details.

    Args:
        code (int, optional): The HTTP status code for the response, default is 400.
        message (str, optional): A custom error message, default is "An error occurred".
        errors (list, optional): A list of specific error details, default is an empty list.

    Returns:
        dict: A dictionary containing the status code, message, and error details.
    """
    return {
        "code": code,
        "message": message,
        "errors": errors or []
    }