from pydantic import BaseModel


class RippleEnergyCredentialAuth(BaseModel):
    email: str
    password: str


class RippleEnergyTokenAuth(BaseModel):
    token: str
