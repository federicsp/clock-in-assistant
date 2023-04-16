from unittest.mock import patch
from utils import create_audio, have_clocked_in

def test_create_audio():
    # Test that the audio file is created successfully
    create_audio("John", "test/audio.mp3")
    with open("test/audio.mp3", "rb") as f:
        assert f.read() != b""

def test_have_clocked_in(capsys):
    # Test that the function returns True if input is received
    with patch("builtins.input", return_value="yes"):
        assert have_clocked_in() == True
