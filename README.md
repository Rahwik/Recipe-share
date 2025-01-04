# Recipe Share

Recipe Share is a Django-based web application designed to make sharing and managing recipes effortless. With a user-friendly interface and secure authentication, users can add, edit, delete, and explore a variety of recipes shared by others.

---

## Features

### User Authentication
- **Secure Login & Logout**: Ensure user data safety with robust authentication.
- **User Registration**: Simple and quick account creation process.

### Recipe Management
- **Add Recipes**: Easily upload recipes, including images and detailed descriptions.
- **Browse Recipes**: Explore shared recipes with a seamless browsing experience.
- **Search Recipes**: Quickly find recipes by their names using the search feature.
- **Edit Recipes**: Update existing recipes to keep them current.
- **Delete Recipes**: Remove outdated or unwanted recipes.

---

## Requirements

- **Python**: Version 3.7 or higher
- **Django**: Version 4.0 or higher
- **Database**: SQLite (default) or any Django-supported database

---

## Installation

### Step 1: Clone the Repository
```bash
$ git clone https://github.com/yourusername/recipe-share.git
$ cd recipe-share
```

### Step 2: Set Up a Virtual Environment
```bash
$ python -m venv venv
$ source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
$ pip install -r requirements.txt
```

### Step 4: Apply Database Migrations
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

### Step 5: Start the Development Server
```bash
$ python manage.py runserver
```

Access the application at `http://127.0.0.1:8000/` in your browser.

---

## Usage

### 1. Register an Account
- Navigate to `/register/` to create a new user account.

### 2. Login to Your Account
- Use your credentials at `/login/` to log in securely.

### 3. Manage Recipes
- Go to `/recipes/` to add new recipes with images and descriptions.
- Visit `/shared/` to view and search for recipes shared by other users.
- Update or delete your recipes as needed.

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

We welcome contributions to improve Recipe Share! To contribute:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add new feature'`.
4. Push your branch: `git push origin feature-name`.
5. Open a Pull Request for review.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

