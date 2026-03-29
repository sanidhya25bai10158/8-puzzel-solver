import heapq

# goal state - where every tile should end up
GOAL_GRID = ((1, 2, 3),(4, 5, 6),(7, 8, 0))

# where each number belongs in the final state
GOAL_POS = {1: (0,0),2: (0,1),3: (0,2),4: (1,0),5: (1,1),6: (1,2),7: (2,0),8: (2,1),0: (2,2)}

# 0 is the blank tile, these are the 4 directions it can slide
DIRECTIONS = {"UP":    (-1, 0), "DOWN":  ( 1, 0), "LEFT":  ( 0,-1), "RIGHT": ( 0, 1),}


def to_tuple(grid):
    return tuple(tuple(r) for r in grid)


def find_zero(grid):
    for r in range(3):
        for c in range(3):
            if grid[r][c]==0:
                return r,c


def get_moves(grid):
    # returns all valid next states as a dict {direction: new_grid}
    result = {}
    r,c=find_zero(grid)
    for d, (dr, dc) in DIRECTIONS.items():
        nr,nc=r+dr,c+dc
        if 0<=nr<3 and 0<=nc<3:
            g=[list(row) for row in grid]
            g[r][c],g[nr][nc]=g[nr][nc],g[r][c]
            result[d]=to_tuple(g)
    return result


def heuristic(grid):
    # to find most efficient path by calculating the path and total cost alltogether 
    dist=0
    for r in range(3):
        for c in range(3):
            tile=grid[r][c]
            if tile!=0:
                gr,gc=GOAL_POS[tile]
                dist+=abs(r - gr)+abs(c - gc)
    return dist


def solve(start):
    start = to_tuple(start)

    # each state stored as a plain dict, easier to trace back later
    init = {"grid": start,"g": 0,"h": heuristic(start),"parent": None,"move": None}
    init["f"]=init["g"]+init["h"]

    heap=[(init["f"],0,init)]
    visited={}
    count=0

    while heap:
        _, _, curr = heapq.heappop(heap)

        if curr["grid"]==GOAL_GRID:
            return curr

        if curr["grid"] in visited and visited[curr["grid"]] <=curr["g"]:
            continue
        visited[curr["grid"]] = curr["g"]

        for move, ngrid in get_moves(curr["grid"]).items():
            ng = curr["g"]+1
            nh = heuristic(ngrid)
            if ngrid in visited and visited[ngrid]<= ng:
                continue
            child = {"grid": ngrid,"g": ng,"h": nh,"f": ng + nh,"parent": curr,"move": move}
            count+=1
            heapq.heappush(heap,(child["f"], count, child))

    return None


def get_path(end_state):
    path=[]
    node=end_state
    while node:
        path.append(node)
        node=node["parent"]
    path.reverse()
    return path


def can_solve(grid):
    # a puzzle is only solvable if inversions are even
    # an inversion = bigger number appears before smaller one in the flat list
    flat= [x for row in grid for x in row if x != 0]
    inv=0
    for i in range(len(flat)):
        for j in range(i+1,len(flat)):
            if flat[i]>flat[j]:
                inv += 1
    return inv % 2 == 0
