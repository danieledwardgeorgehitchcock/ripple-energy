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
    account_sort_code: str = Field(alias="accountSortCode")
    account_number: str = Field(alias="accountNumber")
    payment_day: str = Field(alias="paymentDay")


class MeMeMember(BaseModel):
    id: str
    registration_completed: bool = Field(alias="registrationCompleted")


Me.update_forward_refs()
MeMe.update_forward_refs()
MeMeGroups.update_forward_refs()
MeMeGroupsPermissions.update_forward_refs()
MeMeReferred.update_forward_refs()
MeMeReferredUser.update_forward_refs()
MeMeReferredUserMember.update_forward_refs()
MeMeReferredRecommendedBy.update_forward_refs()
MeMePayments.update_forward_refs()
MeMeDirectDebit.update_forward_refs()
MeMeMember.update_forward_refs()
