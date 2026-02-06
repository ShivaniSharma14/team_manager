# Team Resource Manager

A Django backend application for managing posts/resources with authentication and role-based authorization using Django's built-in permissions and groups. This project focuses on **backend logic, access control, and clean architecture**, rather than frontend design.

---

## 🚀 Features

- User authentication (login/logout)
- Create, view, update, and delete posts/resources
- Ownership-based authorization
- Role-based access using Django Groups & Permissions
- Centralized permission checks for maintainability
- Django Admin integration for role management

---

## 🔐 Roles & Authorization Logic

This project uses **Django's built-in model permissions** along with **Groups** created via the Admin panel.

### 👤 Normal User

- Can view all posts
- Can create new posts
- Can update and delete **only their own posts**

### 👩‍💼 Manager (Group-based role)

- Assigned permissions via Django Admin
- Can create, update, and delete **any post**

### 👑 Superuser

- Full unrestricted access to all features

**Authorization checks combine:**
- **Ownership checks** (`created_by`)
- **Permission checks** (`user.has_perm(...)`)

Permission logic is centralized to keep views clean and reusable.

---

## 🛠 Tech Stack

- Python
- Django
- SQLite (development database)
- HTML Templates
- Django Admin

---

## 📂 Project Structure
```
team-resource-manager/
├── accounts/          # Authentication logic
├── resources/         # Resource CRUD & permission checks
├── team_manager/      # Project settings
├── manage.py
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/ShivaniSharma14/team_manager.git
cd team_manager
```

### 2️⃣ Create & activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On macOS/Linux
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run migrations
```bash
python manage.py migrate
```

### 5️⃣ Create superuser
```bash
python manage.py createsuperuser
```

### 6️⃣ Start development server
```bash
python manage.py runserver
```

Open: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🧑‍💼 Managing Roles & Permissions

1. **Groups** (e.g., Manager) are created via Django Admin
2. **Permissions** (add, change, delete) are assigned to groups
3. **Users** inherit permissions from their group
4. **Normal users** rely on ownership-based access

---

## 📌 Notes

- Database file (`db.sqlite3`) is excluded from version control
- No user data or posts are stored in the repository
- This project was built as part of learning Django backend development
- Emphasis is on security, permissions, and clean backend logic

---

## 👤 Author

**Shivani Sharma**
- GitHub: [@ShivaniSharma14](https://github.com/ShivaniSharma14)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request