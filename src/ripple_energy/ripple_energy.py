"""Python client for fetching data from Ripple Energy API."""
from requests import post
from pygqlmap.network import GQLResponse
from graphql.mutations import *
from graphql.gql_types import *

def request(query = None, url: str = None, headers: dict[str, str] = None, timeout: int = None):
    """Create a request to the Ripple Energy API, parse and validate response."""
    if query is None:
        return #Replace with exception
    if url is None:
        url = "https://rippleenergy.com/graphql"
    if headers is None:
        headers = {"Content-Type": "application/json"}
    if "Content-Type" not in headers:
        headers.update({"Content-Type": "application/json"})
    if timeout is None:
        timeout = 10

    response = post(url = url, timeout = timeout, headers = headers, json = { "query": query.export_gql_source })

    gql_response = GQLResponse(response)

    gql_response.print_msg_out()

    gql_response.map_gqldata_to_obj(query.type)

    data = gql_response.result_obj

    return data

def auth_login_session(email: str = None, password: str = None):
    """Authenticate with Ripple Energy API"""
    if email is None:
        return #Replace with exception
    if password is None:
        return #Replace with exception

    mutation = authLoginSession()
    mutation.name = "AuthLoginSession"

    mutation_input = AuthLoginSessionInputType()
    mutation_input.email = email
    mutation_input.password = password

    mutation._args.input = mutation_input

    data = request(query = mutation)

    return data
