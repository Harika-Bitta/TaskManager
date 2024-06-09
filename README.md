# Task Management System

The Task Management System is a web application developed to facilitate task management within an organizational setting. It allows users from various departments such as HR, Sales, Marketing, and Training to efficiently add, view, and manage tasks.

## Features

- **Technology Stack**: The system is developed using Django, HTML, CSS, and JavaScript, ensuring a robust and user-friendly interface for task management.
- **Task Management**: Users can easily add new tasks, including titles, descriptions, Assigned Date, Status, and any relevant details.
- **Task Deletion and Updating**: Implemented task deletion and updating functionality, enabling users to remove unnecessary or completed tasks from the system to maintain clarity and focus, ensuring streamlined task management workflows.
- **Department-Specific Views**: Users from HR, Sales, Marketing, and Training departments can view all tasks assigned to them, including detailed descriptions and current status (e.g., running, completed) within their respective departments.
- **Data Storage**: Utilized MySQL database for data storage, ensuring reliable and secure management of task-related information, maintaining data integrity across departments.
- **Department-Specific Dashboard**: The system features a department-specific dashboard where users can access task details, monitor progress.

## Getting Started

1. Clone the repository.
2. Install dependencies: `pip install django`
3. Configure MySQL database settings.
4. Run migrations: `python manage.py migrate`
5. Start the development server: `python manage.py runserver`

## Usage

1. Log in with your credentials.
2. Add, view, update, or delete tasks.
3. Use the department-specific dashboard to monitor task progress.


