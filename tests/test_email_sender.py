import pytest
from unittest.mock import patch, MagicMock
from src import email_sender

@patch("email_sender.smtplib.SMTP_SSL")
def test_send_email_success(mock_smtp):
    mock_server = MagicMock()
    mock_smtp.return_value.__enter__.return_value = mock_server

    email_sender.send_email("test@example.com", "Test Subject", "Test Body")

    mock_server.login.assert_called_once_with(email_sender.EMAIL_ADDRESS, email_sender.EMAIL_PASSWORD)
    mock_server.send_message.assert_called_once()

@patch("email_sender.smtplib.SMTP_SSL", side_effect=Exception("SMTP error"))
def test_send_email_failure(mock_smtp):
    email_sender.send_email("test@example.com", "Test Subject", "Test Body")