## Baskeasy-backend-Repo


For `.env` - environment variable file, email ankit.sanghavi87@gmail.com
For running the project, we use Gunicorn. There are the steps
0. Install python, pip and python virtual env
```bash
sudo apt install python
sudo apt update
sudo apt upgrade
sudo apt install python3-pip python3-venv

```

1. Setup python virtual environment
`python3 -m venv benv`

1. Activate the virtual environment
`source benv/bin/activate`

1. Install the requirements
`pip install -r requirements.txt`

1. Install gunicorn
`sudo apt install gunicorn` 

2. Run the project in detached mode
`gunicorn -w 4 -b 0.0.0.0:5000 app:app -D`

3. To stop the project
`ps aux | grep gunicorn`

4. Kill the process
`kill -9 <process_id>`

5. To run the project in debug mode
`python app.py`

