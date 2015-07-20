#! env/bin/python
"""
Run file for development 
"""
from app import app
app.run(debug=True, host='0.0.0.0')
