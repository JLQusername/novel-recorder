from sqlmodel import SQLModel, Field, Session, create_engine, select

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


def add_novel(novel: Novel) -> None:
    with Session(engine) as session:
        session.add(novel)
        session.commit()


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
        old_novel.author = novel.author
        old_novel.name = novel.name
        old_novel.nationality = novel.nationality
        old_novel.read_time = novel.read_time
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
    delete_novel(3)
