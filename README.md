# Bookwarm

Bookwarm is a full-stack bookstore platform designed to provide personalized book recommendations using collaborative filtering techniques. It includes a user-friendly interface for browsing, searching, and exploring a wide variety of books. The backend API is built using Python and Flask, offering efficient and scalable features for a seamless user experience.

## Features

- **Personalized Recommendations:** Collaborative filtering algorithm suggests books based on user preferences and behavior.
- **Search Functionality:** Easily find books by title, author, or genre.
- **User Authentication:** Secure login and registration system.
- **Interactive UI:** A clean and responsive interface built with HTML, CSS, and JavaScript.
- **Real-Time Updates:** Dynamic features for a better user experience.

## Technologies Used

### Backend
- **Python**: Core programming language for the backend.
- **Flask**: Framework used to build the backend API.
- **Collaborative Filtering**: Implemented using Python libraries for personalized recommendations.

### Frontend
- **HTML, CSS, JavaScript**: For designing a responsive and interactive user interface.

### Database
- **SQLite**: Lightweight database for storing user and book data.

### Deployment
- Vite is used for frontend development, and the backend is deployable to platforms like Heroku or Render.

## Installation

Follow these steps to run the Bookwarm project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/kyrahul2107/Bookwarm.git
   cd Bookwarm
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   flask run
   ```

5. **Access the application:**
   Open your browser and navigate to `http://127.0.0.1:5000`.

## Usage

1. **Sign up/Login:** Create an account or log in to explore personalized recommendations.
2. **Browse Books:** Use the search feature or browse through categories to find books.
3. **Get Recommendations:** Receive book suggestions tailored to your preferences.

## Project Structure

```
Bookwarm/
├── static/
│   ├── css/
│   └── js/
├── templates/
├── app.py
├── models.py
├── utils/
├── requirements.txt
└── README.md
```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch-name`).
3. Commit your changes (`git commit -m 'Add a new feature'`).
4. Push to the branch (`git push origin feature-branch-name`).
5. Open a Pull Request.

## Deployment

The project can be deployed to platforms like Heroku, Render, or any Python-compatible hosting service. Refer to the platform documentation for detailed deployment steps.

## Author

**Rahul Kumar Yadav**

LinkedIn: [Rahul Kumar Yadav](https://www.linkedin.com/in/rahulkumaryadav/)
GitHub: [kyrahul2107](https://github.com/kyrahul2107)
Go Live:https://bookwarm-2ya2.onrender.com/

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

