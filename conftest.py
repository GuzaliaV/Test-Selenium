import pytest
from faker import Faker

@pytest.fixture(scope='session', autouse=True)
def setup_name_BU():
    fake = Faker("ru_RU")
    name_BU = fake.city()
    yield name_BU
