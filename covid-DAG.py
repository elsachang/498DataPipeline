# import operators from airflow

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import datetime as dt
default_args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2020, 4, 1, 1, 00, 00),
    'retries': 1
}
#Define the DAG parameters.
dag = DAG('covid',
          default_args=default_args,
          schedule_interval='0 1 * * *',
          catchup=False
          )

# Setting up dependency
command_t1 = 'python PathToYourFile/covid_func.py '
t1 = BashOperator(
          task_id = 'covidPlots',
          bash_command = command_t1
          dag = dag
)

from git import Repo
import os

os.chdir(YourGithubPageDirectoryPath)

PATH_OF_GIT_REPO = YourGithubPageDirectoryPath/.git'
COMMIT_MESSAGE = 'Daily update'

#This required proper git configuration.
def git_push():

    repo = Repo(PATH_OF_GIT_REPO)
    repo.git.add('--all')
    repo.index.commit(COMMIT_MESSAGE)
    origin = repo.remote(name='origin')
    origin.push()

git_push() 

#Add the next task t2 to the DAG
command_t2 = 'python PathToYourFile/git_push.py '

t2 = BashOperator(
                  task_id = 'gitPush',
                  bash_command = command_t2,
                  dag = dag
)

t3 = BashOperator(
                 task_id = 'gitPush_repit',
                 bash_command = command_t2,
                 dag = dag)

#specifying the order of the task.
t1 >> t2 >> t3






#From the starting date to the current one, there could have been several executions according to the schedule_interval.