# -*- coding: utf-8 -*-
# @Time    : 2023/12/10 下午10:33
# @Author  : sudoskys
# @File    : event.py
# @Software: PyCharm
from io import TextIOBase
from typing import Union, IO, Optional

from loguru import logger
from pydantic import BaseModel

from app.utils import WdTaggerSDK
from setting.wdtagger import TaggerSetting

# ANIME = AnimeIDF()


class TaggerResult(BaseModel):
    anime_tags: Optional[str] = ""
    characters: Optional[list] = []


async def pipeline_tag(trace_id, content: Union[IO, TextIOBase]) -> TaggerResult:
    content.seek(0)
    content.seek(0)
    raw_output_wd = await WdTaggerSDK(base_url=TaggerSetting.wd_api_endpoint).upload(
        file=content.read(),
        )
    content.close()
    tag_result: str = ", ".join(i for i in raw_output_wd[0]['tags'].keys() if 'rating:' not in i)
    tag_result = tag_result.replace("_", " ")
    print(tag_result)
    logger.info(f"Censored {trace_id},result {tag_result}")
    return TaggerResult(
        anime_tags=tag_result,
        characters=[]
    )
