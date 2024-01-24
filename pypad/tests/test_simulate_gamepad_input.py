from pygame import event, init, JOYBUTTONDOWN, joystick, quit
from pypad.math import flooring
from pypad.simulate_gamepad_input import simulate_gamepad_input
from random import randrange
from time import sleep, time
from typing import List


class TestSimulateGamepadInputs():
    def test_simulate_gamepad_inputs_1(self) -> None:
        self.simulate_gamepad_inputs()

    def test_simulate_gamepad_inputs_2(self) -> None:
        self.simulate_gamepad_inputs(2, 1/60)

    def test_simulate_gamepad_inputs_3(self) -> None:
        self.simulate_gamepad_inputs(3, 5/60)

    def test_simulate_gamepad_inputs_4(self) -> None:
        self.simulate_gamepad_inputs(4, 6/60)

    def test_simulate_gamepad_inputs_5(self) -> None:
        self.simulate_gamepad_inputs(5, 25/60)

    def simulate_gamepad_inputs(self, stop: int = 1, secs: float = 0, imprecision: int = 100) -> None:
        """Function to simulate gamepad inputs."""
        
        """Arrange"""
        expected_time: float = stop * secs
        
        """Act"""
        # Initialize pygame
        init()

        # Initialize the joystick module
        joystick.init()

        # Process events to avoid freezing
        event.get()

        button_values: List[int]

        start_time: float = time()

        for _ in range(stop):
            while True:
                button_values = [randrange(2), randrange(2), randrange(2), randrange(2)]

                if any(button_values):
                    break

            simulate_gamepad_input(button_values=button_values)
            sleep(secs)

        elapsed_time: float = time() - start_time

        # Check if the button press events have occurred
        number_of_button_down: int = len([event for event in event.get() if event.type == JOYBUTTONDOWN and event.button == 0])

        # Quit pygame
        quit()

        """Assert"""
        assert number_of_button_down == stop
        assert flooring(elapsed_time, imprecision) == flooring(expected_time, imprecision)
