# langchain_dashscope
提供阿里云灵积模型的langchain集成。

## 对话大模型可用的模型名称

  | 模型名 | 模型简介 | 模型输入输出限制 |
  | --- | --- | --- |
  | qwen-turbo | 通义千问超大规模语言模型，支持中文、英文等不同语言输入。 | 模型支持8k tokens上下文，为了保证正常的使用和输出，API限定用户输入为6k tokens。 |
  | qwen-plus | 通义千问超大规模语言模型增强版，支持中文、英文等不同语言输入。 | 模型支持32k tokens上下文，为了保证正常的使用和输出，API限定用户输入为30k tokens。 |
  | qwen-max | 通义千问千亿级别超大规模语言模型，支持中文、英文等不同语言输入。随着模型的升级，qwen-max将滚动更新升级，如果希望使用稳定版本，请使用qwen-max-1201。 | 模型支持8k tokens上下文，为了保证正常的使用和输出，API限定用户输入为6k tokens。 |
  | qwen-max-1201 | 通义千问千亿级别超大规模语言模型，支持中文、英文等不同语言输入。该模型为qwen-max的快照稳定版本，预期维护到下个快照版本发布时间（待定）后一个月。 | 模型支持8k tokens上下文，为了保证正常的使用和输出，API限定用户输入为6k tokens。 |
  | qwen-max-longcontext | 通义千问千亿级别超大规模语言模型，支持中文、英文等不同语言输入。 | 模型支持30k tokens上下文，为了保证正常的使用和输出，API限定用户输入为28k tokens。 |
  | qwen1.5-72b-chat | 通义千问1.5对外开源的72B规模参数量的经过人类指令对齐的chat模型。 | 支持32k tokens上下文，输入最大30k，输出最大2k tokens。 |
  | qwen1.5-14b-chat |  | 模型支持 8k tokens上下文，为了保障正常使用和正常输出，API限定用户输入为6k Tokens。 |
  | qwen1.5-7b-chat |  |  |
  | baichuan13b-chat-v1 | 由百川智能开发的一个开源的大规模预训练模型。 |  |
  | baichuan2-7b-chat-v1 | |  |
  | chatglm3-6b | ChatGLM3-6B-Base 具有在 10B 以下的预训练模型中最强的性能。 |  |

## 文本向量可用的模型名称

- text-embedding-v1
- text-embedding-v2