#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for i in range(len(tickets)):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
    source = "NONE"
    destination = hash_table_retrieve(hashtable, source)
    index = 0
    while destination != "NONE":
        destination = hash_table_retrieve(hashtable, source)
        route[index] = destination
        index += 1
        source = destination
    print(route)
    return route
