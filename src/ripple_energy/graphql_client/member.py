from typing import Optional

from .base_model import BaseModel
from .fragments import MemberFragment


class Member(BaseModel):
    member: Optional["MemberMember"]


class MemberMember(MemberFragment):
    pass


Member.model_rebuild()
MemberMember.model_rebuild()
