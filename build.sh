#!/bin/bash
#!/bin/bash
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install Django>=4.2 djangorestframework==3.15.2 djongo==1.3.6
