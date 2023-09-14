from __future__ import annotations
from graphql_client.client import Client

class RippleEnergy:
    def __init__(self, email: str = None, password: str = None):
        """Initialise Ripple object"""
        if email is None:
            return #Replace with exception
        else:
            self.email = email
        if password is None:
            return #Replace with exception
        else:
            self.password = password

    async def token_auth(self):
        """Authenticate with Ripple and generate JWT token"""
        data = await self.client.token_auth(input = {"email": self.email, "password": self.password})
        self.headers.update({"Authorization": f"JWT {data.token}"})
        return data
    
    async def version(self):
        """Ripple GraphQL API version"""
        data = await self.client.version()
        return data
    
    async def get_member(self):
        """Get member data"""
        data = await self.client.get_member()
        return data
    
    async def __aenter__(self, client: Client | None = None, headers: dict[str, str] = None) -> RippleEnergy:
        """Async enter"""
        if headers is None:
            self.headers = {}
        else:
            self.headers = headers        
        if client is None:
            self.client = Client(url = "https://rippleenergy.com/graphql", headers = self.headers)

        await self.token_auth()
        
        return self

    async def __aexit__(self, *args) -> None:
        """Async exit"""
        self.client = None
        self.headers = None