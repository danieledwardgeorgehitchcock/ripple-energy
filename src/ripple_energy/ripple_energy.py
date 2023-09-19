from __future__ import annotations
import logging
from datetime import datetime
from pydantic import validate_call
from graphql_client.client import Client
from constants import RIPPLE_GRAPH_URL
from helpers import generate_jwt_header
from exceptions import (RippleEnergyMissingAuthorizationHeaderException,
                        RippleEnergyDeauthenticationException,
                        RippleEnergyTokenDestroyException,
                        RippleEnergyAuthenticationException,
                        RippleEnergyTokenExpiredException,
                        RippleEnergyCoOpCodeMissingException
                        )
from models import (RippleEnergyCredentialAuth,
                    RippleEnergyTokenAuth
                    )

logging.getLogger(__name__)


class RippleEnergy:
    @validate_call
    def __init__(self,
                 auth: RippleEnergyCredentialAuth | RippleEnergyTokenAuth,
                 auto_auth_deauth: bool = True
                 ):
        """Initialise Ripple Energy object"""
        if isinstance(auth, RippleEnergyCredentialAuth):
            self.auth_method = "credential"
            self.email = auth.email
            self.password = auth.password
            self.headers: dict[str, str] = {}
        elif isinstance(auth, RippleEnergyTokenAuth):
            self.auth_method = "token"
            self.token = auth.token
            self.headers = generate_jwt_header(auth.token)

        self.auto_auth_deauth = auto_auth_deauth
        self.client = Client(url=RIPPLE_GRAPH_URL, headers=self.headers)

    async def __aenter__(self) -> RippleEnergy:
        """Ripple Energy asyncronous enter"""
        if self.auto_auth_deauth:
            if self.auth_method == "credential":
                await self.authenticate()
        elif self.auth_method == "token":
            await self.verify_token()

        return self

    async def __aexit__(self,
                        *args
                        ) -> None:
        """Ripple Energy asyncronous exit"""
        if self.auto_auth_deauth:
            await self.deauthenticate()

    def check_expiry(function):
        """Ripple Energy decorator function to check JWT token expiry"""
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
        input = {"email": self.email,
                 "password": self.password}

        data = await self.client.authenticate(input=input)

        if not data.token:
            raise RippleEnergyAuthenticationException

        logging.info(f"Authentication successful. Token: {data.token}")

        self.token = data.token
        self.headers.update(generate_jwt_header(data.token))

        await self.verify_token()

        return data

    async def deauthenticate(self):
        """De-authenticate with Ripple Energy and destroy JWT token"""
        if not self.headers.get("Authorization"):
            raise RippleEnergyMissingAuthorizationHeaderException

        data = await self.client.deauthenticate()

        if not data.auth_logout_session.logout_successful:
            raise RippleEnergyDeauthenticationException
        if not data.delete_token_cookie.deleted:
            raise RippleEnergyTokenDestroyException

        self.token = None
        self.token_expires = datetime.now()
        self.headers.pop("Authorization")

        return data

    async def refresh_token(self):
        """Ripple Energy refresh JWT token"""
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
        """Ripple Energy co-op"""
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
        if not tag:
            tag = ""
            logging.info("Querying all FAQs")
        else:
            logging.info(f"Querying FAQs for tag: {tag}")

        data = await self.client.faqs(tag=tag)

        return data

    @check_expiry
    async def wind_farm_generation(self):
        """Ripple Energy wind farm generation"""
        data = await self.client.wind_farm_generation()
        return data

    @check_expiry
    async def monthly_savings(self, date: datetime | None = None):
        """Ripple Energy monthly savings"""
        if not date:
            date = datetime.now()

        date_str: str = date.strftime("%Y-%m-%d")

        logging.info(f"Querying monthly savings for date: {date_str}")

        data = await self.client.monthly_savings(date=date_str)

        return data

    @check_expiry
    async def cumulative_savings(self):
        """Ripple Energy cumulative savings"""
        data = await self.client.cumulative_savings()
        return data

    @check_expiry
    async def coop_timeline_progression(self, coop_code: str | None = None):
        """Ripple Energy co-op timeline progression"""
        if not coop_code:
            raise RippleEnergyCoOpCodeMissingException
        data = await self.client.coop_timeline_progression(coop_code)
        return data

    @check_expiry
    async def consumption(self):
        """Ripple Energy estimated household consumption"""
        data = await self.client.consumption()
        return data
