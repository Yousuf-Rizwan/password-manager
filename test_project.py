import pytest
from project import add_key, view, add
from cryptography.fernet import Fernet
import os

# test 1
def test_add_key():
    test_key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(test_key)

    result = add_key()

    assert result == test_key
    print("\nKey works!\n")

# test 2
def test_view(capsys):
    test_key = Fernet.generate_key()
    fer = Fernet(test_key)
    encrypted_password = fer.encrypt(b"mypassword123").decode()

    # Create password file
    with open("password.txt", "w") as f:
        f.write(f"testuser|{encrypted_password}\n")

    view(fer)

    printed_output = capsys.readouterr().out
    assert "testuser" in printed_output
    assert "mypassword123" in printed_output
    print("\nSaves passwords!\n")

# test 3
def test_add(monkeypatch):

    test_key = Fernet.generate_key()
    fer = Fernet(test_key)
    monkeypatch.setattr('builtins.input', lambda x: "testaccount" if "account" in x else "testpass")


    if os.path.exists("password.txt"):
        os.remove("password.txt")

    add(fer, None, None)

    # verify
    with open("password.txt", "r") as f:
        content = f.read()
        assert "testaccount|" in content
        assert len(content.split("|")) == 2
    print("\nPasswords worked!\n")


@pytest.fixture(autouse=True)
def cleaning_up():
    yield

    if os.path.exists("key.key"):
        os.remove("key.key")
    if os.path.exists("password.txt"):
        os.remove("password.txt")
print("IT WORKS!!")
