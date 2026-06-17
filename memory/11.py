vector1 = [1, 0, 1]  # 代表"猫"
vector2 = [1, 1, 0]  # 代表"狗"

# 2. 计算点积
def dot_product(vec1, vec2):
    return sum(a * b for a, b in zip(vec1, vec2))

similarity = dot_product(vector1, vector2)
print(f"猫和狗的词向量相似度为: {similarity}")