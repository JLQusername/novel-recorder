from sqlmodel import SQLModel, Session, create_engine, select

from model import Novel, NovelStatus


sqlite_url = "sqlite:///novel.db"
engine = create_engine(sqlite_url, echo=False)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_all_novels() -> list[Novel]:
    with Session(engine) as session:
        statement = select(Novel)
        res = session.exec(statement)
        return res.all()


def get_novel_by_id(id: int) -> Novel | None:
    with Session(engine) as session:
        statement = select(Novel).where(Novel.id == id)
        res = session.exec(statement)
        return res.first()


def add_novel(novel: Novel) -> None:
    with Session(engine) as session:
        session.add(novel)
        session.commit()
        session.refresh(novel)


def delete_novel(id: int) -> None:
    with Session(engine) as session:
        statement = select(Novel).where(Novel.id == id)
        res = session.exec(statement)
        novel = res.first()
        if novel:
            session.delete(novel)
            session.commit()


def update_novel(id: int, novel: Novel) -> None:
    with Session(engine) as session:
        statement = select(Novel).where(Novel.id == id)
        res = session.exec(statement)
        old_novel = res.first()
        if not old_novel:
            return
        if novel.id:
            old_novel.id = novel.id
        if novel.author:
            old_novel.author = novel.author
        if novel.name:
            old_novel.name = novel.name
        if novel.nationality:
            old_novel.nationality = novel.nationality
        if novel.read_time:
            old_novel.read_time = novel.read_time
        if novel.status:
            old_novel.status = novel.status
        session.add(old_novel)
        session.commit()


def get_newest_read_time() -> int:
    with Session(engine) as session:
        statement = select(Novel).where(Novel.status == NovelStatus.FINISHED)
        res = session.exec(statement)
        novels = res.all()
        return max([novel.read_time for novel in novels]) if novels else -1


if __name__ == "__main__":
    create_db_and_tables()
    # add_novel(Novel(author="author", name="name", nationality=0, status=0, read_time=0))
    delete_novel(1)
