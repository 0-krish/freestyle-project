import os
import pytest

from app.news_service import get_headlines

CI_ENV = os.getenv("CI") == "true"

@pytest.mark.skipif(CI_ENV==True, reason="to avoid issuing HTTP requests on the CI server")
def test_news_service():
    '''
    Tests to ensure news service (getting the headline data from the News API) is working properly
    '''
    news_received = get_headlines("us", "general")
    assert news_received["status"] == "ok"

