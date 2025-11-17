# ML Zoomcamp midterm project - Getting good grades in college

## Problem description

Every year millions of students go through school and live a stressful like aiming to get good grades. Some of them want the best grades possible, some of them just want a passing score. This work aims to study the habits of students and how these influence on their exam scores. We include a wide variety of habits to understand how these affect the final exam score.

The objective of this project is to understand how these habits affect the score to help students focus on what is important to get a good score.

The model will also be used to evaluate a students habits and try to predict how he will do in school.

| Column Name                | Data Type | Description                                                     |
| -------------------------- | --------- | --------------------------------------------------------------- |
| Hours_Studied              | int64     | Number of hours the student studies per week.            |
| Attendance                 | int64     | Attendance rate.                     |
| Parental_Involvement       | object    | Level of parental engagement in the student’s education.        |
| Access_to_Resources        | object    | Availability of educational resources (books, internet, etc.).  |
| Extracurricular_Activities | object    | Whether the student participates in extracurricular activities. |
| Sleep_Hours                | int64     | Average number of hours the student sleeps per night.           |
| Previous_Scores            | int64     | Scores from previous exams.                      |
| Motivation_Level           | object    | Self-reported motivation level of the student.                  |
| Internet_Access            | object    | Indicates if the student has internet access at home.           |
| Tutoring_Sessions          | int64     | Number of tutoring sessions attended.                           |
| Family_Income              | object    | Household income bracket or category.                           |
| Teacher_Quality            | object    | Perceived or rated quality of the teacher.                      |
| School_Type                | object    | Type of school (public, private).                         |
| Peer_Influence             | object    | Influence of peers on the student (positive/negative).          |
| Physical_Activity          | int64     | Amount of physical exercise (hours per week).                       |
| Learning_Disabilities      | object    | Whether the student has learning disabilities.                  |
| Parental_Education_Level   | object    | Highest education level reached by parents.                     |
| Distance_from_Home         | object    | Distance the student travels from home to school.               |
| Gender                     | object    | Student's gender.                                               |
| Exam_Score                 | int64     | Target variable: student’s exam performance score.              |


## Exploratory data analysis and model selection and training:
Seen on file ```notebook.ipynb```

# Running the project

## Files on this project:

| File Name                            | Description                                                                                                      |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| `data/StudentPerformanceFactors.csv` | Dataset containing student performance and related factors used for training and experimentation.                |
| `.python-version`                    | Specifies the Python version to use (useful for pyenv and environment consistency).                              |
| `Dockerfile`                         | Instructions to build a Docker image that runs the FastAPI service (including dependencies and startup command). |
| `model_1.bin`                        | Serialized machine learning model (saved after training to be used for inference).                               |
| `notebook.ipynb`                     | Jupyter notebook used for EDA, feature analysis, model selection, and hyperparameter tuning.                     |
| `predict_test.py`                    | Script that sends a test request to the deployed API to verify predictions are returned correctly.               |
| `predict.py`                         | FastAPI app that loads the model and exposes a `/predict` endpoint for inference.                                |
| `pyproject.toml`                     | Project configuration file that declares dependencies and metadata (modern replacement for `requirements.txt`).  |
| `README.md`                          | Documentation explaining how the project works, how to run it, and key context.                                  |
| `train.py`                           | Script used to preprocess data, train the model, evaluate it, and save it to `model_1.bin`.                      |
| `uv.lock`                            | Lock file created by `uv` to ensure deterministic dependency installation (version-locked environment).          |


## Clone the repo to your local enviroment. (recommended: use codespaces, instructon at the end)
 (WSL ubuntu on your windows ps, your ubuntu pc or your github space) <p>
Access the folder where you want to clone the repo
 >
    cd "path/to/your/desired/folder"
clone the github repo with the project
 >
    git clone <REPO_URL>
access the folder
 >
    cd "Module 7 mid term project"
If you dont have git you can go into github and download the folder manually and unzip it in your desired location.

## Install uv and dependencies
install uv (python package and project manager)
>
    pip install uv
Install dependencies for the project using uv. This reads the pyproject.toml and uv.lock to understand what packages this project needs and installs them to your enviroment.<p>
Uv will also create a virtual enviroment in the project directory where all the dependencies (pandas, numpy, scikit-learn, etc) are installed.
>
    uv sync
## Running the webservice/API
Run the API in the ubuntu terminal. This will create a running service linked to your port 9696. ```This uses the same port as the docker container. Be sure to close this service before running the docker enviroment```
>
    uv run uvicorn predict:app --reload --port 9696
You can now run ```predict test.py``` and it will use a request.post to send data from a studen (example_student dictionary) and predict its score. <p>
Feel free to change the examples features, always respect the format.

## Initializing docker enviroment (optional)
You can also create a docker container to run the project.<p>
start up the enviroment:<p>
In your ubuntu terminal (WSL2) run the following code to create the image for this project.
>
    docker build -t midtermproject:ver1 .

Now run the docker container with the project. This will be bound to your local host port 9696   
>
    docker run --rm -p 9696:9696 midtermproject:ver1

You can now run ```predict test.py``` and it will use a request.post to send data from a studen (example_student dictionary) and predict its score. <p>
Feel free to change the examples features, always respect the format.

## Running the project in codespaces (recommended)

Clone the repo into the new blank codespace
>
    https://github.com/NicoPHR/ML-Zoomcamp-mid-term-project.git

Move into the project directory
>
    cd ML-Zoomcamp-mid-term-project

install all packages/dependancies
>
    pip install .
Build the docker enviroment
>
    docker build -t midtermproject:ver1 .
Run the docker envoroment in codespaces:
>
    docker run --rm -p 9696:9696 midtermproject:ver1
Open a new terminal in codespaces and run the test script:
>
    python ML-Zoomcamp-mid-term-project/predict_test.py

