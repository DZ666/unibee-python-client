#!/usr/bin/env python3
"""
Basic usage example for the UniBee Python SDK.

This example demonstrates how to configure and use the SDK
to interact with the UniBee Billing API.

Before running, set your API token:
    export UNIBEE_API_TOKEN="your_api_token_here"
"""

import os
import sys

# Add parent directory to path for development testing
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import openapi_client
from openapi_client.rest import ApiException


def main():
    # Get API token from environment
    api_token = os.environ.get("UNIBEE_API_TOKEN")
    
    if not api_token:
        print("Error: UNIBEE_API_TOKEN environment variable not set")
        print("Set it with: export UNIBEE_API_TOKEN='your_token_here'")
        sys.exit(1)
    
    # Configure the SDK
    # Use sandbox for testing: https://api-sandbox.unibee.top
    # Use production for live: https://api.unibee.dev
    configuration = openapi_client.Configuration(
        host="https://api-sandbox.unibee.top",  # Sandbox environment
        access_token=api_token
    )
    
    # Create API client
    with openapi_client.ApiClient(configuration) as api_client:
        print("=" * 50)
        print("UniBee Python SDK - Basic Usage Example")
        print("=" * 50)
        print(f"SDK Version: {openapi_client.__version__}")
        print(f"API Host: {configuration.host}")
        print()
        
        # Example 1: Get merchant profile
        print("1. Getting Merchant Profile...")
        try:
            profile_api = openapi_client.Profile(api_client)
            profile = profile_api.get_get()
            print(f"   Success! Merchant data received.")
            print(f"   Response: {profile}")
        except ApiException as e:
            print(f"   API Error: {e.status} - {e.reason}")
        print()
        
        # Example 2: List subscription plans
        print("2. Listing Subscription Plans...")
        try:
            plan_api = openapi_client.Plan(api_client)
            plans = plan_api.plan_list_get()
            print(f"   Success! Plans received.")
            print(f"   Response: {plans}")
        except ApiException as e:
            print(f"   API Error: {e.status} - {e.reason}")
        print()
        
        # Example 3: List products
        print("3. Listing Products...")
        try:
            product_api = openapi_client.Product(api_client)
            products = product_api.product_list_get(page=0, count=10)
            print(f"   Success! Products received.")
            print(f"   Response: {products}")
        except ApiException as e:
            print(f"   API Error: {e.status} - {e.reason}")
        print()
        
        # Example 4: List users
        print("4. Listing Users...")
        try:
            user_api = openapi_client.User(api_client)
            users = user_api.user_list_get()
            print(f"   Success! Users received.")
            print(f"   Response: {users}")
        except ApiException as e:
            print(f"   API Error: {e.status} - {e.reason}")
        print()
        
        # Example 5: List invoices
        print("5. Listing Invoices...")
        try:
            invoice_api = openapi_client.Invoice(api_client)
            invoices = invoice_api.invoice_list_get()
            print(f"   Success! Invoices received.")
            print(f"   Response: {invoices}")
        except ApiException as e:
            print(f"   API Error: {e.status} - {e.reason}")
        print()
        
        print("=" * 50)
        print("Example completed!")
        print("=" * 50)


if __name__ == "__main__":
    main()
