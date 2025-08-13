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


def update_novel(id: int, _novel: Novel) -> None:
    with Session(engine) as session:
        statement = select(Novel).where(Novel.id == id)
        res = session.exec(statement)
        novel = res.first()
        if not novel:
            return
        if _novel.id:
            novel.id = _novel.id
        novel.author = _novel.author
        novel.name = _novel.name
        novel.nationality = _novel.nationality
        novel.read_time = _novel.read_time
        novel.status = _novel.status
        session.add(novel)
        session.commit()


if __name__ == "__main__":
    create_db_and_tables()
    delete_novel(1)
    update_novel(
        3,
        Novel(
            id=3,
            name="name",
            author="author",
            nationality="nationality",
            read_time=2,
            status=NovelStatus.FINISHED,
        ),
    )
    novels = get_all_novels()
    print(novels)
