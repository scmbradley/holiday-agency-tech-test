# Holiday Agency

To try the simple GUI, run `python agency_gui.py`.

The car journey portion of the trip is represented by a `CarJourney` object from `carjourney.py`.
The air travel portion is handled by `airports.py` which connects to the API,
and `airjourney.py` which contains the `AirJourney` object which represents a trip by air.
The `FullJourney` object represents the whole trip.

## Requirements

The program relies on the `requests` library for API calls and
the `PySimpleGUI` library for the GUI.
The program needs Python 3.6+ because f-strings are great.

## Remarks

I haven't got into the habit of using Python's type hints yet,
but it would probably be a good idea to do so.

The GUI is a proof-of-concept at best.
One improvement would be to set the default options to what was
previously selected when clicking "Restart".

Test coverage is minimal,
you'd want to add a bunch more parameterised tests on the 
user inputs, for example (using, e.g. `hypothesis`).
You'd also want to have a mock up of the API, rather than using calls to
the actual API in the tests.
(e.g. monkeypatch the api call in `TestFullJourney` to return `airport_json` rather than
calling the API).

No error checking or input checking is currently done.
You'd want to handle API error codes and weird user input
more carefully and gracefully.

On the other hand, use of the composite pattern means that 
adding a new form of transport (e.g. trains)
would be pretty simple:
just subclass `Journey` to make `TrainJourney`
and `TrainLeg` classes, following the pattern of `AirJourney`
and `AirLeg`.

Why isn't `AirLeg` a subclass of `AirJourney` rather than `Journey`?
It could be, I don't think it would make much difference either way.
Although I can imagine circumstances where it might make sense to
do things that way instead.

PySimpleGUI is a little awkward in that the 
list items that are inputs to `sg.Combo` are also the outputs
when one is selected.
So if I want to desiply the full name of the airport in the drop-down menu,
but I only need to know the airport code to create the `FullJourney` object,
I need to create this `dict`, `name_to_code` to extract the code from the 
full name.

`FullJourney` is not, currently, very flexible:
it can only handle a car journey followed by a return trip
by plane.
But, as I mentioned above, the underlying `CarJourney` and
`AirJourney` structures are quite flexible, so `FullJourney`
could certainly be made more feature rich fairly easily.
