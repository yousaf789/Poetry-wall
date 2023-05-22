# Poetry Wall
A simple and elegant poetry wall application designed to make your poetry reach the stars (quite litrally). This application uses Flask for routing and HTML/CSS and Javascript for structure, providing an easy-to-use interface for storing your poetry.

## Features
- User-based login system for personalized Poetry walls.
- Secure access to individual walls with saved progress and customizations (In-progress).
- Star display on black background for a night sky effect when submitting poetry for aesthetic purposes.
- Simple and elegant design for easy use and navigation.
- Sharing of poetry with other users (In-progress).

## Installation
1. Clone the repository

```bash
git clone https://github.com/yousaf789/poetry-wall.git
```
2. Create and activate a virtual environment

```bash
cd poetry-wall
python -m venv venv
venv\Scripts\activate # For MacOS, use: source venv/bin/activate
```
3. Insall the require packages

```bash
pip install -r requirements.txt
```

4. Initialize the database

```bash
flask init-db
```

## Usage
1. Run the Flask application
```bash
flask run
```
2. Open a web browser and visit 'https://127.0.0.1:5000' to access the Poetry wall.
3. Register a new account or login to an existing one to start filing your poetry wall.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[](https://choosealicense.com/licenses/mit/)