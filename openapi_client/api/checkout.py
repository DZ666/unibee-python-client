# coding: utf-8

"""
    UniBee API

    UniBee Merchant API for checkout and subscription management

    The version of the OpenAPI document: 2.0.0
"""

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from openapi_client.api_client import ApiClient, RequestSerialized
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType


class Checkout:
    """UniBee Checkout API for managing checkout sessions and links.
    
    This class provides methods to create, manage, and retrieve checkout
    configurations for subscription purchases.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def checkout_new_post(
        self,
        plan_id: Annotated[int, Field(description="The plan ID to create checkout for")],
        success_url: Annotated[Optional[str], Field(description="URL to redirect after successful payment")] = None,
        cancel_url: Annotated[Optional[str], Field(description="URL to redirect if payment is cancelled")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Dict[str, Any]:
        """Create a new checkout session.
        
        Creates a new checkout configuration for a specific plan.
        
        :param plan_id: The plan ID to create checkout for (required)
        :param success_url: URL to redirect after successful payment
        :param cancel_url: URL to redirect if payment is cancelled
        :param _request_timeout: timeout setting for this request
        :return: Checkout session details
        """
        _param = self._checkout_new_post_serialize(
            plan_id=plan_id,
            success_url=success_url,
            cancel_url=cancel_url,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _checkout_new_post_serialize(
        self,
        plan_id,
        success_url,
        cancel_url,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None
        _collection_formats: Dict[str, str] = {}
        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[Dict[str, Any]] = {}

        # Build request body
        _body_params['planId'] = plan_id
        if success_url is not None:
            _body_params['successUrl'] = success_url
        if cancel_url is not None:
            _body_params['cancelUrl'] = cancel_url

        # Set headers
        _header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _header_params['Content-Type'] = 'application/json'

        # Authentication
        _auth_settings: List[str] = ['Authorization']

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/merchant/checkout/new',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )

    @validate_call
    def checkout_list_get(
        self,
        page: Annotated[Optional[int], Field(description="Page number")] = None,
        count: Annotated[Optional[int], Field(description="Number of items per page")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Dict[str, Any]:
        """Get list of checkout configurations.
        
        :param page: Page number
        :param count: Number of items per page
        :return: List of checkout configurations
        """
        _param = self._checkout_list_get_serialize(
            page=page,
            count=count,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _checkout_list_get_serialize(
        self,
        page,
        count,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None
        _collection_formats: Dict[str, str] = {}
        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # Query parameters
        if page is not None:
            _query_params.append(('page', page))
        if count is not None:
            _query_params.append(('count', count))

        # Set headers
        _header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # Authentication
        _auth_settings: List[str] = ['Authorization']

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/merchant/checkout/list',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )

    @validate_call
    def checkout_detail_get(
        self,
        checkout_id: Annotated[str, Field(description="Checkout ID")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Dict[str, Any]:
        """Get checkout detail.
        
        :param checkout_id: Checkout ID (required)
        :return: Checkout details
        """
        _param = self._checkout_detail_get_serialize(
            checkout_id=checkout_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _checkout_detail_get_serialize(
        self,
        checkout_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None
        _collection_formats: Dict[str, str] = {}
        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # Query parameters
        _query_params.append(('checkoutId', checkout_id))

        # Set headers
        _header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # Authentication
        _auth_settings: List[str] = ['Authorization']

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/merchant/checkout/detail',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )

    @validate_call
    def checkout_archive_post(
        self,
        checkout_id: Annotated[str, Field(description="Checkout ID to archive")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Dict[str, Any]:
        """Archive a checkout configuration.
        
        :param checkout_id: Checkout ID to archive (required)
        :return: Archive result
        """
        _param = self._checkout_archive_post_serialize(
            checkout_id=checkout_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _checkout_archive_post_serialize(
        self,
        checkout_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None
        _collection_formats: Dict[str, str] = {}
        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[Dict[str, Any]] = {}

        # Build request body
        _body_params['checkoutId'] = checkout_id

        # Set headers
        _header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _header_params['Content-Type'] = 'application/json'

        # Authentication
        _auth_settings: List[str] = ['Authorization']

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/merchant/checkout/archive',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )
