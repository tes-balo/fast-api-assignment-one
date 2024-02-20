from fastapi import FastAPI
from pydantic import BaseModel

class Student(BaseModel):
	Id: str
	Name: str
	Age: int
	Sex: str
	Height: float

class Students(BaseModel):
	students: list[Student]

students: {int, Students} = {}

app = FastAPI()

@app.post('/students/{Id}')
def create_student():
	Id = 5
	student:Student = {'Name':'john', 'Id': Id }
	return student

@app.get('/students')
def get_root():
	return {'msg':'home page works!'}
@app.get('/students/all')
def get_all_students():
	return students