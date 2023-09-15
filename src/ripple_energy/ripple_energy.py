from __future__ import annotations
from graphql_client.client import Client
from constants import RIPPLE_GRAPH_URL
from helpers import generate_jwt_header
from exceptions import (RippleEnergyEmailException,
                        RippleEnergyPasswordException,
                        RippleEnergyMissingCredentialsOrTokenException,
                        RippleEnergyMissingAuthorizationHeaderException,
                        RippleEnergyAuthenticationException,
                        RippleEnergyDeauthenticationException,
                        RippleEnergyTokenDestroyException)

class RippleEnergy:
    def __init__(
            self,
            email: str | None = None,
            password: str | None = None,
            token: str | None = None,
            client: Client | None = None,
            headers: dict[str, str] = {}
            ):
        """Initialise Ripple object"""
        self.headers = headers
        if not email and not password and not token:
            raise RippleEnergyMissingCredentialsOrTokenException      
        if email:
            self.email = email
        if password:
            self.password = password           
        if token:
            self.headers.update(generate_jwt_header(token))
        if not client:
            self.client = Client(url = RIPPLE_GRAPH_URL, headers = self.headers)

    async def __aenter__(self) -> RippleEnergy:
        """Async enter"""
        await self.authenticate()   
        return self

    async def __aexit__(
            self,
            *args
            ) -> None:
        """Async exit"""
        await self.deauthenticate()
        self.client = None

    async def authenticate(self):
        """Authenticate with Ripple Energy and generate JWT token"""
        if not self.email:
            raise RippleEnergyEmailException
        if not self.password:
            raise RippleEnergyPasswordException

        data = await self.client.authenticate(input = {"email": self.email, "password": self.password})

        if not data.token:
            raise RippleEnergyAuthenticationException
        
        self.headers.update(generate_jwt_header(data.token))

        return data

    async def deauthenticate(self):
        """De-Authenticate with Ripple Energy and destroy Ripple Energy JWT token"""
        if not self.headers.get("Authorization"):
            raise RippleEnergyMissingAuthorizationHeaderException

        data = await self.client.deauthenticate()

        if not data.auth_logout_session.logout_successful:
            raise RippleEnergyDeauthenticationException
        if not data.delete_token_cookie.deleted:
            raise RippleEnergyTokenDestroyException
        
        self.headers.pop("Authorization")

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
