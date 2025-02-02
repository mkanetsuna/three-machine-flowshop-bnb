from itertools import permutations
# Q. itertoolは
from math import inf

def simulate_schedule(jobs, start_times=(0, 0, 0)):
    """
    現在の各機械の完了時刻（tA, tB, tC）から、
    ジョブ列 jobs を順次処理した場合の最終時刻をシミュレーションする。
    """
    tA, tB, tC = start_times
    for job in jobs:
        tA = tA + job.pA
        tB = max(tA, tB) + job.pB
        tC = max(tB, tC) + job.pC
    return (tA, tB, tC)

def compute_lower_bound(start_times, remaining_jobs):
    """
    現在の部分スケジュールの完了時刻 start_times から、
    残りのジョブ列 remaining_jobs の順序全列挙により、最良延長（最小の最終時刻）を下界として返す。
    """
    if not remaining_jobs:
        return start_times[2]
    best = inf
    for perm in permutations(remaining_jobs):
        final_times = simulate_schedule(perm, start_times)
        if final_times[2] < best:
            best = final_times[2]
    return best

def branch_and_bound(jobs, partial_sequence, remaining_indices, current_times, best_solution):
    """
    分枝限定法による探索
      - jobs: Job オブジェクトのリスト
      - partial_sequence: 現在確定しているジョブのインデックス列
      - remaining_indices: 未確定のジョブのインデックス（リスト）
      - current_times: 現在の各機械の完了時刻 (tA, tB, tC)
      - best_solution: {"sequence": best_sequence, "makespan": best_makespan}
    """
    if not remaining_indices:
        # 完全なスケジュールが得られた場合
        makespan = current_times[2]
        if makespan < best_solution["makespan"]:
            best_solution["makespan"] = makespan
            best_solution["sequence"] = partial_sequence.copy()
        return

    # 未確定ジョブの順序全列挙による下界計算
    remaining_jobs = [jobs[i] for i in remaining_indices]
    lb = compute_lower_bound(current_times, remaining_jobs)
    if lb >= best_solution["makespan"]:
        # 下界が既知の最良解以上ならば、この枝は探索しない
        return

    # 各未確定ジョブについて順序を拡張
    for i in remaining_indices:
        job = jobs[i]
        new_times = simulate_schedule([job], current_times)
        new_partial = partial_sequence + [i]
        new_remaining = remaining_indices.copy()
        new_remaining.remove(i)
        branch_and_bound(jobs, new_partial, new_remaining, new_times, best_solution)

def solve_flowshop(jobs):
    """
    分枝限定法で最適ジョブ順序と最小メイクスパンを求める
    """
    best_solution = {"sequence": None, "makespan": inf}
    all_indices = list(range(len(jobs)))
    branch_and_bound(jobs, [], all_indices, (0, 0, 0), best_solution)
    return best_solution
