from pydantic import BaseModel
from typing import Any, Dict, AnyStr, List, Union, Optional

JSONObject = Dict[AnyStr, Any]
JSONArray = List[Any]
JSONStructure = Union[JSONArray, JSONObject]


class InputText(BaseModel):
    sentence_text: str
    language: Optional[str]
