from __future__ import annotations
from graphql_client.client import Client
from constants import RIPPLE_GRAPH_URL
from exceptions import RippleEnergyEmailError, RippleEnergyPasswordError

class RippleEnergy:
    def __init__(
            self,
            email: str | None = None,
            password: str | None = None,
            client: Client | None = None,
            headers: dict[str, str] | None = None
            ):
        """Initialise Ripple object"""
        if email is None:
            raise RippleEnergyEmailError
        else:
            self.email = email
        if password is None:
            raise RippleEnergyPasswordError
        else:
            self.password = password
        if headers is None:
            self.headers = {}
        else:
            self.headers = headers        
        if client is None:
            self.client = Client(url = RIPPLE_GRAPH_URL, headers = self.headers)

    async def __aenter__(self) -> RippleEnergy:
        """Async enter"""
        await self.token_auth()   
        return self

    async def __aexit__(
            self,
            *args
            ) -> None:
        """Async exit"""
        self.client = None
        self.headers = None

    async def token_auth(self):
        """Authenticate with Ripple Energy and generate JWT token"""
        data = await self.client.token_auth(input = {"email": self.email, "password": self.password})
        self.headers.update({"Authorization": f"JWT {data.token}"})
        return data
    
    async def version(self):
        """Ripple Energy GraphQL API version"""
        data = await self.client.version()
        return data
    
    async def member(self):
        """Ripple Energy member data"""
        data = await self.client.member()
        return data

    async def me(self):
        """Ripple Energy user data"""
        data = await self.client.me()
        return data

    async def active_coop_status(self):
        """Ripple Energy active co-op status"""
        data = await self.client.active_coop_status()
        return data

    async def coop(self):
        """Ripple Energy co-op data"""
        data = await self.client.coop()
        return data

    async def tribe_url(self):
        """Ripple Energy Tribe URL"""
        data = await self.client.tribe_url()
        return data
    
    async def faqs(
            self,
            tag: str | None = None
            ):
        """Ripple Energy Frequently Asked Questions"""
        if tag is None:
            tag = ""
        data = await self.client.faqs(tag)
        return data