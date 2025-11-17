# ML Zoomcamp midterm project - Getting good grades in college

## Problem description

Every year millions of students go through school and live a stressful like aiming to get good grades. Some of them want the best grades possible, some of them just want a passing score. This work aims to study the habits of students and how these influence on their exam scores. We include a wide variety of habits to understand how these affect the final exam score.

The objective of this project is to understand how these habits affect the score to help students focus on what is important to get a good score.

The model will also be used to evaluate a students habits and try to predict how he will do in school.

## Exploratory data analysis and model selection
Seen on file ```notebook.ipynb```

# Running the project

## Clone the repo to your local enviroment.
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