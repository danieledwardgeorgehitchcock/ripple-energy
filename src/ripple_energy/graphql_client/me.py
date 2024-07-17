from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class Me(BaseModel):
    me: Optional["MeMe"]


class MeMe(BaseModel):
    id: str
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    email: str
    phone_number: Optional[str] = Field(alias="phoneNumber")
    is_superuser: bool = Field(alias="isSuperuser")
    is_staff: bool = Field(alias="isStaff")
    is_guest: bool = Field(alias="isGuest")
    is_active: bool = Field(alias="isActive")
    is_email_verified: bool = Field(alias="isEmailVerified")
    date_joined: Any = Field(alias="dateJoined")
    groups: List["MeMeGroups"]
    referred: List["MeMeReferred"]
    payments: Optional[List["MeMePayments"]]
    direct_debit: Optional["MeMeDirectDebit"] = Field(alias="directDebit")
    member: Optional["MeMeMember"]


class MeMeGroups(BaseModel):
    id: str
    name: str
    permissions: List["MeMeGroupsPermissions"]


class MeMeGroupsPermissions(BaseModel):
    id: str
    codename: str
    name: str


class MeMeReferred(BaseModel):
    id: str
    user: "MeMeReferredUser"
    recommended_by: Optional["MeMeReferredRecommendedBy"] = Field(alias="recommendedBy")


class MeMeReferredUser(BaseModel):
    id: str
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    date_joined: Any = Field(alias="dateJoined")
    member: Optional["MeMeReferredUserMember"]


class MeMeReferredUserMember(BaseModel):
    id: str


class MeMeReferredRecommendedBy(BaseModel):
    id: str


class MeMePayments(BaseModel):
    id: str
    paid: bool
    amount: int


class MeMeDirectDebit(BaseModel):
    id: str
    account_name: str = Field(alias="accountName")
    account_sort_code: Optional[str] = Field(alias="accountSortCode")
    account_number: Optional[str] = Field(alias="accountNumber")
    payment_day: int = Field(alias="paymentDay")


class MeMeMember(BaseModel):
    id: str
    registration_completed: bool = Field(alias="registrationCompleted")


Me.model_rebuild()
MeMe.model_rebuild()
MeMeGroups.model_rebuild()
MeMeGroupsPermissions.model_rebuild()
MeMeReferred.model_rebuild()
MeMeReferredUser.model_rebuild()
MeMeReferredUserMember.model_rebuild()
MeMeReferredRecommendedBy.model_rebuild()
MeMePayments.model_rebuild()
MeMeDirectDebit.model_rebuild()
MeMeMember.model_rebuild()
