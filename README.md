Dependencies:
+ python
+ flask
+ sqlite3

To run this app:
+ chmod +x run.sh
+ python initialize_uads.py
+ ./run.sh

Only run the initialize_uads.py once, it is solely for generating sample data.
In production the site would have a log in system with permissions and user
accounts, but for this we left all the user pages open. The admin can interact
with the databases by sending SQL commands and the backend will run them.


