from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.student import Student


class StudentRepository:

    async def create_student(self, db: AsyncSession, student_data: dict):
        
        student = Student(**student_data)
        
        db.add(student)
        await db.commit()
        await db.refresh(student)
        
        return student

    async def get_student(self, db: AsyncSession, student_id: int):
        result = await db.execute(select(Student).where(Student.id == student_id))
        
        return result.scalar_one_or_none()

    async def get_all_students(self, db: AsyncSession):
        result = await db.execute(select(Student).order_by(Student.id))
        
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
        update_data: dict
    ):
        student = await self.get_student(db, student_id)
        if not student:
            return None
        for key,value in update_data.items():
            if hasattr(student,key):
                setattr(student, key, value)

        await db.commit()
        await db.refresh(student)
        
        return student

    async def create_students(self, db: AsyncSession, std_data: list[dict]):

        students = [
            Student(**student) for student in std_data
        ]
        db.add_all(students)
        await db.commit()
        for std in students:
            await db.refresh(std)
        return students