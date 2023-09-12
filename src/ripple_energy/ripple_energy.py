from graphql_client.client import Client

class RippleEnergy():
    # init method or constructor
    def __init__(self, token: str = None):
        headers: dict[str, str] = {}
        if token is not None:
            headers.update({"Authorization": f"JWT {token}"})
        self.client = Client(url = "https://rippleenergy.com/graphql", headers = headers)

    async def token_auth(self, email: str = None, password: str = None):
        if email is None:
            return #Replace with exception
        else:
            self.email = email
        if password is None:
            return #Replace with exception
        else:
            self.password = password

        data = await self.client.token_auth(input = {"email": self.email, "password": self.password})
        return data
    
    async def version(self):
        data = await self.client.version()
        return data
    
    async def get_member(self):
        data = await self.client.get_member()
        return data

#    def request(self, query = None, url: str = None, headers: dict[str, str] = {}, timeout: int = None):
#        """Create a request to the Ripple Energy API, parse and validate response."""
#        if query is None:
#            return #Replace with exception
#        if url is None:
#            url = "https://rippleenergy.com/graphql"
#        if not hasattr(headers, "Content-Type"):
#            headers.update({"Content-Type": "application/json"})
#        if hasattr(self, "token") and not hasattr(headers, "Authorization"):
#            headers.update({"Authorization": self.token})
#        if timeout is None:
#            timeout = 10

#        response = post(url = url, timeout = timeout, headers = headers, json = {"query": query.export_gql_source})

#        gql_response = GQLResponse(response)

#        gql_response.print_msg_out()

#        gql_response.map_gqldata_to_obj(query.type)

#        data = gql_response.result_obj

#        return data

#    def token_auth(self, email: str = None, password: str = None):
#        """Generate authentication token with Ripple Energy API"""
#        if email is None:
#            return #Replace with exception
#        if password is None:
#            return #Replace with exception

#        mutation = gql_mutation.tokenAuth()
#        mutation.name = "TokenAuth"

#        mutation_input = gql_type.TokenAuthenticationInput()
#        mutation_input.email = email
#        mutation_input.password = password

#        mutation._args.input = mutation_input

#        data = self.request(query = mutation)

#        token = f"JWT {data.token}"

#        return token