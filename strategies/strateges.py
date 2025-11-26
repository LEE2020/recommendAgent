# 4. 基础策略类

import pandas as pd
import numpy as np

class BaseStrategy:
    def recommend(self, user, items, k=5):
        # 默认返回随机推荐
        return items.sample(k)

class HotStrategy(BaseStrategy):
    def recommend(self, user, items, k=5):
        return items.sort_values(by='hot', ascending=False).head(k)

class TagMatchStrategy(BaseStrategy):
    def recommend(self, user, items, k=5):
        matched = items[items['tag'] == user['interest']]
        if len(matched) < k:
            matched = pd.concat([matched, items.sample(k - len(matched))])
        return matched.sample(k)

class SimpleCFStrategy(BaseStrategy):
    def recommend(self, user, items, k=5):
        # 简单随机打分 + 兴趣加权
        scores = items['hot'] + (items['tag'] == user['interest']) * 0.5
        return items.assign(score=scores).sort_values(by='score', ascending=False).head(k)

