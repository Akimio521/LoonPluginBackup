from typing import Generator
from re import findall
from dataclasses import dataclass

from httpx import Client


@dataclass
class Resource:
    prefix: str
    plugin_prefix: str
    script_prefix: str
    jq_prefix: str
    urls: list[str]


def get_kelee_plugin_urls() -> list[str]:
    """
    从可莉github中提取表格中的插件URL
    """
    URL = "https://raw.githubusercontent.com/luestr/ProxyResource/main/README.md"
    PATTERN = r'<a href="https://www.nsloon.com/openloon/import\?plugin=([^"]+\.lpx)">'

    with Client() as client:
        response = client.get(URL)
    return findall(PATTERN, response.text)


def get_sources() -> Generator[Resource]:
    yield Resource(
        prefix="kelee",
        plugin_prefix="https://kelee.one/Tool/Loon/",
        script_prefix="https://kelee.one/Resource/",
        jq_prefix="https://kelee.one/Resource/",
        urls=get_kelee_plugin_urls(),
    )


if __name__ == "__main__":
    # 提取插件URL
    urls = get_kelee_plugin_urls()
    print(f"找到 {len(urls)} 个插件URL:")
    for url in urls:
        print(url)
