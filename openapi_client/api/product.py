# coding: utf-8

"""
    UniBee API

    UniBee Merchant API for product management

    The version of the OpenAPI document: 2.0.0
"""

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from openapi_client.api_client import ApiClient, RequestSerialized
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType


class Product:
    """UniBee Product API for managing products.
    
    This class provides methods to create, manage, and retrieve products
    which contain subscription plans.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def product_new_post(
        self,
        product_name: Annotated[str, Field(description="Product name")],
        description: Annotated[Optional[str], Field(description="Product description")] = None,
        home_url: Annotated[Optional[str], Field(description="Product home URL")] = None,
        image_url: Annotated[Optional[str], Field(description="Product image URL")] = None,
        metadata: Annotated[Optional[Dict[str, str]], Field(description="Product metadata")] = None,
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
        """Create a new product.
        
        :param product_name: Product name (required)
        :param description: Product description
        :param home_url: Product home URL
        :param image_url: Product image URL
        :param metadata: Product metadata
        :return: Created product details
        """
        _param = self._product_new_post_serialize(
            product_name=product_name,
            description=description,
            home_url=home_url,
            image_url=image_url,
            metadata=metadata,
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

    def _product_new_post_serialize(
        self,
        product_name,
        description,
        home_url,
        image_url,
        metadata,
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
        _body_params['productName'] = product_name
        if description is not None:
            _body_params['description'] = description
        if home_url is not None:
            _body_params['homeUrl'] = home_url
        if image_url is not None:
            _body_params['imageUrl'] = image_url
        if metadata is not None:
            _body_params['metadata'] = metadata

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
            resource_path='/merchant/product/new',
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
    def product_list_get(
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
        """Get list of products.
        
        :param page: Page number
        :param count: Number of items per page
        :return: List of products
        """
        _param = self._product_list_get_serialize(
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

    def _product_list_get_serialize(
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
            resource_path='/merchant/product/list',
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
    def product_detail_get(
        self,
        product_id: Annotated[int, Field(description="Product ID")],
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
        """Get product detail.
        
        :param product_id: Product ID (required)
        :return: Product details
        """
        _param = self._product_detail_get_serialize(
            product_id=product_id,
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

    def _product_detail_get_serialize(
        self,
        product_id,
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
        _query_params.append(('productId', product_id))

        # Set headers
        _header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # Authentication
        _auth_settings: List[str] = ['Authorization']

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/merchant/product/detail',
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
    def product_edit_post(
        self,
        product_id: Annotated[int, Field(description="Product ID")],
        product_name: Annotated[Optional[str], Field(description="Product name")] = None,
        description: Annotated[Optional[str], Field(description="Product description")] = None,
        home_url: Annotated[Optional[str], Field(description="Product home URL")] = None,
        image_url: Annotated[Optional[str], Field(description="Product image URL")] = None,
        metadata: Annotated[Optional[Dict[str, str]], Field(description="Product metadata")] = None,
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
        """Edit a product.
        
        :param product_id: Product ID (required)
        :param product_name: Product name
        :param description: Product description
        :param home_url: Product home URL
        :param image_url: Product image URL
        :param metadata: Product metadata
        :return: Updated product details
        """
        _param = self._product_edit_post_serialize(
            product_id=product_id,
            product_name=product_name,
            description=description,
            home_url=home_url,
            image_url=image_url,
            metadata=metadata,
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

    def _product_edit_post_serialize(
        self,
        product_id,
        product_name,
        description,
        home_url,
        image_url,
        metadata,
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
        _body_params['productId'] = product_id
        if product_name is not None:
            _body_params['productName'] = product_name
        if description is not None:
            _body_params['description'] = description
        if home_url is not None:
            _body_params['homeUrl'] = home_url
        if image_url is not None:
            _body_params['imageUrl'] = image_url
        if metadata is not None:
            _body_params['metadata'] = metadata

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
            resource_path='/merchant/product/edit',
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
    def product_activate_post(
        self,
        product_id: Annotated[int, Field(description="Product ID to activate")],
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
        """Activate a product.
        
        :param product_id: Product ID to activate (required)
        :return: Activation result
        """
        _param = self._product_activate_post_serialize(
            product_id=product_id,
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

    def _product_activate_post_serialize(
        self,
        product_id,
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
        _body_params['productId'] = product_id

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
            resource_path='/merchant/product/activate',
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
    def product_delete_post(
        self,
        product_id: Annotated[int, Field(description="Product ID to delete")],
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
        """Delete a product.
        
        :param product_id: Product ID to delete (required)
        :return: Deletion result
        """
        _param = self._product_delete_post_serialize(
            product_id=product_id,
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

    def _product_delete_post_serialize(
        self,
        product_id,
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
        _body_params['productId'] = product_id

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
            resource_path='/merchant/product/delete',
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
