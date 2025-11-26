import random

class EpsilonGreedyAgent:
    def __init__(self, num_strategies, epsilon=0.1):
        self.num_strategies = num_strategies
        self.epsilon = epsilon
        self.values = [0.0] * num_strategies  # 期望回报
        self.counts = [0] * num_strategies    # 每个策略选择次数

    def select_strategy(self):
        if random.random() < self.epsilon:
            # 随机选择
            return random.randint(0, self.num_strategies - 1)
        else:
            # 选择当前最优策略
            return self.values.index(max(self.values))

    def update(self, strategy_idx, reward):
        self.counts[strategy_idx] += 1
        n = self.counts[strategy_idx]
        value = self.values[strategy_idx]
        # 在线更新期望回报
        self.values[strategy_idx] = value + (reward - value)/n
