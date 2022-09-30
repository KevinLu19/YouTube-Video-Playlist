from queue import Empty

import random
import database

# Data Structure - Queue
class Playlist:
    def __init__(self):
        self.queue_collection = set()
        self.front_data = 0          # First element of the queue.
        self.size = 0                # Current elements inside of the list.

        # self.sqlite3_database = database.Database()
        self.mysql_database = database.Database()

    def add_entry(self, music_url):
        try:
            self.queue_collection.add(music_url)
            print(f"Added {music_url} to the collection.")
        except BaseException as e:
            print(e)

    def print_collection(self):
        self.sqlite3_database.fetch_entry()

    def remove_current_music_entry(self):
        if None in self.queue_collection:
            self.update_playlist()
    
    def update_playlist(self):
        self.queue_collection = [music_url for music_url in self.queue_collection if music_url is not None]

        return self.queue_collection

    def is_empty(self):
        return self.size == True

    def first_element(self):
        if self.is_empty:
            raise Empty("Problem retrieving first element. Could be queue is empty.")
        
        return self.queue_collection[self.front_data]

    def dequeue(self):
        if self.is_empty:
            raise Empty("Queue is empty.")

        first_dequeue_data = self.queue_collection[self.front_data]
        self.queue_collection[self.front_data] = None               # House keeping. Garbage Collection.
        self.front_data = (self.front_data + 1) % len(self.queue_collection)
        self.size -= 1

        return first_dequeue_data

    def shuffle_queue(self):
        return random.shuffle(self.queue_collection)
    