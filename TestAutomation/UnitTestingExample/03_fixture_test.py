import pytest


"""
Basic fixtures
"""


def test_with_local_fixture(local_fixture):
    """
    Fixtures can be invoked simply by having a positional arg
    with the same name as a fixture:
    """
    print("Running test_with_local_fixture...")
    assert True


@pytest.fixture
def local_fixture():
    """
    Fixtures are callables decorated with @fixture
    """
    print("\n(Doing Local Fixture setup stuff!)")


def test_with_global_fixture(global_fixture):
    """
    Fixtures can also be shared across test files (see conftest.py)
    """
    print("Running test_with_global_fixture...")


"""
Fixtures with return values
"""


def test_with_data_fixture(one_fixture):
    """
    PyTest finds the fixture whose name matches the argument,
    calls it, and passes that return value into our test case:
    """
    print("\nRunning test_with_data_fixture: {}".format(one_fixture))
    assert one_fixture == 1


@pytest.fixture
def one_fixture():
    """
    Beyond just "doing stuff", fixtures can return data, which
    PyTest will pass to the test cases that refer to it...
    """
    print("\n(Returning 1 from data_fixture)")
    return 1


def test_with_yield_fixture(yield_fixture):
    print("\n    Running test_with_yield_fixture: {}".format(yield_fixture))
    assert "foo" in yield_fixture


@pytest.fixture
def yield_fixture():
    """
    Fixtures can yield their data
    (additional code will run after the test)
    """
    print("\n\n(Initializing yield_fixture)")
    x = {"foo": "bar"}

    # Remember, unlike generators, fixtures should only yield once (if at all)
    yield x

    print("\n(Cleaning up yield_fixture)")
    del (x)


"""
Fixtures with context
"""

def test_with_introspection(introspective_fixture):
    print("\nRunning test_with_introspection...")
    assert True


@pytest.fixture
def introspective_fixture(request):
    """
    The request fixture allows introspection into the
    "requesting" test case
    """
    print("\n\nintrospective_fixture:")
    print("...Called at {}-level scope".format(request.scope))
    print("   ...In the {} module".format(request.module))
    print("      ...On the {} node".format(request.node))