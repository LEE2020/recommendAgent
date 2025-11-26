
# 1. 模拟用户数据
import numpy as np
import pandas as pd

num_users = 1000
user_ids = np.arange(num_users)
user_ages = np.random.randint(18, 50, size=num_users)
user_genders = np.random.choice(['M','F'], size=num_users)
user_interests = np.random.choice(['tech','sports','music'], size=num_users)

users = pd.DataFrame({
    'user_id': user_ids,
    'age': user_ages,
    'gender': user_genders,
    'interest': user_interests
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