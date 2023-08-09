"""Python client for fetching data from Ripple Energy API."""
from requests import post
from pygqlmap.network import GQLResponse
import graphql.queries as gql_query
import graphql.mutations as gql_mutation
import graphql.gql_types as gql_type

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

def token_auth(email: str = None, password: str = None):
    """Generate authentication token with Ripple Energy API"""
    if email is None:
        return #Replace with exception
    if password is None:
        return #Replace with exception

    mutation = gql_mutation.tokenAuth()
    mutation.name = "TokenAuth"

    mutation_input = gql_type.TokenAuthenticationInput()
    mutation_input.email = email
    mutation_input.password = password

    mutation._args.input = mutation_input

    data = request(query = mutation)

    return data

def auth_login_session(email: str = None, password: str = None):
    """Create login session with Ripple Energy API"""
    if email is None:
        return #Replace with exception
    if password is None:
        return #Replace with exception

    mutation = gql_mutation.authLoginSession()
    mutation.name = "AuthLoginSession"

    mutation_input = gql_type.AuthLoginSessionInputType()
    mutation_input.email = email
    mutation_input.password = password

    mutation._args.input = mutation_input

    data = request(query = mutation)

    return data

def auth_logout_session():
    """Destroy login session with Ripple Energy API"""
    mutation = gql_mutation.authLogoutSession()
    mutation.name = "AuthLogoutSession"

    data = request(query = mutation)

    return data

def me(token: str = None):
    """User information from Ripple Energy API"""
    if token is None:
        return #Replace with exception
    
    query = gql_query.me()
    query.name = "Me"

    token = f"JWT {token}" #Not sure if this is correct but, mimmicking website

    data = request(query = query, headers = {"Authorization": token})

    return data

def version():
    """Version information from Ripple Energy API""" 
    query = gql_query.version()
    query.name = "Version"

    data = request(query = query)

    return data

def branding():
    """Branding information from Ripple Energy API""" 
    query = gql_query.branding()
    query.name = "Branding"

    data = request(query = query)

    return data