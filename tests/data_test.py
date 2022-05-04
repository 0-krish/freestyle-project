import os
import pytest

from app.data_storage import load_auth, read_sheet, write_sheet

CI_ENV = os.getenv("CI") == "true"

@pytest.mark.skipif(CI_ENV==True, reason="to avoid issuing HTTP requests on the CI server")
def test_data_storage():
    assert write_sheet("test", "test@test.com", "us", "general") == {
                                                                    "Name": "test",
                                                                    "Email": "test@test.com",
                                                                    "Country": "us",
                                                                    "Category": "general",
                                                                    }

    
