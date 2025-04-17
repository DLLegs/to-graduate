import numpy as np
import pandas as pd
from scipy.optimize import linprog
import matplotlib.pyplot as plt
from collections import namedtuple

# ------------------------------
# 1. 구조 정의
# ------------------------------
Job = namedtuple('Job', ['name', 'cpu', 'gpu', 'remain_time', 'deadline'])
Cluster = namedtuple('Cluster', ['name', 'cpu', 'gpu', 'carbon', 'power_slope'])

# ------------------------------
# 2. 하드코딩된 입력값
# ------------------------------
T = 5  # 타임 슬롯 수
jobs = [
    Job("job1", cpu=2, gpu=1, remain_time=3, deadline=4),
    Job("job2", cpu=1, gpu=2, remain_time=2, deadline=3),
    Job("job3", cpu=3, gpu=1, remain_time=1, deadline=2),
]
clusters = [
    Cluster("clusterA", cpu=5, gpu=5, carbon=[1.2]*T, power_slope=0.05),
    Cluster("clusterB", cpu=4, gpu=4, carbon=[1.0]*T, power_slope=0.04),
]

N, M = len(jobs), len(clusters)
total_vars = N * M * T

# ------------------------------
# 3. 목적 함수 계산
# ------------------------------
obj1, obj2, obj3 = np.zeros(total_vars), np.zeros(total_vars), np.zeros(total_vars)

for i, job in enumerate(jobs):
    for j, cluster in enumerate(clusters):
        for t in range(T):
            idx = i * M * T + j * T + t
            lateness = max(1, t + job.remain_time - job.deadline)
            obj3[idx] = 1 / lateness
            obj2[idx] = 1 / (t + job.remain_time)
            score = 0
            for tt in range(t, min(T, t + job.remain_time)):
                score += job.gpu / (cluster.gpu * cluster.carbon[tt] * cluster.power_slope)
            obj1[idx] = score

# ------------------------------
# 4. 목적 함수 결합 (정규화 + 가중치)
# ------------------------------
theta1 = np.linalg.norm(obj1)
theta2 = np.linalg.norm(obj2)
theta3 = np.linalg.norm(obj3)
omega1, omega2, omega3 = 1.0, 1.0, 1.0

obj_total = omega1 * obj1 / theta1 + omega2 * obj2 / theta2 + omega3 * obj3 / theta3

# ------------------------------
# 5. 제약 조건 설정
# ------------------------------
A_eq, b_eq = [], []
for i in range(N):
    row = np.zeros(total_vars)
    for j in range(M):
        for t in range(T):
            row[i * M * T + j * T + t] = 1
    A_eq.append(row)
    b_eq.append(1)

A_ub, b_ub = [], []

# 각 클러스터-시간대별 CPU/GPU 자원 제약
for j, cluster in enumerate(clusters):
    for t in range(T):
        row_cpu, row_gpu = np.zeros(total_vars), np.zeros(total_vars)
        for i, job in enumerate(jobs):
            for tt in range(max(0, t - job.remain_time + 1), t + 1):
                if t < tt + job.remain_time:
                    row_cpu[i * M * T + j * T + tt] += job.cpu
                    row_gpu[i * M * T + j * T + tt] += job.gpu
        A_ub.append(row_cpu)
        b_ub.append(cluster.cpu)
        A_ub.append(row_gpu)
        b_ub.append(cluster.gpu)

# 변수 범위: 0 ~ 1
bounds = [(0, 1) for _ in range(total_vars)]

# ------------------------------
# 6. LP 최적화 수행
# ------------------------------
res = linprog(
    c=-obj_total,
    A_ub=A_ub, b_ub=b_ub,
    A_eq=A_eq, b_eq=b_eq,
    bounds=bounds,
    method='highs'
)

# ------------------------------
# 7. 결과 해석 및 시각화
# ------------------------------
decision = res.x.reshape((N, M, T))
assignments = []
for i in range(N):
    best = np.unravel_index(np.argmax(decision[i]), (M, T))
    assignments.append((jobs[i].name, clusters[best[0]].name, best[1]))

# 표 출력
df = pd.DataFrame(assignments, columns=["Job", "Assigned Cluster", "Start Time Slot"])
print(df)

# 히트맵 시각화
assign_matrix = np.zeros((N, M * T))
for i in range(N):
    assign_matrix[i, :] = decision[i].flatten()

plt.figure(figsize=(10, 4))
plt.title("Job-Cluster-Time Assignment Matrix")
plt.imshow(assign_matrix, cmap='viridis', aspect='auto')
plt.xlabel("Cluster-Time Index")
plt.ylabel("Job Index")
plt.colorbar(label="Assignment Weight (x)")
plt.xticks(range(M*T), [f"{clusters[j%M].name}-t{j//M}" for j in range(M*T)], rotation=90)
plt.yticks(range(N), [job.name for job in jobs])
plt.tight_layout()
plt.show()
