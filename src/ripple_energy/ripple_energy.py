"""Python client for fetching data from Ripple Energy API."""
import requests
from pygqlmap.network import GQLResponse
from graphql.mutations import authLoginSession
from graphql.gql_types import AuthLoginSessionInputType

def request(api_key: str = None, url_base: str = None, timeout: int = None):
    """Create a request to the Ripple Energy API, parse and validate response."""
#    if api_key is None:
#        return #Replace with exception
 
    if url_base is None:
        url_base = "https://rippleenergy.com/graphql"

    if timeout is None:
        timeout = 10

    headers: dict[str, str] = {"Content-Type": "application/json"}

    mutation = authLoginSession()
    mutation.name = "AuthLoginSession"

    mutation_input = AuthLoginSessionInputType()

    mutation_input.email = "daniel.edward.george.hitchcock@gmail.com"
    mutation_input.password = "H1tchc0ck"

    mutation._args.input = mutation_input

    response = requests.post(url = url_base, timeout = timeout, headers = headers, json = { "query": mutation.export_gql_source })

    gql_response = GQLResponse(response)

    gql_response.print_msg_out()

    gql_response.map_gqldata_to_obj(mutation.type)

    return gql_response.result_obj