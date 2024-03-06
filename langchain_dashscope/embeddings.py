# common types
from typing import Type, Any, Mapping, Dict, Iterator, List, Optional, cast

from langchain_core.embeddings import Embeddings
from langchain_core.pydantic_v1 import (
    BaseModel,
    Field,
    root_validator,
)
from langchain_core.utils import (
    convert_to_secret_str,
    get_from_dict_or_env,
    get_pydantic_field_names,
)

# async
import asyncio
from typing import AsyncIterator

from http import HTTPStatus

class DashScopeEmbeddings(BaseModel, Embeddings):
    """支持最新的阿里云模型服务灵积API的文本向量模型"""

    client: Any = None
    """访问DashScope的客户端"""

    api_key: str = None

    model: str = Field(default="text-embedding-v2")
    """所要调用的模型编码"""

    @root_validator()
    def validate_environment(cls, values: Dict) -> Dict:
        try:
            from dashscope import TextEmbedding
            values["client"] =  TextEmbedding
        except ImportError:
            raise RuntimeError(
                "Could not import dashscope package. "
                "Please install it via 'pip install -U dashscope'"
            )
        return values

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Embed search docs."""
        response = self.client.call(
            model=self.model,
            input=texts,
            text_type="document"
        )       
        if response.status_code != HTTPStatus.OK:
            raise Exception('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
                response.request_id, response.status_code,
                response.code, response.message
            ))

        chunks = []
        for chunk in response.output['embeddings']:
            chunks.append(chunk['embedding'])

        return chunks

    def embed_query(self, text: str) -> List[float]:
        """Embed query text."""
        response = self.client.call(
            model=self.model,
            input=text,
            text_type="query"
        )
        if response.status_code != HTTPStatus.OK:
            raise Exception('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
                response.request_id, response.status_code,
                response.code, response.message
            ))

        return response.output['embeddings'][0]['embedding']
