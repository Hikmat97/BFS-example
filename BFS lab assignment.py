from collections import deque

def bfs_shortest_path(graph, start, goal):
    # Track visited cities and the path leading to them
    visited = set()
    queue = deque([[start]])
    
    # If the start is the goal, return immediately
    if start == goal:
        return [start]
    
    while queue:
        # Get the current path
        path = queue.popleft()
        city = path[-1]
        
        # If the city is not visited
        if city not in visited:
            neighbors = graph[city]
            
            # Go through all neighboring cities
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                
                # If we found the goal city, return the path
                if neighbor == goal:
                    return new_path
                
                # Add the new path to the queue
                queue.append(new_path)
            
            # Mark the city as visited
            visited.add(city)
    
    # If no path is found
    return None

# Cities and their connections (graph representation)
cities_graph = {
    'Islamabad': ['Rawalpindi', 'Lahore', 'Peshawar'],
    'Rawalpindi': ['Islamabad', 'Peshawar', 'Quetta'],
    'Peshawar': ['Islamabad', 'Rawalpindi', 'Quetta'],
    'Lahore': ['Islamabad', 'Multan', 'Quetta'],
    'Multan': ['Lahore', 'Karachi', 'Quetta'],
    'Quetta': ['Rawalpindi', 'Peshawar', 'Multan', 'Karachi'],
    'Karachi': ['Multan', 'Quetta']
}

# Find the shortest path from Islamabad to Karachi
shortest_path = bfs_shortest_path(cities_graph, 'Islamabad', 'Karachi')
print("Shortest path:", shortest_path)
