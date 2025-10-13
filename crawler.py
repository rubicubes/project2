import sys
from queue import SimpleQueue
import re



def main():
    argc = len(sys.argv)
    # 追加
    if argc != 3:
        print(f"[USAGE] python {sys.argv[0]} START GOAL")
        sys.exit(0)

    start = sys.argv[1]
    goal = sys.argv[2]
  
if __name__ == "__main__":
    main()


base_url = "https://ja.wikipedia.org/wiki/"
title = start
url = base_url + urllib.parse.quote(title)
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "ja",
    "Accept-Charset": "utf-8",
}

req = urllib.request.Request(url, headers=headers, method="GET")
with urllib.request.urlopen(req) as resp:
    body = resp.read().decode("utf-8")
  
# キューは現在の記事とリンク元の記事を管理
que = SimpleQueue()
que.put((start, None))
checked = {}  # チェック済みなら、記事名をキー、リンク元の記事を値とする要素を持つ

# キューが空になるまで処理を継続
while not que.empty():
    # スロットリング
    time.sleep(0.1)

    # ノードの取り出し
    node = que.get()
    page, prev = node

    # 既にチェック済みの記事かどうかを調べる
    # !!! 実装する !!!
    if page in checked:
        continue
    # 未チェックの記事なら、リンクされた記事を取得
    next_pages = get_pages(page)

    # 新しい記事の中にゴールが見つかったら終了
    # !!! 実装する !!!
    if goal in next_pages:
        pass
    # 取得した記事名をキューに追加
    # !!! もう少し早くできる !!!
    for next_page in next_pages:
        que.put((next_page, page))
# 経路の取り出し
path = [goal]
# !!! 実装する !!!

# 結果の表示
print("")
print("Answer:")
print(" -> ".join(path))
