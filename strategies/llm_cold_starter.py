from openai import OpenAI

class LLMColdStartRecommender:
    def __init__(self, llm_client):
        self.llm = llm_client

    def recommend(self, user_features, candidate_items, top_n=5):
        # 构建 prompt
        prompt = self.build_prompt(user_features, candidate_items, top_n)
        response = self.llm.chat_completion(prompt)  # 或 call 方法
        # 解析 LLM 输出，返回 item id 列表
        recommended_items = self.parse_response(response)
        return recommended_items

    def build_prompt(self, user_features, candidate_items, top_n):
        items_str = "\n".join([f"{i['id']}: {i['title']}" for i in candidate_items])
        prompt = f""" 用户特征: {user_features} 可选 item:{items_str} 
                        请推荐最适合用户的 top-{top_n} item，输出 item id 列表。"""
        return prompt

    def parse_response(self, response):
        # 简单解析 JSON 或文本
        return [int(x) for x in response.strip().split(",")]
