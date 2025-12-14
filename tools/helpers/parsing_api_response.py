from pydantic import BaseModel
import httpx

def parse_api_response(model: type[BaseModel], response: httpx.Response) -> BaseModel:
    """
    A universal function for parsing an API JSON response into a Pydantic model.

    Args:
        model: The Pydantic model, e.g., CreateUserResponseSchema
        response: A Response object from requests or a similar object that has a .text attribute

    Returns:
        An instance of the Pydantic model
    """
    return model.model_validate_json(response.text)