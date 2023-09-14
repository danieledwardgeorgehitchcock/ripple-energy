from __future__ import annotations
from graphql_client.client import Client
from constants import RIPPLE_GRAPH_URL

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
    
    async def member(self):
        """Ripple member data"""
        data = await self.client.member()
        return data

    async def me(self):
        """Ripple user data"""
        data = await self.client.me()
        return data

    async def active_coop_status(self):
        """Ripple active co-op status"""
        data = await self.client.active_coop_status()
        return data

    async def coop(self):
        """Ripple co-op data"""
        data = await self.client.coop()
        return data

    async def __aenter__(self, client: Client | None = None, headers: dict[str, str] = None) -> RippleEnergy:
        """Async enter"""
        if headers is None:
            self.headers = {}
        else:
            self.headers = headers        
        if client is None:
            self.client = Client(url = RIPPLE_GRAPH_URL, headers = self.headers)
        await self.token_auth()   
        return self

    async def __aexit__(self, *args) -> None:
        """Async exit"""
        self.client = None
        self.headers = None