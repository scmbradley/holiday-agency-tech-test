# Holiday Agency

To try the simple GUI, run `python agency_gui.py`.

The car journey portion of the trip is represented by a `CarJourney` object from `carjourney.py`.
The air travel portion is handled by `airports.py` which connects to the API,
and `airjourney.py` which contains the `AirJourney` object which represents a trip by air.
The `FullJourney` object represents the whole trip.

## Requirements

The program relies on the `requests` library for API calls and
the `PySimpleGUI` library for the GUI.
