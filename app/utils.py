# -*- coding: utf-8 -*-
# @Time    : 2023/11/18 上午12:51
# @Author  : sudoskys
# @File    : utils.py
# @Software: PyCharm

import aiohttp


def parse_command(command):
    if not command:
        return None, None
    parts = command.split(" ", 1)
    if len(parts) > 1:
        return parts[0], parts[1]
    elif len(parts) == 1:
        return parts[0], None
    else:
        return None, None


def generate_uuid():
    import shortuuid

    return str(shortuuid.uuid())


class WdTaggerSDK:
    def __init__(self, base_url):
        self.base_url = base_url

    async def upload(
        self, file, format="json", character_threshold=0.85
    ):
        url = f"{self.base_url}evaluate"
        data = {
            "format": format,
            "file": file,
        }
        # print(data)
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data) as response:
                print(await response.json())
                # response.raise_for_status()
                return await response.json()
