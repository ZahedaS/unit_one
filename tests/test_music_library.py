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


def test_add_empty_string():
    tracker = Music_library()
    with pytest.raises(Exception) as err:
        tracker.add_track("", "")
    assert str(err.value) == "Please provide track details"


def test_add_multiple_tracks():
    tracker = Music_library()
    tracker.add_track("Muad", "Al-Quran")
    tracker.add_track("Zain Bhikha", "Mountains of Makkah")
    assert tracker.view_library() == {"Muad":"Al-Quran", 
                                    "Zain Bhikha":"Mountains of Makkah"}
    


def test_add_duplicate_tracks():
    tracker = Music_library()
    tracker.add_track("Muad", "Al-Quran")
    with pytest.raises(Exception) as err:
        tracker.add_track("Muad", "Al-Quran")
    assert str(err.value) == "Track already exists"

def test_whitespace():
    tracker = Music_library()
    with pytest.raises(Exception) as err:
        tracker.add_track(" ", " ")
    assert str(err.value) == "Please provide track details"


def test_check_if_string():
    tracker = Music_library()
    with pytest.raises(TypeError) as err:
        tracker.add_track(1,3)
    
    assert str(err.value) == "Please enter text"