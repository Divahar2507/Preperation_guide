# 🎓 PrepMaster - Java Full Stack Interview Preparation

A comprehensive, beautifully designed interview preparation application for Java Full Stack Developer freshers.

## ✨ Features

### 📚 Study Topics
- **Core Java**: OOPs, Collections, String Pool, hashCode/equals contract
- **Spring Boot**: Auto-configuration, Dependency Injection, Bean Lifecycle
- **Database (SQL)**: ACID properties, Indexing, DELETE vs TRUNCATE
- **React.js**: Hooks, Virtual DOM, Component Lifecycle
- **Data Structures & Algorithms**: Time Complexity, HashMap internals
- **HR & Behavioral**: STAR method, Common interview questions

### 🎯 Key Features
- **30+ Interview Questions** with deep, detailed explanations
- **Markdown Support** for rich formatting in answers (code blocks, tables, lists)
- **6-Week Study Plan** with structured roadmap
- **Interactive Mock Test** with scoring system
- **Curated Resources** with external learning links
- **Beautiful Dark UI** with glassmorphism design
- **Responsive Design** works on all screen sizes

## 🚀 Getting Started

### Prerequisites
- Node.js (v16 or higher)
- npm or yarn

### Installation

```bash
# Install dependencies
npm install

# Run development server
npm run dev

# Build for production
npm run build
```

### Access the Application
Open your browser and navigate to:
```
http://localhost:5173
```

## 📁 Project Structure

```
interview_preperation/
├── src/
│   ├── components/
│   │   ├── Icons.jsx          # Icon mappings
│   │   ├── Sidebar.jsx        # Navigation sidebar
│   │   ├── TopicCard.jsx      # Topic cards on home
│   │   └── QuestionCard.jsx   # Expandable Q&A cards
│   ├── pages/
│   │   ├── Home.jsx           # Dashboard with stats
│   │   ├── TopicQuestions.jsx # Questions by topic
│   │   ├── StudyPlan.jsx      # 6-week roadmap
│   │   ├── MockTest.jsx       # Practice test
│   │   └── Resources.jsx      # External links
│   ├── data/
│   │   └── interviewData.json # All questions & answers
│   ├── App.jsx                # Main app with routing
│   ├── index.css              # Tailwind styles
│   └── main.jsx               # Entry point
├── package.json
├── tailwind.config.js
└── vite.config.js
```

## 🎨 Tech Stack

- **Frontend**: React 19 + Vite
- **Routing**: React Router DOM v7
- **Styling**: Tailwind CSS v3 + Custom Glassmorphism
- **Icons**: Lucide React
- **Markdown**: react-markdown + remark-gfm

## 📝 Data Structure

All interview data is stored in `src/data/interviewData.json`:

```json
{
  "stats": { ... },
  "topics": [
    {
      "id": "java-core",
      "title": "Core Java",
      "icon": "Coffee",
      "questions": [
        {
          "id": 1,
          "question": "...",
          "answer": "...",
          "difficulty": "Easy",
          "tags": ["Basics"]
        }
      ]
    }
  ]
}
```

## 🎯 Features Breakdown

### Dashboard
- Stats overview (Total Questions, Completed, Topics, Streak)
- Topic cards with question counts
- Quick access to Mock Test

### Topic Questions
- Expandable question cards
- Copy answer functionality
- Difficulty badges
- Tag system
- Markdown formatting for rich content

### Study Plan
- 6-week structured roadmap
- Progress tracking
- Recommended time allocation

### Mock Test
- 10 random questions
- Self-evaluation (I got it right/wrong)
- Score calculation
- Retake functionality

### Resources
- Curated external links
- Categorized by topic
- Official documentation
- Practice platforms

## 🌈 Design Philosophy

- **Dark Theme**: Easy on the eyes for long study sessions
- **Glassmorphism**: Modern, premium feel
- **Gradients**: Visual hierarchy and attention guidance
- **Micro-animations**: Engaging hover effects
- **Responsive**: Mobile-first approach

## 📖 Usage Tips

1. **Start with Study Plan**: Get an overview of the 6-week roadmap
2. **Topic-by-Topic**: Study each topic systematically
3. **Read Thoroughly**: Answers include analogies, code examples, and interview tips
4. **Practice Mock Tests**: Test yourself regularly
5. **Explore Resources**: Dive deeper with external links

## 🔧 Customization

### Adding New Questions

Edit `src/data/interviewData.json`:

```json
{
  "id": 999,
  "question": "Your question here?",
  "answer": "Detailed answer with **markdown** support",
  "difficulty": "Medium",
  "tags": ["Tag1", "Tag2"]
}
```

### Changing Colors

Edit `tailwind.config.js`:

```js
colors: {
  primary: "#6366f1",    // Change primary color
  secondary: "#ec4899",  // Change secondary color
  background: "#0f172a", // Change background
}
```

## 🐛 Troubleshooting

### Blank Page / CSS Not Loading
- Ensure Tailwind CSS v3 is installed (not v4)
- Check `postcss.config.js` uses `tailwindcss` (not `@tailwindcss/postcss`)
- Restart dev server: `Ctrl+C` then `npm run dev`

### Port Already in Use
- Change port in `vite.config.js` or
- Kill process on port 5173

## 📄 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Feel free to fork, modify, and add more questions to help the community!

---

**Built with ❤️ for Java Full Stack Developer Freshers**
