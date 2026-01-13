# coding: utf-8

"""
    UniBee API

    UniBee Merchant API for discount code management

    The version of the OpenAPI document: 2.0.0
"""

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from openapi_client.api_client import ApiClient, RequestSerialized
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType


class Discount:
    """UniBee Discount API for managing discount codes.
    
    This class provides methods to create, manage, and retrieve discount codes
    for subscription plans.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def discount_new_post(
        self,
        code: Annotated[str, Field(description="Discount code string")],
        name: Annotated[str, Field(description="Discount code name")],
        billing_type: Annotated[int, Field(description="Billing type: 1-one-time, 2-recurring")],
        discount_type: Annotated[int, Field(description="Discount type: 1-percentage, 2-fixed amount")],
        discount_amount: Annotated[Optional[int], Field(description="Discount amount in cents (for fixed)")] = None,
        discount_percentage: Annotated[Optional[int], Field(description="Discount percentage (1-100)")] = None,
        currency: Annotated[Optional[str], Field(description="Currency code (e.g., USD)")] = None,
        cycle_limit: Annotated[Optional[int], Field(description="Number of billing cycles limit")] = None,
        start_time: Annotated[Optional[int], Field(description="Start time (unix timestamp)")] = None,
        end_time: Annotated[Optional[int], Field(description="End time (unix timestamp)")] = None,
        quantity: Annotated[Optional[int], Field(description="Total available quantity")] = None,
        plan_ids: Annotated[Optional[List[int]], Field(description="List of applicable plan IDs")] = None,
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
        """Create a new discount code.
        
        :param code: Discount code string (required)
        :param name: Discount code name (required)
        :param billing_type: Billing type: 1-one-time, 2-recurring (required)
        :param discount_type: Discount type: 1-percentage, 2-fixed amount (required)
        :param discount_amount: Discount amount in cents (for fixed)
        :param discount_percentage: Discount percentage (1-100)
        :param currency: Currency code
        :param cycle_limit: Number of billing cycles limit
        :param start_time: Start time (unix timestamp)
        :param end_time: End time (unix timestamp)
        :param quantity: Total available quantity
        :param plan_ids: List of applicable plan IDs
        :return: Created discount code details
        """
        _param = self._discount_new_post_serialize(
            code=code,
            name=name,
            billing_type=billing_type,
            discount_type=discount_type,
            discount_amount=discount_amount,
            discount_percentage=discount_percentage,
            currency=currency,
            cycle_limit=cycle_limit,
            start_time=start_time,
            end_time=end_time,
            quantity=quantity,
            plan_ids=plan_ids,
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

    def _discount_new_post_serialize(
        self,
        code,
        name,
        billing_type,
        discount_type,
        discount_amount,
        discount_percentage,
        currency,
        cycle_limit,
        start_time,
        end_time,
        quantity,
        plan_ids,
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
        _body_params: Dict[str, Any] = {}

        # Build request body
        _body_params['code'] = code
        _body_params['name'] = name
        _body_params['billingType'] = billing_type
        _body_params['discountType'] = discount_type
        if discount_amount is not None:
            _body_params['discountAmount'] = discount_amount
        if discount_percentage is not None:
            _body_params['discountPercentage'] = discount_percentage
        if currency is not None:
            _body_params['currency'] = currency
        if cycle_limit is not None:
            _body_params['cycleLimit'] = cycle_limit
        if start_time is not None:
            _body_params['startTime'] = start_time
        if end_time is not None:
            _body_params['endTime'] = end_time
        if quantity is not None:
            _body_params['quantity'] = quantity
        if plan_ids is not None:
            _body_params['planIds'] = plan_ids

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
            resource_path='/merchant/discount/new',
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
    def discount_list_get(
        self,
        page: Annotated[Optional[int], Field(description="Page number")] = None,
        count: Annotated[Optional[int], Field(description="Number of items per page")] = None,
        status: Annotated[Optional[int], Field(description="Status filter")] = None,
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
        """Get list of discount codes.
        
        :param page: Page number
        :param count: Number of items per page
        :param status: Status filter
        :return: List of discount codes
        """
        _param = self._discount_list_get_serialize(
            page=page,
            count=count,
            status=status,
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

    def _discount_list_get_serialize(
        self,
        page,
        count,
        status,
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
        if status is not None:
            _query_params.append(('status', status))

        # Set headers
        _header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # Authentication
        _auth_settings: List[str] = ['Authorization']

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/merchant/discount/list',
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
    def discount_detail_get(
        self,
        discount_id: Annotated[int, Field(description="Discount ID")],
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
        """Get discount code detail.
        
        :param discount_id: Discount ID (required)
        :return: Discount code details
        """
        _param = self._discount_detail_get_serialize(
            discount_id=discount_id,
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

    def _discount_detail_get_serialize(
        self,
        discount_id,
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
        _query_params.append(('id', discount_id))

        # Set headers
        _header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # Authentication
        _auth_settings: List[str] = ['Authorization']

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/merchant/discount/detail',
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
    def discount_activate_post(
        self,
        discount_id: Annotated[int, Field(description="Discount ID to activate")],
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
        """Activate a discount code.
        
        :param discount_id: Discount ID to activate (required)
        :return: Activation result
        """
        _param = self._discount_activate_post_serialize(
            discount_id=discount_id,
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

    def _discount_activate_post_serialize(
        self,
        discount_id,
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
        _body_params: Dict[str, Any] = {}

        # Build request body
        _body_params['id'] = discount_id

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
            resource_path='/merchant/discount/activate',
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
    def discount_deactivate_post(
        self,
        discount_id: Annotated[int, Field(description="Discount ID to deactivate")],
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
        """Deactivate a discount code.
        
        :param discount_id: Discount ID to deactivate (required)
        :return: Deactivation result
        """
        _param = self._discount_deactivate_post_serialize(
            discount_id=discount_id,
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

    def _discount_deactivate_post_serialize(
        self,
        discount_id,
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
        _body_params: Dict[str, Any] = {}

        # Build request body
        _body_params['id'] = discount_id

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
            resource_path='/merchant/discount/deactivate',
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
    def discount_delete_post(
        self,
        discount_id: Annotated[int, Field(description="Discount ID to delete")],
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
        """Delete a discount code.
        
        :param discount_id: Discount ID to delete (required)
        :return: Deletion result
        """
        _param = self._discount_delete_post_serialize(
            discount_id=discount_id,
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

    def _discount_delete_post_serialize(
        self,
        discount_id,
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
        _body_params: Dict[str, Any] = {}

        # Build request body
        _body_params['id'] = discount_id

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
            resource_path='/merchant/discount/delete',
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
