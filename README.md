# League Champion Directory 🛡️

A Flask web application that lets users search, view, and leave reviews on League of Legends champions. Built with raw CSS for styling and connected to a MongoDB backend for storing champion reviews.

## 🌐 Features

- 🔍 Search for champions by name
- 📖 View champion details (image, title, tags, stats, and lore)
- 📝 Submit and display notes or reviews per champion
- 🎨 Clean responsive layout with pure CSS (no Tailwind or Bootstrap)

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS (no framework)
- **Database**: MongoDB (via PyMongo)

---

## 📂 Project Structure

league-champ-directory/
├── data/
│ └── champions.json # Local JSON data for champion info
├── flask_app/
│ ├── static/
│ │ └── source.css # Raw CSS for the entire app
│ ├── templates/
│ │ ├── base.html # Base layout
│ │ ├── header.html # Navigation bar
│ │ ├── index.html # Search page
│ │ ├── query_results.html # Search results page
│ │ └── champion_detail.html # Individual champion profile
│ ├── init.py # App factory
│ ├── app.py # Flask routes
│ ├── model.py # MongoDB interactions
│ └── forms.py # Flask-WTF forms
├── .flaskenv # Flask environment variables
├── requirements.txt # Required Python packages
└── README.md
