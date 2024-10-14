import pygame

# Initialize Pygame
pygame.init()

# Set up the display window
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Python Chess Game Tutorial with Pygame")

# Function to draw text
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Main game loop
running = True
while running:
    screen.fill(pygame.Color("black"))

    # Display the personalized message
    font = pygame.font.SysFont("helvetica", 30)
    draw_text("Welcome CK to our Committee", font, pygame.Color("white"), 200, 50)

    # Handle events (e.g., quit event)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

# Clean up and exit
pygame.quit()
