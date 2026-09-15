import validation

def test_email():
    assert validation.validate_email("test@example.com")
    assert not validation.validate_email("bad email")

def test_phone():
    assert validation.validate_phone("2485551234")
    assert not validation.validate_phone("abc123")
