## Setup Environment

python3 -m venv ./venv
source venv/bin/activate
pip3 install -r requirements.txt

## Start

export FLASK_APP=slamy_view.py

flask run --host=0.0.0.0

python slamy_pub.py