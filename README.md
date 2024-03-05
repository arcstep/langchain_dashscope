# langchain_dashscope
提供阿里云灵积模型的langchain集成。

阿里云平台的灵积模型不仅支持通义千问公有云服务，还支持很多开源模型在平台内的部署：

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
  | qwen-72b-chat | 通义千问对外开源的72B规模参数量的经过人类指令对齐的chat模型。 | 支持32k tokens上下文，输入最大30k，输出最大2k tokens。 |
  | qwen-14b-chat |  | 模型支持 8k tokens上下文，为了保障正常使用和正常输出，API限定用户输入为6k Tokens。 |
  | qwen-7b-chat |  |  |
  | qwen-1.8b-longcontext-chat | | 支持32k tokens上下文，输入最大30k，输出最大2k tokens。 |
  | qwen-1.8b-chat | | 模型支持 8k tokens上下文，为了保障正常使用和正常输出，API限定用户输入为6k Tokens。 |
  | llama2-7b-chat-v2 | LLaMa2系列大语言模型由Meta开发并公开发布，针对对话场景微调优化后的版本。| |
  | llama2-13b-chat-v2| | |
  | bailian-v1 |  |  |
  | baichuan13b-chat-v1 | 由百川智能开发的一个开源的大规模预训练模型。 |  |
  | baichuan2-7b-chat-v1 | |  |
  | belle-llama-13b-2m-v1 | BELLE-LLaMA模型是由BELLE出品的大规模语言模型，基于BLOOM和LLAMA针对中文优化、模型调优且仅使用由ChatGPT生成的数据，为中文指令提供更好的支持。 | |
  | dolly-12b-v2 | Dolly模型是由Databricks出品的大规模语言模型。该模型是在pythia-12b的基础上，使用databricks-dolly-15k数据集微调得到的。数据集包括头脑风暴、分类、生成、问答、信息抽取等任务的语料。|  |
  | chatglm3-6b | ChatGLM3-6B-Base 具有在 10B 以下的预训练模型中最强的性能。 |  |
  | sanle-v1 | 智海三乐教育大模型，取名于孟子所言“天下英才而教育之，三乐也”喻意，由浙江大学联合高等教育出版社、阿里云和华院计算等单位共同研制。该模型以阿里云通义千问70亿参数通用模型为基座，通过继续预训练和微调等技术手段，利用核心教材、领域论文和学位论文等教科书级高质量语料和专业指令数据集打造的一款专注于人工智能专业领域教育的大模型。 |  |
  | ziya-llama-13b-v1 | Ziya-LLaMA通用大模型是由IDEA研究院出品的大规模语言模型。Ziya-LLaMA大模型V1是基于LLaMa的130亿参数的大规模预训练模型，具备翻译，编程，文本分类，信息抽取，摘要，文案生成，常识问答和数学计算等能力。 |  |

