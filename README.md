# api_drones
API Drones  For our use case the load is medications.

## Installaltion and run:

(Python 3.10.5)

 pip install -r requirements.txt

python manage.py runserver --noreload

Note: scheduler for check log battery start with application

## Run Tests:
python manage.py test

## Admin UI Area

http://localhost:8000/admin/

user: admin

password: admin123

Check schedule logs in Table Log batterys of admin UI

## API REST Endpoints:
- http://localhost:8000/drones/drone -> List, Register
- http://localhost:8000/drones/drone/<serial_number>/ -> Detail, Update, Delete
- http://localhost:8000/drones/check-battery-level/<serial_number>/ -> check drone battery level for a given drone
- http://localhost:8000/drones/availables/ -> checking available drones for loading;
- http://localhost:8000/drones/loading-drone/<serial_number>/ -> loading a drone with medication items;
- http://localhost:8000/drones/check-loaded-medications/<serial_number>/ -> checking loaded medication items for a given drone;

- http://localhost:8000/drones/medication -> List, Register
- http://localhost:8000/drones/medication/<medication code>/ -> Detail, Update, Delete

