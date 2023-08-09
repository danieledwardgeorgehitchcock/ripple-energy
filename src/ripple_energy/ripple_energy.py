"""Python client for fetching data from Ripple Energy API."""
import requests
from pygqlmap.network import GQLResponse
from graphql.mutations import authLoginSession
from graphql.gql_types import AuthLoginSessionInputType

def auth_login_session(email: str = None, password: str = None, url_base: str = None, timeout: int = None):
    """Create a request to the Ripple Energy API, parse and validate response."""
    if email is None:
        return #Replace with exception

    if password is None:
        return #Replace with exception

    if url_base is None:
        url_base = "https://rippleenergy.com/graphql"

    if timeout is None:
        timeout = 10

    headers: dict[str, str] = {"Content-Type": "application/json"}

    mutation = authLoginSession()
    mutation.name = "AuthLoginSession"

    mutation_input = AuthLoginSessionInputType()

    mutation_input.email = email
    mutation_input.password = password

    mutation._args.input = mutation_input

    response = requests.post(url = url_base, timeout = timeout, headers = headers, json = { "query": mutation.export_gql_source })

    gql_response = GQLResponse(response)

    gql_response.print_msg_out()

    gql_response.map_gqldata_to_obj(mutation.type)

    return gql_response.result_obj