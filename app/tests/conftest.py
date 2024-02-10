import pytest
from playwright.sync_api import expect


@pytest.fixture
def cust_expect():
    expect.set_options(timeout=10_000)
    return expect
