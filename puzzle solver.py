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


def show(grid):
    print("")
    for row in grid:
        line = "  |"
        for v in row:
            line += f" {'_' if v==0 else v}"
        line += " |"
        print(line)
    print("")


def print_steps(path):
    print(f"\n  solved in {len(path)-1} move(s)\n")
    for i, s in enumerate(path):
        if i==0:
            print("  start:")
        else:
            print(f"\n  step {i} - {s['move']}")
        show(s["grid"])


def read_puzzle():
    print("\n  enter the puzzle one row at a time (use 0 for blank)")
    print("  example row: 1 2 3\n")
    grid = []
    seen = set()
    for i in range(3):
        while True:
            raw = input(f"  row {i+1}: ").strip().split()
            if len(raw) != 3:
                print("  need exactly 3 numbers")
                continue
            try:
                row = list(map(int, raw))
            except:
                print("  only integers please")
                continue
            if not all(0<=x<=8 for x in row):
                print("  numbers must be 0-8")
                continue
            if any(x in seen for x in row):
                print("  duplicate number, try again")
                continue
            seen.update(row)
            grid.append(row)
            break
    return grid


# some puzzles to test with
PRESETS = {"1": {"label": "easy   (1 move)",  "grid": [[1,2,3],[4,5,6],[7,0,8]]},
    "2": {"label": "medium (10 moves)","grid": [[1,2,3],[5,0,6],[4,7,8]]},
    "3": {"label": "hard   (20 moves)","grid": [[8,1,3],[4,0,2],[7,6,5]]},
    "4": {"label": "expert (26 moves)","grid": [[8,6,7],[2,5,4],[3,0,1]]},}


def main():
    print("\n")
    print("   8-puzzle solver  |  A* search")
    print("")

    print("  [1] pick a preset")
    print("  [2] enter your own")
    print("  [3] quit")

    c = input("\n  choice: ").strip()

    if c=="3":
        print("\n  bye!\n")
        return

    if c=="1":
        print()
        for k,v in PRESETS.items():
            print(f"  [{k}] {v['label']}")
        pick= input("\n  choice: ").strip()
        if pick not in PRESETS:
            print("  invalid, exiting")
            return
        grid= PRESETS[pick]["grid"]

    elif c=="2":
        grid = read_puzzle()

    else:
        print("  invalid, exiting")
        return

    print("\n  your puzzle:")
    show(grid)

    if not can_solve(grid):
        print("\n  this configuration has no solution (odd inversions)\n")
        return

    print("\n  working on it...")
    result= solve(grid)

    if not result:
        print("  no solution found")
        return

    path=get_path(result)

    print(f"\n  done! optimal solution = {len(path)-1} moves")
    print(f"  initial heuristic (manhattan) = {heuristic(to_tuple(grid))}")

    see = input("\n  show steps? [y/n]: ").strip().lower()
    if see=="y":
        print_steps(path)
    else:
        moves = [s["move"] for s in path if s["move"]]
        print("\n  moves: " + " -> ".join(moves))

    print("\n \n")


if __name__ == "__main__":
    main()
