from typing import Optional

from fastapi import APIRouter
from fastapi_pagination import Page, paginate

from orgs.models import Organization

from .schemas import OrganizationSchema

rt_organizations = APIRouter(
    prefix="/orgs",
    tags=["orgs"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@rt_organizations.get(
    "/",
    response_model=Page[
        Optional[list[OrganizationSchema]] or Optional[OrganizationSchema]
    ],
    response_model_exclude={"id"},
)
async def get_organizations(name: str = None, edrpou_code: str = None):
    if all((name, edrpou_code)):
        return {"error": "Choose one between organization_id, edrpou_code"}
    if edrpou_code:
        organization = await Organization.get_all_organizations_via_edrpou_code(
            code=edrpou_code
        )
    else:
        organization = await Organization.get_organizations()
    return paginate(organization)


@rt_organizations.get(
    "/<int:orgazation_id>",
    response_model=Optional[OrganizationSchema],
    response_model_exclude={"id"},
)
async def get_organization(edrpou_code: str = None, organization_id: int = None):
    if organization_id:
        organization = await Organization.get_all_organizations_via_id(
            org_id=organization_id
        )
        return organization


@rt_organizations.get(
    "/<str:edrpou_code>",
    response_model=Optional[OrganizationSchema],
    response_model_exclude={"id"},
)
async def get_organization(edrpou_code: str = None, organization_id: int = None):
    if edrpou_code:
        organization = await Organization.get_all_organizations_via_edrpou_code(
            code=edrpou_code
        )
        return organization
