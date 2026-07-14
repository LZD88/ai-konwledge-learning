from langchain_classic.chains.summarize.map_reduce_prompt import prompt_template
from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import PromptTemplate

#1.创建客户端
llm = Tongyi(model="qwen-max")
  
#2.创建提示词模板
prompt_template = PromptTemplate.from_template(
    "假设你是一个{expert}专家，请你解释一下{content}是什么。"
)
chain = prompt_template | llm
result = chain.stream(input={"expert": "AI", "content": "Langgraph"})
for chunk in result:
    print(chunk,end="",flush=True)