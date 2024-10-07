
def success_response(data=None, message="Success", code=200):
    return {
        "code": code,
        "message": message,
        "data": data
    }

def error_response(code=400, message="An error occurred", errors=None):
    return {
        "code": code,
        "message": message,
        "errors": errors or []
    }