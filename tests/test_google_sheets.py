import pytest
from unittest.mock import patch, MagicMock
from src import google_sheets

@patch("src.google_sheets.gspread.authorize")
@patch("src.google_sheets.ServiceAccountCredentials.from_json_keyfile_name")
def test_get_form_responses(mock_creds, mock_authorize):
    mock_client = MagicMock()
    mock_sheet = MagicMock()
    mock_sheet.get_all_records.return_value = [{"Name": "Test", "Email": "test@example.com"}]
    mock_client.open.return_value.sheet1 = mock_sheet
    mock_authorize.return_value = mock_client

    responses = google_sheets.get_form_responses()
    assert isinstance(responses, list)
    assert responses[0]["Name"] == "Test_Test"
    assert responses[0]["Email"] == "test@example.com"