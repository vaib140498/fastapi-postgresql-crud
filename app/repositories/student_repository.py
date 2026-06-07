from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.student import Student


class StudentRepository:

    async def create_student(self, db: AsyncSession, student: Student):
        db.add(student)
        await db.commit()
        await db.refresh(student)
        return student

    async def get_student(self, db: AsyncSession, student_id: int):
        result = await db.execute(select(Student).where(Student.id == student_id))
        return result.scalar_one_or_none()

    async def get_all_students(self, db: AsyncSession):
        result = await db.execute(select(Student))
        return result.scalars().all()

    async def delete_student(self, db: AsyncSession, student_id: int):
        student = await self.get_student(db, student_id)
        if not student:
            return None
        await db.delete(student)
        await db.commit()
        return student

    async def update_student(
        self,
        db: AsyncSession,
        student_id: int,
        branch: str,
        marks: int | None,
    ):
        student = await self.get_student(db, student_id)
        if not student:
            return None
        student.branch = branch
        student.marks = marks
        await db.commit()
        await db.refresh(student)
        return student
