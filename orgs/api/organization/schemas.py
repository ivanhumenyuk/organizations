from typing import Optional

from pydantic import BaseModel


class OrganizationSchema(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    edrpou_code: str = None

