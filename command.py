import typer
from typing_extensions import Annotated

from database import *
from model import *
from util import *

app = typer.Typer()


@app.command()
def show_all() -> None:
    novels = get_all_novels()
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+ ID |书名                |作者              |国籍|状态  |阅读时间 +")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    for novel in novels:
        _print_novel(novel)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


@app.command()
def add(
    author: Annotated[str, typer.Option("--author", "-a", prompt=True)],
    name: Annotated[str, typer.Option("--name", "-n", prompt=True)],
    nationality: Annotated[
        NovelNationality, typer.Option("--nationality", "-nt", prompt=True)
    ],
    read_time: Annotated[int, typer.Option("--read-time", "-rt")] = 0,
    status: Annotated[NovelStatus, typer.Option("--status", "-s")] = NovelStatus.NO_BUY,
):
    novel = Novel(
        author=author,
        name=name,
        nationality=nationality,
        read_time=read_time,
        status=status,
    )
    add_novel(novel)
    print("Added novel:" + str(novel))


@app.command()
def update(
    nationality: Annotated[
        NovelNationality, typer.Option("--nationality", "-nt")
    ] = None,
    author: Annotated[str, typer.Option("--author", "-a")] = None,
    name: Annotated[str, typer.Option("--name", "-n")] = None,
    read_time: Annotated[int, typer.Option("--read-time", "-rt")] = None,
    status: Annotated[NovelStatus, typer.Option("--status", "-s")] = None,
    id: Annotated[int, typer.Option("--id", "-i")] = None,
) -> None:
    novel = Novel(
        id=id,
        author=author,
        name=name,
        nationality=nationality,
        read_time=read_time,
        status=status,
    )
    update_novel(id, novel)


@app.command()
def delete(id: int) -> None:
    delete_novel(id)
    typer.echo(f"Deleting {id}")


def _print_novel(novel: Novel) -> None:
    id = novel.id
    name = novel.name
    author = novel.author
    national = get_real_nationality(novel.nationality)
    status = get_real_status(novel.status)
    read_time = get_real_read_time(novel.read_time)
    name_len = 20 - get_chinese_char_num(name)
    author_len = 18 - get_chinese_char_num(author)
    status_len = 6 - get_chinese_char_num(status)
    read_time_len = 9 - get_chinese_char_num(read_time)
    print(
        f"+{id:3} |{name:{name_len}}|{author:{author_len}}|{national:2}|{status:{status_len}}|{read_time:{read_time_len}}+"
    )


if __name__ == "__main__":
    app()
