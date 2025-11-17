import pickle
from fastapi import FastAPI
from pydantic import BaseModel

file_name = "model_1.bin"

example_student = {'Hours_Studied': 22,
 'Attendance': 69,
 'Parental_Involvement': 'Low',
 'Access_to_Resources': 'Medium',
 'Extracurricular_Activities': 0,
 'Sleep_Hours': 7,
 'Previous_Scores': 98,
 'Motivation_Level': 'Low',
 'Internet_Access': 1,
 'Tutoring_Sessions': 0,
 'Family_Income': 'Low',
 'Teacher_Quality': 'Medium',
 'Peer_Influence': 'Positive',
 'Physical_Activity': 2,
 'Learning_Disabilities': 0,
 'Parental_Education_Level': 'Postgraduate',
 'Distance_from_Home': 'Moderate',
 'School_Public': 1,
 'Gender_Male': 1}

class Input(BaseModel):
    Hours_Studied: int
    Attendance: int
    Parental_Involvement: str
    Access_to_Resources: str
    Extracurricular_Activities: int
    Sleep_Hours: int
    Previous_Scores: int
    Motivation_Level: str
    Internet_Access: int
    Tutoring_Sessions: int
    Family_Income: str
    Teacher_Quality: str
    Peer_Influence: str
    Physical_Activity: int
    Learning_Disabilities: int
    Parental_Education_Level: str
    Distance_from_Home: str
    School_Public: int
    Gender_Male: int


app = FastAPI()

@app.get("/")
def check():
    return {"hello world": "this API works!"}

@app.post("/predict")
def predict(data: Input):
    with open(file_name, 'rb') as f_in:
        dv, model = pickle.load(f_in)
        student = data.model_dump()

        X = dv.transform([student])
        y_pred = model.predict(X)

        response = {
            "Predicted Score": float(y_pred)
        }
        return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("predict:app", host="0.0.0.0", port=9696, reload=True)