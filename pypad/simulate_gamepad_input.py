from pygame import event, JOYAXISMOTION, JOYBUTTONDOWN, JOYBUTTONUP
from typing import List


def simulate_gamepad_input(joy: int = 0, axis_values: List[float] = None, button_values: List[int] = None) -> None:
    """Function to simulate a gamepad input."""

    button_index: int
    button_state: int

    if axis_values:
        event.post(event.Event(JOYAXISMOTION, {"joy": joy, "value": axis_values}))
    
    if button_values:
        for button_index, button_state in enumerate(button_values):
            if button_state == JOYBUTTONDOWN:
                event.post(event.Event(JOYBUTTONUP, {"joy": joy, "button": button_index}))
                
            event.post(event.Event(JOYBUTTONDOWN, {"joy": joy, "button": button_index}))
