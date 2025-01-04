# Recipe Share

Recipe Share is a Django-based web application that allows users to share, update, and delete their favorite recipes. With secure authentication, users can manage their recipes seamlessly and explore shared recipes from other users.

---

## Features

### User Authentication
- **Login & Logout**: Secure login and logout functionality.
- **Registration**: Easy account creation with username and password.

### Recipe Management
- **Create Recipes**: Users can upload recipes, including images and descriptions.
- **View Recipes**: Browse through a list of shared recipes.
- **Search Recipes**: Search for specific recipes by name.
- **Update Recipes**: Edit existing recipes.
- **Delete Recipes**: Remove recipes from the database.

---

## Requirements

- Python 3.7+
- Django 4.0+
- Database: SQLite (default), or other Django-supported databases.

---

## Installation

### Step 1: Clone the Repository
```bash
$ git clone https://github.com/yourusername/recipe-share.git
$ cd recipe-share
```

### Step 2: Create a Virtual Environment
```bash
$ python -m venv venv
$ source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
$ pip install -r requirements.txt
```

### Step 4: Apply Migrations
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

### Step 5: Run the Development Server
```bash
$ python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to use the application.

---

## Usage

### 1. Register a New Account
- Visit `/register/` to create an account.

### 2. Login to Your Account
- Use your credentials to log in at `/login/`.

### 3. Manage Recipes
- Navigate to `/recipes/` to add new recipes.
- Go to `/shared/` to view and search for recipes.
- Update or delete recipes as needed.

---

## File Structure

```
recipe-share/
├── manage.py
├── app/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── recipes.html
│   │   ├── shared.html
│   │   ├── update_recipe.html
│   └── static/
├── db.sqlite3
└── requirements.txt
```

---

## Contributing

We welcome contributions to improve Recipe Share! Please follow these steps:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact

For questions or suggestions, please contact:

**Rahul Prasad**  
Email: rahul.prasad@example.com

