from typing import Any, Dict, List, Optional, Union, cast

import httpx
from attr import asdict

from ...client import AuthenticatedClient, Client
from ...types import Response

from typing import Dict
from ...models.create_address import CreateAddress
from ...types import UNSET, Unset
from typing import Union
from typing import cast
from ...models.representative import Representative



def _get_kwargs(
    *,
    client: Client,
    customer_id: str,
    representative_id: str,
    json_body: CreateAddress,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: str,

) -> Dict[str, Any]:
    url = "{}/customers/{customerID}/representatives/{representativeID}/address".format(
        client.base_url,customerID=customer_id,representativeID=representative_id)

    headers: Dict[str, Any] = client.get_headers()

    if x_request_id is not UNSET:
        headers["x-request-id"] = x_request_id
    headers["x-organization"] = x_organization


    

    json_json_body = json_body.to_dict()



    return {
        "url": url,
        "headers": headers,
        "cookies": client.get_cookies(),
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Representative]:
    if response.status_code == 200:
        response_200 = Representative.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Representative]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    customer_id: str,
    representative_id: str,
    json_body: CreateAddress,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: str,

) -> Response[Representative]:
    kwargs = _get_kwargs(
        client=client,
customer_id=customer_id,
representative_id=representative_id,
json_body=json_body,
x_request_id=x_request_id,
x_organization=x_organization,

    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    *,
    client: Client,
    customer_id: str,
    representative_id: str,
    json_body: CreateAddress,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: str,

) -> Optional[Representative]:
    """ Add an address to an existing customer representative record """

    return sync_detailed(
        client=client,
customer_id=customer_id,
representative_id=representative_id,
json_body=json_body,
x_request_id=x_request_id,
x_organization=x_organization,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    customer_id: str,
    representative_id: str,
    json_body: CreateAddress,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: str,

) -> Response[Representative]:
    kwargs = _get_kwargs(
        client=client,
customer_id=customer_id,
representative_id=representative_id,
json_body=json_body,
x_request_id=x_request_id,
x_organization=x_organization,

    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    *,
    client: Client,
    customer_id: str,
    representative_id: str,
    json_body: CreateAddress,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: str,

) -> Optional[Representative]:
    """ Add an address to an existing customer representative record """

    return (await asyncio_detailed(
        client=client,
customer_id=customer_id,
representative_id=representative_id,
json_body=json_body,
x_request_id=x_request_id,
x_organization=x_organization,

    )).parsed
