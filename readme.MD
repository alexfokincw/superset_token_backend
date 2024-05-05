# Backend Flask app for embedded Superset dashboards

This repository contains code that will return a guest token for the Superset embedded dashboards.

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository to your local machine:
```bash
1. git clone https://github.com/alexfokincw/superset_token_backend.git```
2. Navigate to the project directory:
   ```cd your-repo-name```
3. Create a copy of the `.env.example` file and name it `.env`
4. Open the `.env` file in a text editor and fill in the required fields with appropriate values:

```env
SUPERSET_BASE_URL=http://localhost:8088
SUPERSET_USER=myappuser
SUPERSET_FIRST_NAME=MyApp
SUPERSET_LAST_NAME=MyApp
SUPERSET_PASSWORD=12345
FRONTEND_BASE_URL=http://localhost:3000
```

**FRONTEND_BASE_URL** Frontend react application for example.

5. Save the .env file.


2. Run Flask server
```bash
python app.py
```

Application will be available here: 
http://localhost:8000/guest-token