from langchain_community.llms.tongyi import Tongyi
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

class Person(BaseModel):
    name: str = Field(description="姓名")
    age: int = Field(description="年龄")

parser = JsonOutputParser(pydantic_object=Person)

# 在 Prompt 中注入格式要求
prompt = PromptTemplate(
    template="解析这段文字：{input}\n{format_instructions}",
    input_variables=["input"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)
llm = Tongyi(model="qwen-max")

chain = prompt | llm | parser
# 输出为 Python dict
print(chain.invoke({"input": "小明25岁"}))