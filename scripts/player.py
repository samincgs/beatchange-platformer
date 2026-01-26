import pygame

class Player:
    def __init__(self):
        self.x = 10
        self.y = 200
        self.speed = 200
        self.direction = 1  # 1 for right, -1 for left
        self.scale_x = 2
        self.scale_y = 2
        
        # Create simple colored rectangles for now (placeholder for images)
        self.width = 32
        self.height = 32
        self.color = (255, 255, 255)  # White color for player
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        dir_x = 0
        
        if keys[pygame.K_d]:  # Move right
            dir_x += 1
        if keys[pygame.K_a]:  # Move left
            dir_x -= 1
            
        if dir_x != 0:
            self.direction = dir_x
            
        self.x += dir_x * self.speed * dt
        
    def draw(self, screen):
        # Draw player as a rectangle (placeholder for sprite)
        draw_width = self.width * self.scale_x
        draw_height = self.height * self.scale_y
        
        # Flip direction if facing left
        if self.direction == -1:
            pygame.draw.rect(screen, self.color, 
                           (self.x - draw_width//2, self.y - draw_height//2, draw_width, draw_height))
        else:
            pygame.draw.rect(screen, self.color, 
                           (self.x - draw_width//2, self.y - draw_height//2, draw_width, draw_height))