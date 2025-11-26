
# 1. 模拟用户数据
import numpy as np
import pandas as pd

def is_cold_user(user):
    # 简单示例：没有历史点击记录或新用户
    return 'history_clicks' not in user or len(user['history_clicks']) == 0

def is_cold_item(item):
    # 长尾或新上架 item
    return item['hot'] < 0.1


num_users = 1000
user_ids = np.arange(num_users)
user_ages = np.random.randint(18, 50, size=num_users)
user_genders = np.random.choice(['M','F'], size=num_users)
user_interests = np.random.choice(['tech','sports','music'], size=num_users)
# 2. 生成 history_clicks，部分为空表示冷启动用户
history_clicks = []
for _ in range(num_users):
    if np.random.rand() < 0.3:  # 30% 用户冷启动
        history_clicks.append([])  # 没有历史点击
    else:
        num_clicks = np.random.randint(1, 10)  # 历史点击数
        clicks = np.random.randint(0, 200, size=num_clicks).tolist()  # 随机 item_id
        history_clicks.append(clicks)

users = pd.DataFrame({
    'user_id': user_ids,
    'age': user_ages,
    'gender': user_genders,
    'interest': user_interests,
    'history_clicks': history_clicks
})

# 2. 模拟内容数据
num_items = 200
item_ids = np.arange(num_items)
item_types = np.random.choice(['article','video','product'], size=num_items)
item_tags = np.random.choice(['tech','sports','music'], size=num_items)
item_hot = np.random.rand(num_items)

items = pd.DataFrame({
    'item_id': item_ids,
    'type': item_types,
    'tag': item_tags,
    'hot': item_hot
})