# PONG Game in Python

This is a classic Pong game built in Python using the `pygame` library. It features a simple, fun gameplay experience and showcases the following features:
- **Game Menu**: Start or quit the game from the main menu.
- **Gameplay**: Two paddles and a bouncing ball, with a competitive objective to keep the ball from going out of bounds.
- **Score Tracking**: Counts the number of times each player hits the ball during gameplay.
- **Game Over Screen**: Displays the winner and the total number of hits made by the winner.
- **Restart or Quit**: Players can restart the game or exit after the game ends.

## Demo
![Game Demo](./media/gameplay.gif)

## Features
1. **Main Menu**:
   - Options: "Start Game" and "Quit".

2. **Pong Gameplay**:
   - Classic Pong mechanics: Two paddles and a bouncing ball.
   - Player 1 (left paddle) controls: `W` (up) and `S` (down).
   - Player 2 (right paddle) controls: `UP ARROW` (up) and `DOWN ARROW` (down).

3. **Dynamic Scoring**:
   - Tracks how many times each player successfully hits the ball.

4. **Game Over Screen**:
   - Displays the winning player and their total hits.
   - Options: "Restart Game" or "Quit".

5. **Replayability**:
   - Restart the game easily from the "Game Over" screen.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pong-game-python.git
   cd pong-game-python
   ```

2. Install dependencies:
   ```bash
   pip install pygame
   ```

3. Run the game:
   ```bash
   python game.py
   ```

## Controls
- **Player 1 (Left Paddle)**:
  - `W` - Move up
  - `S` - Move down
- **Player 2 (Right Paddle)**:
  - `UP ARROW` - Move up
  - `DOWN ARROW` - Move down
- **Menu Navigation**:
  - Click on options to select.

## Project Structure
```bash
pong-game-python/
├── src/
│   ├── ball.py          # Handles ball behavior, movement, and rotation
│   ├── controls.py      # Displays the controls screen and animations
│   ├── game.py          # Main game loop and overall logic
│   ├── game_over.py     # GameOver screen functionality
│   ├── menu.py          # Main menu and navigation options
│   ├── mouse.py         # Custom mouse cursor behavior
│   ├── paddle.py        # Paddle behavior, movement, and collision
│   ├── starfield.py     # Starfield background animation
├── assets/              # Game assets (images, fonts, etc.)
├── media/               # Additional media files (e.g., sounds, gifs)
├── README.md            # Project documentation
└── .gitignore           # Git ignore file for unnecessary files
        

```

## Future Improvements
This project is a work in progress, with the goal of learning! :)