# Standard library imports
import os
import uuid
from pathlib import Path
from unittest.mock import patch

# Third-party imports
import pytest
from dotenv import load_dotenv

# Load test environment variables
load_dotenv(Path(__file__).parent.parent / '.env.test')

# Ensure environment variables are set
# SUPABASE_URL and SUPABASE_SERVICE_KEY are required for running tests,
# even though we mock the Supabase client. These variables are used in the
# initialization process and must be present in the environment.
# In CI, these are set as GitHub Secrets and passed to the workflow.
# Locally, they are loaded from .env.test file at the project root.
if not os.getenv('SUPABASE_URL') or not os.getenv('SUPABASE_SERVICE_KEY'):
    raise EnvironmentError("Required Supabase environment variables are not set")

# Mock for Supabase client
class MockSupabase:
    def __init__(self):
        self.storage = MockStorage()

class MockStorage:
    def __init__(self):
        # Pre-create the charts bucket since it's used in tests
        self.buckets = {"charts": {}}
    
    def from_(self, bucket_name):
        # Always return a valid bucket object, even if the bucket doesn't exist
        if bucket_name not in self.buckets:
            self.buckets[bucket_name] = {}
        return MockBucket(self.buckets[bucket_name], bucket_name)

class MockBucket:
    def __init__(self, storage, bucket_name):
        self.storage = storage
        self.bucket_name = bucket_name
    
    def upload(self, file_name, file_obj):
        """
        Mock upload function that handles file objects of any type
        """
        # Close the file if it's open to avoid resource leaks
        if hasattr(file_obj, 'close') and callable(file_obj.close):
            try:
                file_obj.close()
            except Exception:
                pass
                
        # Store a reference that we got this file
        self.storage[file_name] = True
        return {"Key": file_name}
    
    def get_public_url(self, file_name):
        """
        Return a predictable URL for testing
        """
        return f"http://mock-supabase-{self.bucket_name}.com/{file_name}"

@pytest.fixture(autouse=True)
def mock_supabase():
    """
    Automatically patch the Supabase client in all tests.
    This fixture runs automatically for all tests.
    """
    mock_client = MockSupabase()
    
    # Patch the create_client function to return our mock
    with patch('supabase.create_client', return_value=mock_client):
        # Also patch direct imports from insight_engine if they exist
        with patch('api.services.insight_engine._supabase', mock_client):
            yield mock_client

@pytest.fixture
def mock_uuid():
    """
    Fixture to mock uuid.uuid4() for consistent test results
    """
    fixed_uuid = "00000000-0000-0000-0000-000000000000"
    with patch('uuid.uuid4', return_value=uuid.UUID(fixed_uuid)):
        yield fixed_uuid

