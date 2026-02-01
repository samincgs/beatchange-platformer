import pygame
import random
from scripts.utils import load_imgs
import opensimplex


class Mapgen:
    def __init__(self, seed=None):
        self.seed = seed or random.randint(0, 10000)
        random.seed(self.seed)
        self.noise = opensimplex.OpenSimplex(seed=self.seed)
        
        self.tile_size = 32
        self.chunk_width = 25
        self.chunk_height = 19
        
        # Load terrain tiles
        self.grass_tiles = load_imgs('data/images/grass/')
        self.sand_tiles = load_imgs('data/images/sand/')
        self.decor_tiles = load_imgs('data/images/decor/')
        
    def generate_chunk(self, chunk_x):
        chunk_data = []
        for y in range(self.chunk_height):
            row = []
            for x in range(self.chunk_width):
                world_x = chunk_x * self.chunk_width + x
                height_noise = self.noise.noise2d(world_x * 0.05, 0)
                detail_noise = self.noise.noise2d(world_x * 0.2, 0)
                
                tile_type = None
                
                # Ground level (bottom of screen)
                if y >= 16:
                    if height_noise > 0.3:
                        tile_type = 'grass'
                    elif height_noise > 0:
                        tile_type = 'sand'
                    else:
                        tile_type = None
                        
                # Platform level
                elif 12 <= y <= 15:
                    if height_noise > 0.1:
                        tile_type = 'grass'
                    else:
                        tile_type = None
                        
                # Upper platforms (sparse)
                elif y < 12:
                    if detail_noise > 0.7:
                        tile_type = 'grass'
                    else:
                        tile_type = None

                row.append(tile_type)
            chunk_data.append(row)
        return chunk_data
    
    def get_tile_image(self, tile_type):
        """Get a random tile image for the given type"""
        if tile_type == 'grass' and self.grass_tiles:
            return random.choice(self.grass_tiles)
        elif tile_type == 'sand' and self.sand_tiles:
            return random.choice(self.sand_tiles)
        return None
    
    def render_chunk(self, chunk_data):
        """Render a chunk to a surface for performance"""
        surface = pygame.Surface((self.chunk_width * self.tile_size, self.chunk_height * self.tile_size), pygame.SRCALPHA)
        
        for y, row in enumerate(chunk_data):
            for x, tile_type in enumerate(row):
                if tile_type:
                    tile_image = self.get_tile_image(tile_type)
                    if tile_image:
                        surface.blit(tile_image, (x * self.tile_size, y * self.tile_size))
        
        return surface


class Chunk:
    def __init__(self, x, chunk_data, mapgen):
        self.x = x
        self.tiles = chunk_data
        self.surface = mapgen.render_chunk(chunk_data)
        self.width = mapgen.chunk_width * mapgen.tile_size
        self.height = mapgen.chunk_height * mapgen.tile_size


class ChunkManager:
    def __init__(self, mapgen):
        self.chunks = {}
        self.mapgen = mapgen
        self.load_distance = 3  # Number of chunks to keep loaded on each side
        
    def update(self, player_x):
        """Load/unload chunks based on player position"""
        chunk_x = int(player_x // (self.mapgen.chunk_width * self.mapgen.tile_size))
        
        # Load chunks around player
        for offset in range(-self.load_distance, self.load_distance + 1):
            x = chunk_x + offset
            if x not in self.chunks:
                chunk_data = self.mapgen.generate_chunk(x)
                self.chunks[x] = Chunk(x, chunk_data, self.mapgen)
        
        # Unload distant chunks
        to_remove = [x for x in self.chunks.keys() if abs(x - chunk_x) > self.load_distance + 1]
        for x in to_remove:
            del self.chunks[x]
    
    def get_chunks_in_view(self, camera_x, camera_y, view_width, view_height):
        """Get chunks that are visible in the current view"""
        visible_chunks = []
        chunk_width = self.mapgen.chunk_width * self.mapgen.tile_size
        
        for chunk in self.chunks.values():
            chunk_screen_x = chunk.x * chunk_width - camera_x
            
            # Check if chunk is visible (with some margin)
            if -chunk_width <= chunk_screen_x <= view_width:
                visible_chunks.append(chunk)
        
        return visible_chunks

