from src import helloworld


def test_helloworld() -> None:
    """this is testhello world"""
    assert helloworld() == "Hello World"
