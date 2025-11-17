import requests


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


r = requests.post(url="http://localhost:9696/predict", json=example_student)

r.status_code

print(r.json())
