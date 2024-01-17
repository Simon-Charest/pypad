from pygame import event, init, JOYBUTTONDOWN, joystick, quit
from random import randrange
from pypad.simulate_gamepad_input import simulate_gamepad_input
from time import sleep
from typing import List


def test_simulate_gamepad_inputs_1() -> None:
    simulate_gamepad_inputs()

def test_simulate_gamepad_inputs_2() -> None:
    simulate_gamepad_inputs(5, 1)

def test_simulate_gamepad_inputs_3() -> None:
    simulate_gamepad_inputs(10, 0.2)

def test_simulate_gamepad_inputs_4() -> None:
    simulate_gamepad_inputs(50)
    
def test_simulate_gamepad_inputs_5() -> None:
    simulate_gamepad_inputs(2000, 0.5)


def simulate_gamepad_inputs(expected: int = 1, secs: float = 0) -> None:
    """Function to simulate gamepad inputs."""
    
    """Arrange"""
    button_values: List[int]

    """Act"""
    # Initialize pygame
    init()

    # Initialize the joystick module
    joystick.init()

    # Process events to avoid freezing
    event.get()

    for _ in range(expected):
        while True:
            button_values = [randrange(2), randrange(2), randrange(2), randrange(2)]

            if any(button_values):
                break

        simulate_gamepad_input(button_values=button_values)
        sleep(secs / expected)

    # Check if the button press events have occurred
    actual: int = len([event for event in event.get() if event.type == JOYBUTTONDOWN and event.button == 0])

    # Quit pygame
    quit()

    """Assert"""
    assert actual == expected
