from typing import Optional

from .base_model import BaseModel
from .fragments import MemberFragment


class GetMember(BaseModel):
    member: Optional["GetMemberMember"]


class GetMemberMember(MemberFragment):
    pass


GetMember.update_forward_refs()
GetMemberMember.update_forward_refs()
