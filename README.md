# IP Address Management REST API
 
Create a simple IP Address Management REST API using python Django, on top of any data store. It will include the ability to add IP Addresses by CIDR block and then either acquire or release IP addresses individually. Each IP address will have a status associated with it that is either “available” or “acquired”. 
 
The REST API must support four endpoint:
  * **Create IP addresses** - take in a CIDR block (e.g. 10.0.0.1/24) and add all IP addresses within that block to the data store with status “available”
  * **List IP addresses** - return all IP addresses in the system with their current status
  * **Acquire an IP** - set the status of a certain IP to “acquired”
  * **Release an IP** - set the status of a certain IP to “available”




## Setup environment -

#### Clone or Download the repository
```bash
git clone https://github.com/shravanskp/ip-rest-api-PARIKH.git
cd ip-rest-api-PARIKH
```

#### Create virtual environment and activate
```bash
python -m venv env

source env/bin/activate 
```

#### Install Dependencies

```bash
pip install -r requirements.txt
```

#### Database Migrations

```bash
python manage.py makemigraations

python manage.py migrate
```

#### Now launch the server
```bash
python manage.py runserver
```

#### To run tests
```bash
python manage.py test
```


### Available Routes - 
| Ent-Point  | Method  |
|---|---|
| http://localhost:8000/api/ips/  | POST |
| http://localhost:8000/api/ips/  | GET  |
| http://localhost:8000/api/ips/{id}/  | GET  |
| http://localhost:8000/api/ips/{id}/acquire/  | PUT  |
| http://localhost:8000/api/ips/{id}/release/  | PUT  |
