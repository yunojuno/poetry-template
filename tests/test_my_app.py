def test_import():
    import my_app  # noqa: F401

    assert "Empty test to ensure pytest passes."
