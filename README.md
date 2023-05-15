# Gobind Sarvar Jeopardy Game Show

This is a Python project developed for a history Jeopardy competition successfully used by Gobind Sarvar Surrey School. The project implements a 4-player game show with multiple modes, buzzer functionality, sound effects, player light indicators, a GUI component for administrative control, and multi-threading support. It is designed to run on a Raspberry Pi and provides an interactive and engaging experience for the participants.

## Features

The Game Show Python project offers the following features:

1. **Multiple Game Modes:** The project includes several game modes to cater to different preferences and gameplay styles.

2. **Buzzer Integration:** The project supports buzzer functionality, allowing participants to buzz in to answer questions.

3. **Sound Effects:** Sound effects are played to indicate correct and incorrect answers, enhancing the game show experience.

4. **Player Light Indicators:** The players' lights flash to indicate when they have successfully buzzed in.

5. **GUI Component:** The project includes a GUI component developed using Python's Pygame library. This allows administrators to control the game, manage questions, and display game-related information on a graphical interface.

6. **Multi-threading:** The project incorporates multi-threading to handle concurrent processes. This ensures smooth execution of different tasks, such as managing player input, updating game state, and displaying information simultaneously.

## Game Modes

The game show consists of the following game modes:

### Mode 1: Regular Mode

In this mode, up to 4 participants can play simultaneously. The rules for this mode are as follows:

- Each participant will be asked a series of questions.
- Participants can buzz in by pressing their respective buzzer buttons.
- When a participant buzzes in, a sound effect plays, and their player light flashes.
- If the participant answers correctly, a correct answer sound effect plays.
- If the participant answers incorrectly, a wrong answer sound effect plays.

### Mode 2: Steal Round

In this mode, up to 4 participants can play simultaneously. The rules for this mode are as follows:

- Each participant will be asked a series of questions.
- Participants can buzz in by pressing their respective buzzer buttons.
- When a participant buzzes in, a sound effect plays, and their player light flashes.
- If the participant answers correctly, a correct answer sound effect plays.
- If the participant answers incorrectly, a wrong answer sound effect plays.
- The participant with the wrong answer will have there buzzer disabled.
- Other players have the option to buzz in and steal the point if the answer is incorrect.

## Getting Started

To use the Game Show Python project on a Raspberry Pi, follow these steps:

1. Set up your Raspberry Pi with the necessary peripherals (buttons, lights, speakers, and a display for the GUI component).
2. Install Python on your Raspberry Pi if not already installed.
3. Clone the project repository from GitHub: `git clone https://github.com/Gurshant/gs-jeopardy-game-show`
4. Install the required dependencies by running the following command: `pip install -r requirements.txt`
5. Connect the buttons and lights to the Raspberry Pi GPIO pins according to the project's wiring diagram.
6. Configure the sound effects to be played by connecting the speakers to the Raspberry Pi audio output.
7. Launch the game by running the script: `python ControlMenu.py`
8. Use the GUI interface to control the game.
9. Participants can interact with the game using the buzzer buttons.

## Wiring Diagram

<img src="https://github.com/Gurshant/gs-jeopardy-game-show/blob/master/wiring%20diagram.jpeg" align="left" height="900" width="380" >

## Contributors

The Game Show Python project was developed by the following contributors:

- Gurshant Sandhu ([@gurshant](https://github.com/gurshant))
- Charlie Gill ([@charlie](https://github.com/cgill87))

