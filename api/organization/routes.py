from typing import Optional
from fastapi import APIRouter

from models import Organization
from .schemas import OrganizationSchema

rt_organizations = APIRouter(
    prefix="/organizations",
    tags=["organizations"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@rt_organizations.get("/", response_model=Optional[list[OrganizationSchema]] or Optional[OrganizationSchema], response_model_exclude={"id"})
async def get_organizations(name: str = None, edrpou_code: str = None):
    if all((name, edrpou_code)):
        return {"error": "Choose one between organization_id, edrpou_code"}
    if name:
        organizations = await Organization.get_all_organizations_via_name(name=name)
    if edrpou_code:
        organizations = await Organization.get_all_organizations_via_edrpou_code(code=edrpou_code)
    else:
        organizations = await Organization.get_organizations()
    return organizations if organizations else []
