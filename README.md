# My Portfolio

Welcome to my portfolio project! This is a Django-based web application showcasing my skills, services, and projects. The project is open source and made with all the love in the world by ISSAKA HAMA Barhamou ❤️.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

### About page with an introduction yourself
![About Page](screenshots/home_page.png)

### Home page with an introduction, skills, services, and projects
![Home Page](screenshots/home1.png)
![Home Page](screenshots/home2.png)
![Home Page](screenshots/home3.png)

### Contact form with email functionality
![Contact Form](screenshots/contact_form.png)

### Unique visitor counter
![Visitor Counter](screenshots/visitor_counter.png)

### Responsive design using Bootstrap
![Responsive Design](screenshots/responsive_design.png)

### Animation effects for a dynamic user experience

### Footer with links to LinkedIn and GitHub
![Footer](screenshots/footer.png)

### Admin panel to manage content including skills, services, projects, and contact messages
![Admin Panel](screenshots/admin_panel.png)

### Blog section with posts and details
![Blog Section](screenshots/blog_section.png)

### Display of the 5 latest blog posts on the home page
![Latest Blog Posts](screenshots/latest_blog_posts.png)

### Pagination for projects on the home page
![Project Pagination](screenshots/project_pagination.png)

### Social media links with icons
![Social Media Links](screenshots/social_media_links.png)

### Filter Post by name
![Post Filter](screenshots/poste_filter.png)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/HamaBarhamou/myportfolio.git
    cd myportfolio
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv .env
    source .env/bin/activate  # On Windows use `.env\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the project root and add the following for production:

    ```env
    DEBUG=False
    POSTGRES_DB=your_db_name
    POSTGRES_USER=your_db_user
    POSTGRES_PASSWORD=your_db_password
    POSTGRES_HOST=your_db_host
    POSTGRES_PORT=your_db_port
    ```

    For development, using SQLite, you can keep the default settings in `settings.py`.

5. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## Usage

- **Home Page:** Displays an introduction, skills, services, projects, visitor counter, and the 5 latest blog posts.
- **Contact Page:** Allows users to send messages directly from the site.
- **Admin Panel:** Manage content including skills, services, projects, and contact messages.
- **Blog Section:** Create, update, and delete blog posts.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, feel free to reach out to me:

- **Email:** [your_email@gmail.com](mailto:your_email@gmail.com)
- **LinkedIn:** [ISSAKA HAMA Barhamou](https://www.linkedin.com/in/barhamou-issaka-hama-90047b179/)
- **GitHub:** [HamaBarhamou](https://github.com/HamaBarhamou)

Thank you for visiting my [portfolio!](https://0qx-driven-pascal.circumeo-apps.net/)
