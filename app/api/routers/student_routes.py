from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.schemas.student_schema import StudentCreate, StudentResponse, StudentUpdate
from app.models.student import Student
from app.repositories.student_repository import StudentRepository

router = APIRouter(prefix="/students", tags=["Student"])
repo = StudentRepository()


@router.post("/", response_model=StudentResponse)
async def create_student(
    student_data: StudentCreate, db: AsyncSession = Depends(get_db)
):
    
    return await repo.create_student(db, student_data.model_dump())


@router.get("/", response_model=list[StudentResponse])
async def get_all_students(db: AsyncSession = Depends(get_db)):
    return await repo.get_all_students(db)


@router.get("/{student_id}", response_model=StudentResponse)  # FIX: was response_class (typo)
async def get_student(student_id: int, db: AsyncSession = Depends(get_db)):
    student = await repo.get_student(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@router.put("/{student_id}", response_model=StudentResponse)
async def update_student(
    student_id: int,
    student_data: StudentUpdate,
    db: AsyncSession = Depends(get_db),
):
    update_data = student_data.model_dump(exclude_unset=True, exclude_none=True)
    
    student = await repo.update_student(db, student_id, update_data)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@router.delete("/{student_id}")
async def delete_student(student_id: int, db: AsyncSession = Depends(get_db)):
    student = await repo.delete_student(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": f"Student {student_id} deleted."}


#To enter list of students in one go.
@router.post("/bulk", response_model= list[StudentResponse])
async def create_students(
    students_data: list[StudentCreate],
    db: AsyncSession = Depends(get_db)
):
    return await repo.create_students(
        db,
        [std.model_dump() for std in students_data]
    )