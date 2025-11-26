import numpy as np
import pandas as pd

class MultiSceneStrategyCombiner:
    def __init__(self, strategies, scenes, default_weights=None):
        self.strategies = strategies
        self.scenes = scenes
        self.weights = {scene: default_weights if default_weights else [1]*len(strategies)
                        for scene in scenes}

    def recommend(self, scene, user, items, k=5):
        rec_scores = pd.DataFrame({'item_id': items['item_id'], 'score': 0})
        weights = self.weights[scene]
        for strategy, weight in zip(self.strategies, weights):
            recs = strategy.recommend(user, items, k)
            rec_scores.loc[rec_scores['item_id'].isin(recs['item_id']), 'score'] += weight
        final_recs = rec_scores.sort_values(by='score', ascending=False).head(k)
        return items[items['item_id'].isin(final_recs['item_id'])]

class StrategyCombiner:
    def __init__(self, strategies, weights=None):
        self.strategies = strategies
        self.weights = weights if weights else [1]*len(strategies)

    def recommend(self, user, items, k=5):
        # 收集每个策略的推荐
        rec_scores = pd.DataFrame({'item_id': items['item_id'], 'score': 0})
        for strategy, weight in zip(self.strategies, self.weights):
            recs = strategy.recommend(user, items, k)
            rec_scores.loc[rec_scores['item_id'].isin(recs['item_id']), 'score'] += weight
        # 输出最终推荐 top-k
        final_recs = rec_scores.sort_values(by='score', ascending=False).head(k)
        return items[items['item_id'].isin(final_recs['item_id'])]

