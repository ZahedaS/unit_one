# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them._

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Music_library():
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        #   None
        # Side effects:
        #   Create an empty dict to store the music in
        self.library = {}

    def add_track(self, artist, title):
        # Parameters:
        #   artist: a string representing the artists name
        #   title: a string representing the track title
        # Returns:
        #   Nothing
        # Side-effects
        #   will add the track details to the library dictionary
        self.library[artist] = title

    def view_library(self):
        # Returns:
        #   a dictionary of all current tracks that have been added
        # Side-effects:
        #   throws exception if library is empty
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` 
"""
test view empty library 
it should throw en exception "LIbrary is empty"
"""

"""
test add 1 track to the library and view the library
the added track should be int he library
"""

"""
test add an empty track/string to the library 
should raise an exception "Please provide artist name and track title"
"""

"""
test adding multiple tracks and viewing the library
the corresponding tracks should inside the library
"""

"""
test adding same track multiple times
should raise an exception if same track is added more than once
"Track already exists in library"
"""

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
