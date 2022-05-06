import os
import pytest

from app.email_service import send_test_email

CI_ENV = os.getenv("CI") == "true"

@pytest.mark.skipif(CI_ENV==True, reason="to avoid issuing HTTP requests on the CI server")
def test_email_service():
    '''
    Tests to ensure email service is working properly
    '''
    assert send_test_email() == 202
