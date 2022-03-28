import time
from multiprocessing import Lock, Process
from typing import Dict, List


def f(
    s: str,  # printしたい文字列
    id: str,  # （例えば）ユーザーID
    wait_seconds: int,  # 排他処理や並列処理が動作していることを確認するために使う
    locks: Dict[str, Lock],  # ユーザーID単位で排他処理するためのLockを格納しているDict
    start: float,  # 親プロセスが開始した時間
):
    # ユーザー単位でそれぞれ排他処理する（守りたい処理順序があるときなど。）
    with locks[id]:
        try:
            with open(f"{id}.txt", "r") as filer:
                lines = filer.readlines()
        except FileNotFoundError as e:
            lines = []
        try:
            with open(f"{id}.txt", "w") as filew:
                time.sleep(wait_seconds)
                lines.append(f"{s}(通算{int(time.time() - start)}秒経過) ")
                print("".join(lines), file=filew)  # print()でfileにテキストを追記
        except Exception as e:
            with open(f"{id}_error.txt", "w") as ew:
                print(e, file=ew)


if __name__ == "__main__":
    threads: List[Process] = []

    # ユーザーIDごとに排他処理をするのに使うLockオブジェクトを保持する
    locks: Dict[str, Lock] = {
        "A": Lock(),
        "B": Lock(),
    }
    start = time.time()  # 処理経過時間計測開始

    # 実際どれが先に実行されるかはご機嫌次第。ここに書いた順とは限らない
    threads.append(Process(target=f, args=("A1", "A", 4, locks, start)))
    threads.append(Process(target=f, args=("A2", "A", 1, locks, start)))
    threads.append(Process(target=f, args=("B1", "B", 2, locks, start)))
    threads.append(Process(target=f, args=("B2", "B", 3, locks, start)))

    [t.start() for t in threads]
    [t.join() for t in threads]

    print("全部完了。")
