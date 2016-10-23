import pytest

from sut.docker import Docker


@pytest.fixture(scope="module")
def module_scope():
    return Docker("Module")


@pytest.fixture(scope="session")
def session_scope():
    return Docker("Session")


@pytest.fixture(scope="class")
def class_scope():
    return Docker("Class")


@pytest.fixture(scope="function")
def function_scope():
    return Docker("Function")
