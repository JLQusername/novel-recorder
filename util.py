from model import *

novel_nationalities = ["欧美", "日本", "中国"]
read_status = ["未购买", "未读", "正在读", "已读"]
read_times = [
    "大一下",
    "暑假",
    "大二上",
    "寒假",
    "大二下",
    "暑假",
    "大三上",
    "寒假",
    "大三下",
    "暑假",
    "大四上",
    "寒假",
    "大四下",
]


def get_real_read_time(read_time: int):
    if read_time < 0 or read_time >= len(read_times):
        return "异常值"
    return read_times[read_time]


def get_real_status(status: NovelStatus) -> str:
    if status.value < 0 or status.value >= len(read_status):
        return "异常值"
    return read_status[status.value]


def get_real_nationality(nationality: NovelNationality) -> str:

    if nationality.value < 0 or nationality.value >= len(novel_nationalities):
        return "异常值"
    return novel_nationalities[nationality.value]


def get_chinese_char_num(text: str) -> int:
    return sum(1 for ch in text if "\u4e00" <= ch <= "\u9fff")
