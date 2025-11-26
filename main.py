import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from strategies.strateges import BaseStrategy, HotStrategy, TagMatchStrategy, SimpleCFStrategy
from strategies.strategy_combiner import StrategyCombiner, MultiSceneStrategyCombiner
from agent.epsilon_greedy_agent import EpsilonGreedyAgent
import random
from data.data import users, items
from scenes.scene import scenes, scene_metrics

# 用户点击模拟函数
def simulate_click(user, item):
    # 简单规则：兴趣匹配加热度 + 随机噪声
    match = 1 if user['interest'] == item['tag'] else 0
    prob = 0.3 * match + 0.7 * item['hot']  # 简单线性组合
    return np.random.rand() < prob

# 5. 测试一轮推荐
strategies = [HotStrategy(), TagMatchStrategy(), SimpleCFStrategy()]
weights = [0.5, 1.0, 1.0]  # 权重可调
combiner = StrategyCombiner(strategies, weights)
num_strategies = 3
agents = {scene: EpsilonGreedyAgent(len(strategies), epsilon=0.2) for scene in scenes}
multi_combiner = MultiSceneStrategyCombiner(strategies, scenes)

num_rounds = 200
for round_idx in range(num_rounds):
    user = users.sample(1).iloc[0]
    scene = random.choice(scenes)
    
    agent = agents[scene]
    strategy_idx = agent.select_strategy()
    strategy = strategies[strategy_idx]
    
    recs = multi_combiner.recommend(scene, user, items, k=5)
    # 计算 reward，假设 reward = CTR
    clicks = sum(simulate_click(user, recs.iloc[i]) for i in range(len(recs)))
    reward = clicks / len(recs)
    
    agent.update(strategy_idx, reward)

    if (round_idx+1) % 20 == 0:
        print(f"Round {round_idx+1}, Scene: {scene}, Agent values: {agent.values}")
# 多场景结果可视化

for scene in scenes:
    plt.plot(agents[scene].values, label=scene)

plt.xlabel("Strategy Index")
plt.ylabel("Estimated Reward")
plt.title("Multi-Scene Agent Learned Values")
plt.legend()
plt.show()
