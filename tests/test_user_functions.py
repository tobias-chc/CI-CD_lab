# Tests (copy to tests/test_user_functions.py)
import pytest
import os
import io

from src.user_functions import *


# Email test
def test_email_with_user_input_no_at_sign(monkeypatch):
    # Set the console input to: petra.adaltas.com
    monkeypatch.setattr('sys.stdin', io.StringIO('petra.adaltas.com'))
    assert get_email_from_input() is None

def test_email_with_user_input_no_dot(monkeypatch):
    # Set the console input to: petra@adaltascom
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltascom'))
    assert get_email_from_input() is None

def test_email_with_user_input_correct(monkeypatch):
    # Set the console input to: petra@adaltas.com
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltas.com'))
    assert get_email_from_input() == 'petra@adaltas.com'


# Username test
def test_get_user_name_from_input_spaces(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('tobias chc'))
    assert get_user_name_from_input() is None

def test_get_user_name_from_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('tobiaschc'))
    assert get_user_name_from_input() == 'tobiaschc'

# Password test
def test_get_password_from_input_less8_characters(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('1@eR#'))
    assert get_password_from_input() is None

def test_get_password_from_input_no_number(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('xWErXsw@er'))
    assert get_password_from_input() is None

def test_get_password_from_input_no_upper_case(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('125334@m'))
    assert get_password_from_input() is None

def test_get_password_from_input_no_lower_case(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('123784@#M'))
    assert get_password_from_input() is None

def test_get_password_from_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('12ERdf@zW'))
    assert get_password_from_input() == '12ERdf@zW'
