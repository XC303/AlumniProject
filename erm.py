import pygame
import textwrap

# Initialize pygame
pygame.init()

# Define screen dimensions
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Wrapped Text Example')

# Define font
font = pygame.font.Font(None, 36)

# Long text that needs to be wrapped
long_text = "This is a very long string of text that will be wrapped to fit within the screen width. " \
            "Text wrapping is useful when you have dynamic text or user input that may exceed the screen width."

# Wrap the text using textwrap
margin = 20
max_width = screen_width - margin * 2  # Leaving some margin on both sides
wrapped_text = textwrap.fill(long_text, width=60)  # Adjust width as needed for your font

# Main loop
running = True
while running:
    screen.fill((255, 255, 255))  # Fill the screen with a white background

    # Draw the wrapped text
    y_position = margin
    for line in wrapped_text.splitlines():
        text_surface = font.render(line, True, (0, 0, 0))  # Render each line of text
        screen.blit(text_surface, (margin, y_position))
        y_position += text_surface.get_height()  # Move down for the next line

    pygame.display.flip()  # Update the screen

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit pygame
pygame.quit()
