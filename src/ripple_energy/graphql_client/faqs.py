from typing import List

from .base_model import BaseModel


class Faqs(BaseModel):
    faqs: List["FaqsFaqs"]


class FaqsFaqs(BaseModel):
    id: str
    question: str
    answer: str
    tags: List["FaqsFaqsTags"]


class FaqsFaqsTags(BaseModel):
    id: str
    name: str


Faqs.model_rebuild()
FaqsFaqs.model_rebuild()
