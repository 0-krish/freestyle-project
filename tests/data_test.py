import os
import pytest

from app.data_storage import read_sheet, write_sheet

CI_ENV = os.getenv("CI") == "true"

@pytest.mark.skipif(CI_ENV==True, reason="to avoid issuing HTTP requests on the CI server")
def test_data_storage():
    '''
    Tests to ensure data storage is working properly
    '''
    assert write_sheet("test", "test@test.com", "us", "general") == {
                                                                    "Name": "test",
                                                                    "Email": "test@test.com",
                                                                    "Country": "us",
                                                                    "Category": "general",
                                                                    }

    test_dict = read_sheet()
    assert list(test_dict[0].keys()) == ['Name', 'Email', 'Country', 'Category']
