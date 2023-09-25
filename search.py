#!./.venv/bin/python3

import sqlite3, json

from colorama import Fore, Style
printi = lambda *a, **kw: print(f' {Style.BRIGHT}[{Fore.CYAN}i{Fore.RESET}]{Style.RESET_ALL}', *a, **kw)
printe = lambda *a, **kw: print(f' {Style.BRIGHT}[{Fore.LIGHTRED_EX}-{Fore.RESET}]', *a, **kw)
prints = lambda *a, **kw: print(f' {Style.BRIGHT}[{Fore.LIGHTGREEN_EX}+{Fore.RESET}]', *a, **kw)

# Function to create magnet links
def create_magnet_link(hash_value):
    return f'magnet:?xt=urn:btih:{hash_value}'

class Search:
    def __init__(self):
        printi(f"Connecting to database...")
        self.conn = sqlite3.connect('./rarbg_db.sqlite')
        if not self.conn is None:

            # Retrieve data from the 'items' table
            printi('Loading torrents from database...')
            self.conn.execute(f"SELECT * from items")

    def search_database(self, query):
        try:
            words = query.split(" ")
            final_query = "LIKE '%" + "%' AND title LIKE '%".join(words) + "%'"
            resp = self.conn.execute(f"SELECT id,title,hash,size,dt,cat FROM items WHERE title {final_query}")
            resp_data = resp.fetchall()
            # Create a list to store the magnet links
            torrents = []
            
            # Generate magnet links
            for id, title, hash, size, dt, cat in resp_data:
                if not size: size = 0
                torrent = {
                    'id': id,
                    'hash': hash,
                    'title': title,
                    'dt': dt,
                    'category': cat,
                    'size': size,
                    'magnet_link': create_magnet_link(hash)
                    }
                    
                torrents.append(torrent)
            return torrents
        except sqlite3.Error as e:
            print("SQLite error:", e)

try:
    #query = input('?> ')
    search = Search()
    while True:   
        search_query = input('Search ?> ')
        if '.exit' == search_query: 
            printe(f"Exiting")
            exit(1)
        torrents = search.search_database(query=search_query)
        if len(torrents) > 0:
            printi("Matching torrents:")
            for torrent in torrents:
                prints(f"\t{torrent['title']}(Size: {round(int(torrent['size'])/125000000,2)} GB)\n\t    {torrent['magnet_link']}")
            printi(f"Torrents Found: {len(torrents)}")
        else:
            printe(f"No torrents found")
except KeyboardInterrupt as ke:
    printe(f"Exiting")
    exit(1)