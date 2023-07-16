"""Python client for fetching data from Ripple Energy API."""
from requests import get
from models import EnergyGeneration


def request(api_key: str = None, url_base: str = None, timeout: int = None) -> EnergyGeneration:
    """Create a request to the Ripple Energy API, parse and validate response."""
    if api_key is None:
        return #Replace with exception
 
    if url_base is None:
        url_base = "https://rippleenergy.com/rest/member_data"

    if timeout is None:
        timeout = 10

    url: str = f"{url_base}/{api_key}"

    response = get(url, timeout = timeout).json()

    data = EnergyGeneration(**response)

    return data