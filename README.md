# 🎓 Java Full-Stack Interview Preparation Platform

> A comprehensive, AI-powered interview preparation platform with voice recording, smart validation, and 88+ curated questions.

[![Live Demo](https://img.shields.io/badge/demo-live-success)](https://your-demo-url.vercel.app)
[![GitHub](https://img.shields.io/github/license/Divahar2507/Preperation_guide)](LICENSE)
[![React](https://img.shields.io/badge/React-19-blue)](https://reactjs.org/)
[![Vite](https://img.shields.io/badge/Vite-5-purple)](https://vitejs.dev/)

## ✨ Features

### 🎤 Voice Mock Interview
- **Voice Recording** with Web Speech API
- **AI Answer Validation** using keyword + concept matching
- **Thinking Timer** (30 seconds to prepare)
- **Answer Timer** (tracks response time)
- **Audio Playback** of questions and correct answers
- **Real-time Transcription**
- **Smart Feedback** with detailed metrics

### 📚 Comprehensive Question Bank
- **88 Interview Questions** across 6 modules
- **Detailed Answers** with code examples
- **Markdown Support** for formatting
- **Difficulty Levels** (Easy/Medium/Hard)
- **Tag System** for categorization

### 🎯 Study Tools
- **6-Week Study Plan** with roadmap
- **Progress Tracking** with stats
- **External Resources** (LeetCode, GeeksforGeeks, etc.)
- **Topic-wise Navigation**

### 🎨 Beautiful UI
- **Glassmorphism Design** with dark theme
- **Fully Responsive** (mobile, tablet, desktop)
- **Smooth Animations**
- **Premium Look & Feel**

## 📊 Question Coverage

| Module | Questions | Topics Covered |
|--------|-----------|----------------|
| ☕ Core Java | 20 | OOPs, Collections, Multithreading, Java 8+, Exception Handling |
| 🍃 Spring Boot | 15 | DI, Annotations, JPA, REST APIs, Transactions, Microservices |
| 🗄️ Database/SQL | 13 | Joins, Keys, Normalization, ACID, Indexes, Triggers |
| ⚛️ React.js | 10 | Hooks, Components, State, Redux, API Integration |
| 💻 DSA | 10 | Sorting, Trees, Graphs, BFS/DFS, Algorithms |
| 👔 HR | 9 | STAR method, Behavioral, Career Goals |

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ 
- npm or yarn

### Installation

```bash
# Clone the repository
git clone https://github.com/Divahar2507/Preperation_guide.git

# Navigate to project directory
cd Preperation_guide

# Install dependencies
npm install

# Start development server
npm run dev
```

Open [http://localhost:5173](http://localhost:5173) in your browser.

## 📦 Build for Production

```bash
npm run build
```

The optimized build will be in the `dist/` folder.

## 🌐 Deploy

### Deploy to Vercel (Recommended)

1. Push your code to GitHub
2. Go to [Vercel](https://vercel.com)
3. Import your repository
4. Deploy!

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/Divahar2507/Preperation_guide)

### Deploy to Netlify

1. Push your code to GitHub
2. Go to [Netlify](https://netlify.com)
3. Import your repository
4. Build command: `npm run build`
5. Publish directory: `dist`

[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/Divahar2507/Preperation_guide)

## 🛠️ Tech Stack

- **Frontend:** React 19 + Vite
- **Routing:** React Router DOM v7
- **Styling:** Tailwind CSS v3
- **Icons:** Lucide React
- **Markdown:** react-markdown + remark-gfm
- **Voice:** Web Speech API
- **Data:** JSON (no backend required)

## 📁 Project Structure

```
interview_preperation/
├── src/
│   ├── components/       # Reusable UI components
│   │   ├── Sidebar.jsx
│   │   ├── TopicCard.jsx
│   │   ├── QuestionCard.jsx
│   │   └── Icons.jsx
│   ├── pages/           # Page components
│   │   ├── Home.jsx
│   │   ├── TopicQuestions.jsx
│   │   ├── MockTest.jsx
│   │   ├── StudyPlan.jsx
│   │   └── Resources.jsx
│   ├── data/            # Question database
│   │   └── interviewData.json
│   ├── App.jsx          # Main app component
│   └── index.css        # Global styles
├── public/              # Static assets
├── index.html
├── package.json
├── vite.config.js
└── tailwind.config.js
```

## 🎯 How to Use

### 1. Browse Questions
- Navigate to any topic from the dashboard
- Read detailed answers with code examples
- Copy answers to clipboard

### 2. Take Mock Test
1. Click "Mock Test" in sidebar
2. Start thinking timer (30s optional)
3. Record your answer with voice
4. Get AI validation with detailed feedback
5. Listen to correct answer
6. Track your time and score

### 3. Follow Study Plan
- 6-week structured roadmap
- Daily topics and goals
- Progress tracking

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Add More Questions**
   - Edit `src/data/interviewData.json`
   - Follow the existing format
   - Include detailed answers with examples

2. **Improve Features**
   - Enhance AI validation algorithm
   - Add new study tools
   - Improve UI/UX

3. **Fix Bugs**
   - Report issues
   - Submit pull requests

### Contribution Guidelines

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Adding Questions

To add new questions, edit `src/data/interviewData.json`:

```json
{
  "id": 100,
  "question": "Your question here?",
  "answer": "Detailed answer with **markdown** support\n\n### Code Example\n```java\ncode here\n```",
  "difficulty": "Medium",
  "tags": ["tag1", "tag2"]
}
```

## 🎨 Customization

### Change Theme Colors

Edit `tailwind.config.js`:

```javascript
colors: {
  primary: '#6366f1',    // Change primary color
  secondary: '#8b5cf6',  // Change secondary color
  // ... other colors
}
```

### Modify Timer Duration

Edit `src/pages/MockTest.jsx`:

```javascript
const [thinkingTime, setThinkingTime] = useState(30); // Change to desired seconds
```

## 🌟 Features Roadmap

- [ ] User authentication
- [ ] Progress persistence (localStorage)
- [ ] Question bookmarking
- [ ] Custom study plans
- [ ] Performance analytics
- [ ] Mobile app (React Native)
- [ ] Offline mode (PWA)
- [ ] Multi-language support

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Divahar P**
- GitHub: [@Divahar2507](https://github.com/Divahar2507)
- LinkedIn: [Divahar P](https://linkedin.com/in/divahar-p)

## 🙏 Acknowledgments

- Questions sourced from GeeksforGeeks, Baeldung, InterviewBit, freeCodeCamp
- Built with React and Vite
- UI inspired by modern design trends

## 📞 Support

If you find this helpful, please ⭐ star the repository!

For issues or questions:
- Open an [Issue](https://github.com/Divahar2507/Preperation_guide/issues)
- Start a [Discussion](https://github.com/Divahar2507/Preperation_guide/discussions)

## 🚀 Live Demo

Try it out: [Live Demo](https://your-demo-url.vercel.app)

---

**Made with ❤️ for Java Full-Stack Developers preparing for interviews**

**Star ⭐ this repo if you found it helpful!**
