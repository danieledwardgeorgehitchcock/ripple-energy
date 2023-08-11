"""Python client for fetching data from Ripple Energy API."""
from requests import post
from pygqlmap.network import GQLResponse
import graphql.queries as gql_query
import graphql.mutations as gql_mutation
import graphql.gql_types as gql_type

class RippleEnergy():
    # init method or constructor
    def __init__(self, email: str = None, password: str = None):
        if email is None:
            return #Replace with exception
        if password is None:
            return #Replace with exception
        if not hasattr(self, "token"):
            self.token = self.token_auth(email = email, password = password)

    def request(self, query = None, url: str = None, headers: dict[str, str] = {}, timeout: int = None):
        """Create a request to the Ripple Energy API, parse and validate response."""
        if query is None:
            return #Replace with exception
        if url is None:
            url = "https://rippleenergy.com/graphql"
        if not hasattr(headers, "Content-Type"):
            headers.update({"Content-Type": "application/json"})
        if hasattr(self, "token") and not hasattr(headers, "Authorization"):
            headers.update({"Authorization": self.token})
        if timeout is None:
            timeout = 10

        response = post(url = url, timeout = timeout, headers = headers, json = {"query": query.export_gql_source})

        gql_response = GQLResponse(response)

        gql_response.print_msg_out()

        gql_response.map_gqldata_to_obj(query.type)

        data = gql_response.result_obj

        return data

    def token_auth(self, email: str = None, password: str = None):
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

        data = self.request(query = mutation)

        token = f"JWT {data.token}"

        return token

    def auth_login_session(self, email: str = None, password: str = None):
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

        data = self.request(query = mutation)

        return data

    def auth_logout_session(self):
        """Destroy login session with Ripple Energy API"""
        mutation = gql_mutation.authLogoutSession()
        mutation.name = "AuthLogoutSession"

        data = self.request(query = mutation)

        return data

    def me(self):
        """User information from Ripple Energy API"""
        query = gql_query.me()
        query.name = "Me"

        data = self.request(query = query)

        return data

    def version(self):
        """Version information from Ripple Energy API""" 
        query = gql_query.version()
        query.name = "Version"

        data = self.request(query = query)

        return data

    def branding(self):
        """Branding information from Ripple Energy API""" 
        query = gql_query.branding()
        query.name = "Branding"

        data = self.request(query = query)

        return data

    def products(self):
        """Products information from Ripple Energy API""" 
        query = gql_query.products()
        query.name = "Products"

        print(query)

        data = self.request(query = query)

        return data