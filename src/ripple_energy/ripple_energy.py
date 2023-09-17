from __future__ import annotations
import logging
from datetime import datetime
from graphql_client.client import Client
from constants import RIPPLE_GRAPH_URL
from helpers import generate_jwt_header
from exceptions import (RippleEnergyEmailException,
                        RippleEnergyPasswordException,
                        RippleEnergyMissingCredentialsOrTokenException,
                        RippleEnergyMissingAuthorizationHeaderException,
                        RippleEnergyDeauthenticationException,
                        RippleEnergyTokenDestroyException,
                        RippleEnergyAuthenticationException,
                        RippleEnergyMissingTokenException,
                        RippleEnergyTokenExpiredException
                        )

logging.getLogger(__name__)


class RippleEnergy:
    def __init__(self,
                 email: str | None = None,
                 password: str | None = None,
                 token: str | None = None,
                 client: Client | None = None,
                 headers: dict[str, str] = {},
                 auto_auth_deauth: bool = True
                 ):
        """Initialise Ripple object"""
        self.email = email
        self.password = password
        self.headers = headers
        self.token = token
        self.auto_auth_deauth = auto_auth_deauth
        if not email and not password and not token:
            raise RippleEnergyMissingCredentialsOrTokenException
        if token:
            self.headers.update(generate_jwt_header(token))
        if not client:
            self.client = Client(url=RIPPLE_GRAPH_URL, headers=self.headers)

    async def __aenter__(self) -> RippleEnergy:
        """Async enter"""
        if self.auto_auth_deauth:
            if not self.token:
                await self.authenticate()
            else:
                await self.verify_token()
            if self.token_expires < datetime.now():
                await self.refresh_token()

        return self

    async def __aexit__(self,
                        *args
                        ) -> None:
        """Async exit"""
        if self.auto_auth_deauth:
            await self.deauthenticate()

    def check_expiry(function):
        async def wrapper(*args, **kwargs):
            if args[0].token_expires < datetime.now():
                if args[0].auto_auth_deauth:
                    await args[0].refresh_token()
                else:
                    raise RippleEnergyTokenExpiredException

            return await function(*args, **kwargs)

        return wrapper

    async def authenticate(self):
        """Authenticate with Ripple Energy and generate JWT token"""
        if not self.email:
            raise RippleEnergyEmailException
        if not self.password:
            raise RippleEnergyPasswordException

        data = await self.client.authenticate(input={"email": self.email,
                                                     "password": self.password}
                                              )

        if not data.token:
            raise RippleEnergyAuthenticationException

        logging.info(f"Authentication successful. Token: {data.token}")

        self.token = data.token
        self.headers.update(generate_jwt_header(data.token))

        await self.verify_token()

        return data

    async def deauthenticate(self):
        """De-Authenticate with Ripple Energy and destroy JWT token"""
        if not self.headers.get("Authorization"):
            raise RippleEnergyMissingAuthorizationHeaderException

        data = await self.client.deauthenticate()

        if not data.auth_logout_session.logout_successful:
            raise RippleEnergyDeauthenticationException
        if not data.delete_token_cookie.deleted:
            raise RippleEnergyTokenDestroyException

        self.token = None
        self.headers.pop("Authorization")

        return data

    async def refresh_token(self):
        """Ripple Energy refresh JWT token"""
        if not self.token:
            raise RippleEnergyMissingTokenException

        data = await self.client.refresh_token(self.token)

        if not data.token:
            raise RippleEnergyAuthenticationException

        logging.info(f"Token refresh successful. Token: {data.token}")

        self.token = data.token
        self.headers.update(generate_jwt_header(data.token))
        self.token_expires = datetime.fromtimestamp(data.refresh_expires_in)

        return data

    async def verify_token(self):
        """Ripple Energy verify JWT token"""
        if not self.token:
            raise RippleEnergyMissingTokenException

        data = await self.client.verify_token(self.token)

        self.token_expires = datetime.fromtimestamp(data.payload["exp"])

        logging.info(f"Token verified. Expires: {self.token_expires}")

        return data

    @check_expiry
    async def version(self):
        """Ripple Energy GraphQL API version"""
        data = await self.client.version()
        return data

    @check_expiry
    async def member(self):
        """Ripple Energy member data"""
        data = await self.client.member()
        return data

    @check_expiry
    async def me(self):
        """Ripple Energy user data"""
        data = await self.client.me()
        return data

    @check_expiry
    async def active_coop_status(self):
        """Ripple Energy active co-op status"""
        data = await self.client.active_coop_status()
        return data

    @check_expiry
    async def coop(self):
        """Ripple Energy co-op data"""
        data = await self.client.coop()
        return data

    @check_expiry
    async def tribe_url(self):
        """Ripple Energy Tribe URL"""
        data = await self.client.tribe_url()
        return data

    @check_expiry
    async def faqs(self, tag: str | None = None):
        """Ripple Energy Frequently Asked Questions"""
        if tag is None:
            tag = ""
        data = await self.client.faqs(tag)
        return data

