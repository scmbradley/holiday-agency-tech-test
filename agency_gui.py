"""Handles creating the simple GUI."""

import PySimpleGUI as sg
from fulljourney import FullJourney
from airports import Airports

a = Airports()
airport_list, name_to_code = a.airport_list(with_code=True)


def enter_info_window():
    """Create a window for user to enter journey information."""
    layout = [
        [sg.Text("Please enter your information.")],
        [sg.Text("Number of travellers:"), sg.Push(), sg.InputText("", key="people")],
        [sg.Text("Distance to airport:"), sg.Push(), sg.InputText("", key="distance")],
        [sg.Text("Origin Airport"), sg.Push(), sg.Combo(airport_list, key="outbound")],
        [
            sg.Text("Destination Airport"),
            sg.Push(),
            sg.Combo(airport_list, key="inbound"),
        ],
        [sg.OK(), sg.Cancel()],
    ]
    return sg.Window("Holiday Agency", layout)


def create_full_journey(values):
    """Take values output from window and return FullJourney"""
    outbound = name_to_code[values["outbound"]]
    inbound = name_to_code[values["inbound"]]
    f = FullJourney(
        int(values["people"]),
        int(values["distance"]),
        outbound,
        inbound,
        airports=a,
    )
    return f


def create_confirmation_window(f):
    layout = [[sg.Text(x)] for x in f.journey_string()] + [
        [sg.OK(), sg.Button("Restart"), sg.Cancel()]
    ]
    return sg.Window("Your trip", layout)


### Main loop:

window = enter_info_window()

while True:
    event, values = window.read()
    if event in [sg.WINDOW_CLOSED, "Cancel"]:
        break
    elif event == "OK":
        f = create_full_journey(values)
        window.close()
        window_pop = create_confirmation_window(f)
        event, values = window_pop.read()
        window_pop.close()
        if event in [sg.WINDOW_CLOSED, "Cancel"]:
            window_pop.close()
            break
        elif event == "OK":
            print("Booking holiday")
            f.print_journey()
            window_pop.close()
            break
        elif event == "Restart":
            window = enter_info_window()

window.close()
