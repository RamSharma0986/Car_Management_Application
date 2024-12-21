# Car_Management_Application
🚗✨ Built a Car Management Application in Django to simplify car management! 🚀🛠️

**Video Link** <a href="https://drive.google.com/file/d/1_8_w-3Hdb1h81br3mLjcYW3k7NLiA_r4/view" target="_blank" > Click Here </a>

🚗✨ I created a Car Management System with Login/Register, a car list, and a Search option. If no cars are available, it shows "No car available". Registered users can add, edit, or delete cars, while unregistered users can only view descriptions. After login, Create New Car and Logout buttons appear. The form allows adding car details and up to 10 images. Editing and deleting options are available after login. 🚙💻

## Prerequisites

1. **Install Python**  
   Make sure Python is installed on your system. Download it from the [official Python website](https://www.python.org/downloads/).

   ```bash
   # Check if Python is installed
   python --version

2. **setup Django**

 ```bash
   #  Django is installed
   pip install django

   # Verify the installation
   django-admin --version
```

### 2️⃣ Set Up Your Virtual Environment (Optional)
To avoid dependency issues, it is recommended to create a virtual environment. Here's how:
1. Open the extracted folder in **VS Code**.
2. In the terminal, create the virtual environment:
   ```bash
   python -m venv env
   ```
3. Activate the virtual environment:
   ```bash
   .\env\Scripts\activate.ps1
   ```

### 3️⃣ Install Dependencies
Once inside the virtual environment, install Django:
```bash
pip install django
```

### 4️⃣ Navigate to the Project Directory
Change to the `car_management` directory where the `manage.py` file is located:
```bash
cd car_management
```

### 5️⃣ Migrate the Database
Apply database migrations using the following commands:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create a Superuser 
You can create a superuser to manage the database via Django's admin panel: 
```bash
python manage.py createsuperuser
```
- Follow the prompts to add a username and password of your choice. To access the admin panel you can visit to http://127.0.0.1:8000/admin/ url and see database.

![d1](https://github.com/user-attachments/assets/afd97d33-00ff-4164-a934-3cd066076fb9)

### Run the Superuser 
To run the server run the below command in terminal after run the command to access the website you can visit to http://127.0.0.1:8000/
```bash
python manage.py runserver
```

## 🚗✨ Car Management System

Welcome to the **Car Management System**! This project allows users to explore, manage, and interact with car information. Below is a detailed walkthrough of the system. 🌟

---

## 🏠 Homepage  
The first page shows:  
- **Login/Register** buttons 🔑  
- All available cars 🚘  
- A **Search** option 🔍  

![Homepage with cars](https://github.com/user-attachments/assets/f1fb1c27-4e75-4edf-ab69-89745a6ee2c9)  
If no cars are available, it shows **"No car available"** 😞.
![No cars available](https://github.com/user-attachments/assets/36c7c5d5-bc0c-4919-9ad0-da452abc53cb)

---

## 📋 Viewing Car Details  
Clicking on any car name displays its details. 🛠️ However, you can't modify the description unless you **register and log in**.  

![Car details](https://github.com/user-attachments/assets/c0d56fe7-4a70-4dc5-899a-d271f34d52d0)

---

## 🔑 Registration and Login  
To **add, edit, or delete cars**, users must **register** first.  
- **Login Page** 🖥️:  
  ![Login page](https://github.com/user-attachments/assets/e8bb8afc-f4b2-4d4f-90b8-cf1cd83fa22b)  
- **Register Page** 📝:  
  ![Register page](https://github.com/user-attachments/assets/b6660fdf-2cca-4ad4-80fe-241d0a32b6b9)

After successful registration, the **Login/Register** buttons transform into **Create New Car** 🆕 and **Logout** 🚪.  

![Post-login buttons](https://github.com/user-attachments/assets/a6072e53-8cf2-4de0-ad96-2f33857e3540)

---

## 🆕 Creating a New Car  
Click **Create New Car** to access a form for adding details:  
- **Title**  
- **Description**  
- **Car Type** 
- **Company** 
- **Tag**  
- **Dealer**  
- **Image Upload (max: 10 images)** 📸  
Exceeding 10 images shows an error ❗.

![Create car form](https://github.com/user-attachments/assets/7f613999-4564-4684-9209-13990a994613)

---

## ✏️ Editing and ❌ Deleting Cars  
After logging in, clicking any car on the homepage displays **Edit** and **Delete** buttons at the bottom.  
- **Edit Button** ✏️: Opens a form to modify car details.  
- **Delete Button** ❌: Removes the car.

![Edit/Delete buttons](https://github.com/user-attachments/assets/8ce7fb70-7c8b-42a0-8264-7cd2b23f990c)  
![Edit form](https://github.com/user-attachments/assets/345af7dd-422a-45e6-b2e8-8c9a42373711)

---

## 🎉 Features Summary  
- **Browse Cars** 🚘  
- **Search Functionality** 🔍  
- **User Authentication** 🔑  
- **Add/Edit/Delete Cars** 🆕✏️❌  
- **Image Upload Support** 📸 (max: 10 images)  

This way, I built the **Car Management System**! 🚗💻 If you face any issues, please refer to the 📹 **Video Link** provided at the beginning—it will help resolve your queries. 🙌 Thanks for visiting! 😊✨
