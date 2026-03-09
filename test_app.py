from app import greet


def test_greet():
    assert greet("World") == "Hello, World!"

def test_greet_custom():
    assert greet("Garen") == "Hello, Garen!"
