from lib.music_library import Music_library
import pytest;

def test_view_empty_library_raises_exception():

    tracker = Music_library()

    with pytest.raises(Exception) as err:
        tracker.view_library()
    assert str(err.value) == "Library is empty"


def test_add_one_track_and_view():
    tracker = Music_library()

    tracker.add_track("Maher Zain", "The chosen one")
    result = tracker.view_library()
    assert result == {
        "Maher Zain" :"The chosen one"
    }