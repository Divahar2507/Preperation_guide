import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import Home from './pages/Home';
import TopicQuestions from './pages/TopicQuestions';
import StudyPlan from './pages/StudyPlan';
import MockTest from './pages/MockTest';
import Resources from './pages/Resources';

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-background text-text flex">
        <Sidebar />
        <main className="flex-1 md:ml-64 p-4 md:p-8 overflow-x-hidden">
          <div className="max-w-7xl mx-auto">
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/topic/:id" element={<TopicQuestions />} />
              <Route path="/plan" element={<StudyPlan />} />
              <Route path="/mock" element={<MockTest />} />
              <Route path="/resources" element={<Resources />} />
            </Routes>
          </div>
        </main>
      </div>
    </Router>
  );
}

export default App;
