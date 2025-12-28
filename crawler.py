import urllib.request
import urllib.parse
import sys
import re
import time
from queue import SimpleQueue

BASE_URL = "https://ja.wikipedia.org/wiki/"

def get_pages(title):
    url = BASE_URL + urllib.parse.quote(title)
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "ja",
        "Accept-Charset": "utf-8"
    }
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        body = resp.read().decode("utf-8")

    links = []
    for m in re.findall(r'href="/wiki/([^:#"]+)"', body):
        name = urllib.parse.unquote(m)
        links.append(name)
    return links

def bfs(start, goal):
    que = SimpleQueue()
    que.put((start, None))
    checked = {start: None}

    while not que.empty():
        page, prev = que.get()

        if page == goal:
            break

        time.sleep(0.1)

        for nxt in get_pages(page):
            if nxt not in checked:
                checked[nxt] = page
                que.put((nxt, page))
                if nxt == goal:
                    return checked
    return checked

def bfs_with_dist(start, max_depth=3):
    que = SimpleQueue()
    que.put((start, 0))
    checked = {start: 0}

    while not que.empty():
        page, dist = que.get()
        if dist >= max_depth:
            print(f"{page} (distance: {dist})")
            continue

        time.sleep(0.1)
        for nxt in get_pages(page):
            if nxt not in checked:
                checked[nxt] = dist + 1
                que.put((nxt, dist+1))

def reconstruct_path(checked, start, goal):
    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = checked[cur]
    path.reverse()
    return path

# def main():
#     if len(sys.argv) != 3:
#         print(f"[USAGE] python {sys.argv[0]} START GOAL")
#         sys.exit(1)

#     start, goal = sys.argv[1], sys.argv[2]
#     checked = bfs(start, goal)
    
#     if goal in checked:
#         path = reconstruct_path(checked, start, goal)
#         print(" -> ".join(path))
#     else:
#         print("No path found.")

def main():
    if len(sys.argv) != 2:
        print(f"[USAGE] python {sys.argv[0]} START")
        sys.exit(1)

    start = sys.argv[1]
    bfs_with_distance(start, max_depth=3)

if __name__ == "__main__":
    main()
