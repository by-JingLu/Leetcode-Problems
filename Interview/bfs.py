from collections import deque

def is_sellser(name):
    return name[-1] == 'm'


def search_mango(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()

        if person not in searched:
            if is_sellser(person):
                print(f'{person} is mango seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    
    return False

    

graph = {}
graph['you'] = ['alice', 'bob', 'cindy']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['cindy'] = ['thom', 'jonny']
graph['peggy'] = []
graph['anuj'] = []
graph['thom'] = []
graph['jonny'] = []

print(search_mango('you'))
