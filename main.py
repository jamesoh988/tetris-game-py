import pygame
import sys
import random
from config import *

class Block:
    def __init__(self, shape_index, x, y):
        self.shape_index = shape_index
        self.shape_matrix = SHAPES[self.shape_index]
        self.color = COLORS[self.shape_index]
        self.x = int(x)
        self.y = int(y)
        self.rotation = 0

    def rotate(self):
        # Rotate 90 degrees clockwise
        old_matrix = self.shape_matrix
        rows = len(old_matrix)
        cols = len(old_matrix[0])
        rotated = [[old_matrix[rows - 1 - j][i] for j in range(rows)] for i in range(cols)]
        return rotated

    def draw(self, screen):
        for r_idx, row in enumerate(self.shape_matrix):
            for c_idx, val in enumerate(row):
                if val != 0:
                    pygame.draw.rect(screen, self.color,
                                     (GRID_TOP_LEFT_X + (self.x + c_idx) * GRID_SIZE,
                                      GRID_TOP_LEFT_Y + (self.y + r_idx) * GRID_SIZE,
                                      GRID_SIZE - 1, GRID_SIZE - 1))

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Python Tetris")
        self.clock = pygame.time.Clock()
        self.running = True
        self.block = None
        self.board = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.new_block()

        self.fall_time = 0
        self.fall_speed = 1000  # milliseconds (1 second initially)
        self.score = 0
        self.lines_cleared = 0
        self.level = 1
        
        # Initialize font for text rendering
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)

    def new_block(self):
        # Create a new block with a random shape
        shape_index = random.randint(0, len(SHAPES) - 1)
        self.block = Block(shape_index,
                           GRID_WIDTH / 2 - len(SHAPES[shape_index][0]) / 2, # Centered horizontally
                           0) # At the top of the grid

    def run(self):
        while self.running:
            dt = self.clock.get_time() # Time since last frame in milliseconds
            self.fall_time += dt

            self.events()
            self.update()
            self.draw()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_LEFT:
                    self.move_block(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    self.move_block(1, 0)
                elif event.key == pygame.K_DOWN:
                    self.move_block(0, 1)
                elif event.key == pygame.K_UP:
                    self.rotate_block()
                elif event.key == pygame.K_SPACE:
                    self.hard_drop()

    def update(self):
        if self.fall_time >= self.fall_speed:
            if not self.move_block(0, 1): # Move down by 1
                self.place_block()
                self.clear_lines()
                self.new_block()
                if self.check_collision(self.block, 0, 0):
                    self.running = False  # Game over
            self.fall_time = 0

    def move_block(self, dx, dy):
        if not self.check_collision(self.block, dx, dy):
            self.block.x += dx
            self.block.y += dy
            return True
        return False

    def draw(self):
        self.screen.fill(BLACK)
        self.draw_grid()
        self.draw_board()
        if self.block:
            self.block.draw(self.screen)
        self.draw_ui()
        pygame.display.flip()
    
    def draw_ui(self):
        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (20, 20))
        
        # Draw lines cleared
        lines_text = self.font.render(f"Lines: {self.lines_cleared}", True, WHITE)
        self.screen.blit(lines_text, (20, 60))
        
        # Draw level
        level_text = self.font.render(f"Level: {self.level}", True, WHITE)
        self.screen.blit(level_text, (20, 100))
        
        # Draw controls
        controls = [
            "Controls:",
            "Left/Right : Move",
            "Down : Soft drop", 
            "Up : Rotate",
            "Space : Hard drop",
            "Esc : Exit"
        ]
        
        for i, control in enumerate(controls):
            control_text = self.small_font.render(control, True, WHITE)
            self.screen.blit(control_text, (SCREEN_WIDTH - 200, 20 + i * 25))

    def check_collision(self, block, dx, dy):
        for r_idx, row in enumerate(block.shape_matrix):
            for c_idx, val in enumerate(row):
                if val != 0:
                    new_x = block.x + c_idx + dx
                    new_y = block.y + r_idx + dy
                    
                    # Check boundaries
                    if new_x < 0 or new_x >= GRID_WIDTH or new_y >= GRID_HEIGHT:
                        return True
                    
                    # Check collision with placed blocks (skip if new_y < 0 for spawn)
                    if new_y >= 0 and self.board[new_y][new_x] != 0:
                        return True
        return False

    def place_block(self):
        for r_idx, row in enumerate(self.block.shape_matrix):
            for c_idx, val in enumerate(row):
                if val != 0:
                    board_x = self.block.x + c_idx
                    board_y = self.block.y + r_idx
                    if 0 <= board_x < GRID_WIDTH and 0 <= board_y < GRID_HEIGHT:
                        self.board[board_y][board_x] = self.block.shape_index + 1

    def clear_lines(self):
        lines_to_clear = []
        for y in range(GRID_HEIGHT):
            if all(self.board[y][x] != 0 for x in range(GRID_WIDTH)):
                lines_to_clear.append(y)
        
        # Calculate score based on lines cleared
        if lines_to_clear:
            lines_count = len(lines_to_clear)
            # Scoring: 1 line = 100, 2 lines = 300, 3 lines = 500, 4 lines (Tetris) = 800
            score_values = {1: 100, 2: 300, 3: 500, 4: 800}
            self.score += score_values.get(lines_count, lines_count * 100) * self.level
            self.lines_cleared += lines_count
            
            # Increase level every 10 lines
            self.level = self.lines_cleared // 10 + 1
            
            # Increase falling speed with level (minimum 100ms)
            self.fall_speed = max(100, 1000 - (self.level - 1) * 100)
        
        for y in lines_to_clear:
            del self.board[y]
            self.board.insert(0, [0 for _ in range(GRID_WIDTH)])

    def draw_board(self):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if self.board[y][x] != 0:
                    color = COLORS[self.board[y][x] - 1]
                    pygame.draw.rect(self.screen, color,
                                   (GRID_TOP_LEFT_X + x * GRID_SIZE,
                                    GRID_TOP_LEFT_Y + y * GRID_SIZE,
                                    GRID_SIZE - 1, GRID_SIZE - 1))

    def draw_grid(self):
        # Vertical lines
        for i in range(GRID_WIDTH + 1):
            pygame.draw.line(self.screen, GRAY, (GRID_TOP_LEFT_X + i * GRID_SIZE, GRID_TOP_LEFT_Y), (GRID_TOP_LEFT_X + i * GRID_SIZE, GRID_TOP_LEFT_Y + GRID_HEIGHT * GRID_SIZE), 1)
        # Horizontal lines
        for i in range(GRID_HEIGHT + 1):
            pygame.draw.line(self.screen, GRAY, (GRID_TOP_LEFT_X, GRID_TOP_LEFT_Y + i * GRID_SIZE), (GRID_TOP_LEFT_X + GRID_WIDTH * GRID_SIZE, GRID_TOP_LEFT_Y + i * GRID_SIZE), 1)

    def rotate_block(self):
        old_matrix = self.block.shape_matrix
        self.block.shape_matrix = self.block.rotate()
        
        if self.check_collision(self.block, 0, 0):
            self.block.shape_matrix = old_matrix  # Revert if collision
        else:
            self.block.rotation = (self.block.rotation + 1) % 4

    def hard_drop(self):
        # Drop the block as far down as possible
        while not self.check_collision(self.block, 0, 1):
            self.block.y += 1
        
        # Place the block immediately and add hard drop score
        self.place_block()
        self.clear_lines()
        self.score += (GRID_HEIGHT - self.block.y) * 2  # 2 points per row dropped
        self.new_block()
        
        # Check for game over
        if self.check_collision(self.block, 0, 0):
            self.running = False


if __name__ == '__main__':
    game = Game()
    game.run()
