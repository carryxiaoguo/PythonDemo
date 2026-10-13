import os

from typing import Dict, List, Any

from dotenv import load_dotenv
from openai import OpenAI

# 加载env配置文件
load_dotenv()
# 智能体经典范式构件  调用api接口，流式输出 无存储记忆 最经典的一个智能体范式ReAct (Reason + Act)
"""
在ReAct诞生之前，主流的方法可以分为两类：一类是“纯思考”型，如思维链 (Chain-of-Thought)，它能引导模型进行复杂的逻辑推理，
但无法与外部世界交互，容易产生事实幻觉；另一类是“纯行动”型，模型直接输出要执行的动作，但缺乏规划和纠错能力。
ReAct的巧妙之处在于，它认识到思考与行动是相辅相成的。思考指导行动，而行动的结果又反过来修正思考。
为此，ReAct范式通过一种特殊的提示工程来引导模型，使其每一步的输出都遵循一个固定的轨迹：
    Thought (思考)： 这是智能体的“内心独白”。它会分析当前情况、分解任务、制定下一步计划，或者反思上一步的结果。
    Action (行动)： 这是智能体决定采取的具体动作，通常是调用一个外部工具，例如 Search['华为最新款手机']。
    Observation (观察)： 这是执行Action后从外部工具返回的结果，例如搜索结果的摘要或API的返回值。
"""
SYSTEM_PROMPT = """你是一个搜索问答助手。请根据用户问题提供精准答案。
必须严格以 JSON 格式返回，不要包含任何 markdown 标记或其他废话：
{
  "direct_answer": "最直接的答案（如果没有则为null）",
  "key_points": ["要点1", "要点2"], 
  "source_summary": "信息来源的简要说明"
}"""


class HelloAgentLLM:
    """
    为本书 "Hello Agents" 定制的LLM客户端。
    它用于调用任何兼容OpenAI接口的服务，并默认使用流式响应。
   """

    def __init__(self, model: str = None, api_key: str = None, base_url: str = None, timeout: int = None):
        """
        初始化客户端。优先使用传入参数，如果未提供，则从环境变量加载。
        """
        self.model = model or os.getenv("MODEL_ID")
        api_key = api_key or os.getenv("API_KEY")
        base_url = base_url or os.getenv("BASE_URL")
        timeout = timeout or os.getenv("TIMEOUT", 60)
        # 校验
        if not all([self.model, api_key, base_url]):
            raise ValueError("模型ID,模型密钥以及模型地址必须提供，或放在env文件里")
        # 创建客户端实例
        self.client = OpenAI(api_key=api_key, base_url=base_url, timeout=timeout)

    def think(self, message: List[Dict[str, str]], temperature: float = 0) -> str:
        """
        调用模型思考，并返回相应
        """
        print(f"正在调用:{self.model}模型.....")
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                temperature=temperature,
                messages=message,
                stream=True,
            )
            # 处理流式相应
            print("调用大模型正常")
            collected_chunk = []
            # 遍历流式响应生成器。每次迭代获取一个 SSE (Server-Sent Events) 数据块。
            for chunk in response:
                # 安全检查。某些 chunk 可能不包含有效 choices
                if not chunk.choices:
                    continue
                content = chunk.choices[0].delta.content or ""
                print(content, end="", flush=True)  # flush=True 关键参数，强制立即刷新输出缓冲区，实现真正的"逐字/逐词"实时显示效果
                collected_chunk.append(content)
            print()  # 流式结束后换行
            return " ".join(collected_chunk)
        except Exception as e:
            print(f"调用LLM模型失败,{e}")
            return None

    def search(self, query: str) -> str:
        """
        一个基于qwen3.8网页搜索引擎工具，可以用serpApi代替，因为qwen3.8支持网页搜索，为了学习。
        """
        print(f"正在使用{self.model}模型，进行网页搜索")
        # 如果用serpApi需要env注入和密钥验证，这里不做判断
        try:
            response = self.client.completions.create(model=self.model,
                                                      message=[{"role": "system", "content": SYSTEM_PROMPT},
                                                               {"role": "user", "content": query}],
                                                      response_format={"type": "json_object"})
            import json
            result = json.loads(response.choices[0].message.content)
            # 智能解析
            # 此时的解析逻辑变成了确定性的字典操作，等同于 answer_box
            if result.get("direct_answer"):
                return result["direct_answer"]
            if result.get("key_points"):
                return "\n".join(result["key_points"])
            return f"对不起，没有找到关于 '{query}' 的信息。"
        except Exception as e:
            print(f"搜索时发生错误:{e}")


# --- 客户端使用示例 ---
if __name__ == "__main__":
    try:
        agent = HelloAgentLLM()
        exmpleMessage = [
            {"role": "system", "content": "You are a helpful assistant that writes Python code."},
            {"role": "user", "content": "写一个快速排序算法"}
        ]
        print("调用大模型")
        agent_think = agent.think(exmpleMessage)
        if agent_think:
            print("\n\n--- 完整模型响应 ---")
            print(agent_think)
    except Exception as e:
        print(e)



 
class ToolExecuto:
    """
    一个工具执行器，负责管理和执行工具。
    """
    def __init__(self):
        self.tools:Dict[str,Dict[str, Any]] = {}
    def register_tool(self,name:str,description:str,func:callable):
        """
        向工具箱注册一个新工具
        """
        if name in self.tools:
            print(f"{self.tools}工具已经存在，禁止重复添加")
        self.tools[name] = {"description": description, "func": func}
        print(f"工具 '{name}' 已注册。")

    def getTool(self, name: str) -> callable:
        """
        根据名称获取一个工具的执行函数。
        """
        return self.tools.get(name, {}).get("func")

    def getAvailableTools(self) -> str:
        """
        获取所有可用工具的格式化描述字符串。
        """
        return "\n".join([
            f"- {name}: {info['description']}"
            for name, info in self.tools.items()
        ])