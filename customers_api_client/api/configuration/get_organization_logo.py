from typing import Any, Dict, List, Optional, Union, cast

import httpx
from attr import asdict

from ...client import AuthenticatedClient, Client
from ...types import Response




def _get_kwargs(
    *,
    client: Client,
    x_organization: str,

) -> Dict[str, Any]:
    url = "{}/configuration/logo".format(
        client.base_url)

    headers: Dict[str, Any] = client.get_headers()

    headers["x-organization"] = x_organization


    

    

    return {
        "url": url,
        "headers": headers,
        "cookies": client.get_cookies(),
        "timeout": client.get_timeout(),
    }




def _build_response(*, response: httpx.Response) -> Response[None]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    *,
    client: Client,
    x_organization: str,

) -> Response[None]:
    kwargs = _get_kwargs(
        client=client,
x_organization=x_organization,

    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    x_organization: str,

) -> Response[None]:
    kwargs = _get_kwargs(
        client=client,
x_organization=x_organization,

    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(
            **kwargs
        )

    return _build_response(response=response)

