from queue import Empty
from collections import deque

import random
import database

# Data Structure - Queue
class Playlist:
    MAX_SIZE = 100

    def __init__(self):
        self.queue_collection = set()
        self.front_data = 0          # First element of the queue.
        self.size = 0                # Current elements inside of the list.

        self._queue = deque(maxlen=self.MAX_SIZE)
        
        self._mysql_database = database.Database()
        try:
            
            self._music_url = self._mysql_database.fetch_music_url()
            self._music_title = ""
        except BaseException as e: 
            print(e)

        self.enqueue_music_url()
    
    # ----------------------------------------
    # Public Methods
    # ----------------------------------------

    def enqueue_music_url(self):
        return self._queue.append(self._music_url) 

    def dequeue_music_url(self):
        deque_url = [url[0] for url in self._queue.pop()]
        self.music_title = self._mysql_database.fetch_music_title(deque_url[0])
        print("Current song: ", self.music_title[0])

        return deque_url[0]

    def shuffle_queue(self):
        return random.shuffle(self._queue)

    def print_current_song_title(self):
        return self._music_title
    
    def print_queue_pop(self):
        print(self._queue.pop())

    def play_next_song(self):
        pass

    # ----------------------------------------
    # Private Methods
    # ----------------------------------------

if __name__ == "__main__":
    playlist = Playlist()
    
    # print(playlist.dequeue_music_title())
    