from app.data_storage import load_auth, read_sheet, write_sheet

def test_data_storage():
    assert write_sheet("test", "test@test.com", "us", "general") == {
                                                                    "Name": "test",
                                                                    "Email": "test@test.com",
                                                                    "Country": "us",
                                                                    "Category": "general",
                                                                    }
