# coding: utf-8

"""
    UniBee API

    UniBee Merchant API for credit and promo credit management

    The version of the OpenAPI document: 2.0.0
"""

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from openapi_client.api_client import ApiClient, RequestSerialized
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType


class Credit:
    """UniBee Credit API for managing user credits and promo credits.
    
    This class provides methods to manage credit configurations,
    credit accounts, and credit transactions.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def credit_config_list_get(
        self,
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
        """Get credit configuration list.
        
        :return: List of credit configurations
        """
        _param = self._credit_config_list_get_serialize(
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

    def _credit_config_list_get_serialize(
        self,
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

        # Set headers
        _header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # Authentication
        _auth_settings: List[str] = ['Authorization']

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/merchant/credit/config_list',
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
    def credit_account_list_get(
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
        """Get credit account list.
        
        :param page: Page number
        :param count: Number of items per page
        :return: List of credit accounts
        """
        _param = self._credit_account_list_get_serialize(
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

    def _credit_account_list_get_serialize(
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
            resource_path='/merchant/credit/account_list',
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
    def credit_transaction_list_get(
        self,
        user_id: Annotated[Optional[int], Field(description="User ID filter")] = None,
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
        """Get credit transaction list.
        
        :param user_id: User ID filter
        :param page: Page number
        :param count: Number of items per page
        :return: List of credit transactions
        """
        _param = self._credit_transaction_list_get_serialize(
            user_id=user_id,
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

    def _credit_transaction_list_get_serialize(
        self,
        user_id,
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
        if user_id is not None:
            _query_params.append(('userId', user_id))
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
            resource_path='/merchant/credit/transaction_list',
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
    def credit_account_detail_get(
        self,
        user_id: Annotated[int, Field(description="User ID")],
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
        """Get credit account detail for a user.
        
        :param user_id: User ID (required)
        :return: Credit account details
        """
        _param = self._credit_account_detail_get_serialize(
            user_id=user_id,
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

    def _credit_account_detail_get_serialize(
        self,
        user_id,
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
        _query_params.append(('userId', user_id))

        # Set headers
        _header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # Authentication
        _auth_settings: List[str] = ['Authorization']

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/merchant/credit/account_detail',
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
    def promo_credit_increment_post(
        self,
        user_id: Annotated[int, Field(description="User ID")],
        amount: Annotated[int, Field(description="Amount to add (in cents)")],
        currency: Annotated[str, Field(description="Currency code")],
        description: Annotated[Optional[str], Field(description="Description")] = None,
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
        """Increment user's promo credit.
        
        :param user_id: User ID (required)
        :param amount: Amount to add in cents (required)
        :param currency: Currency code (required)
        :param description: Description
        :return: Updated promo credit details
        """
        _param = self._promo_credit_increment_post_serialize(
            user_id=user_id,
            amount=amount,
            currency=currency,
            description=description,
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

    def _promo_credit_increment_post_serialize(
        self,
        user_id,
        amount,
        currency,
        description,
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
        _body_params['userId'] = user_id
        _body_params['amount'] = amount
        _body_params['currency'] = currency
        if description is not None:
            _body_params['description'] = description

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
            resource_path='/merchant/promo_credit/increment',
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
    def promo_credit_decrement_post(
        self,
        user_id: Annotated[int, Field(description="User ID")],
        amount: Annotated[int, Field(description="Amount to subtract (in cents)")],
        currency: Annotated[str, Field(description="Currency code")],
        description: Annotated[Optional[str], Field(description="Description")] = None,
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
        """Decrement user's promo credit.
        
        :param user_id: User ID (required)
        :param amount: Amount to subtract in cents (required)
        :param currency: Currency code (required)
        :param description: Description
        :return: Updated promo credit details
        """
        _param = self._promo_credit_decrement_post_serialize(
            user_id=user_id,
            amount=amount,
            currency=currency,
            description=description,
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

    def _promo_credit_decrement_post_serialize(
        self,
        user_id,
        amount,
        currency,
        description,
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
        _body_params['userId'] = user_id
        _body_params['amount'] = amount
        _body_params['currency'] = currency
        if description is not None:
            _body_params['description'] = description

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
            resource_path='/merchant/promo_credit/decrement',
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
