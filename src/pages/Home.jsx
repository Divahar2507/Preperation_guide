import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import TopicCard from '../components/TopicCard';
import data from '../data/interviewData.json';
import { Icons } from '../components/Icons';

const Home = () => {
    const { topics, stats } = data;
    const navigate = useNavigate();

    return (
        <div className="space-y-8">
            {/* Hero Section */}
            <div className="relative overflow-hidden rounded-3xl bg-gradient-to-r from-primary to-secondary p-8 md:p-12 text-white shadow-2xl">
                <div className="absolute top-0 right-0 -mt-10 -mr-10 w-64 h-64 bg-white opacity-10 rounded-full blur-3xl"></div>
                <div className="absolute bottom-0 left-0 -mb-10 -ml-10 w-64 h-64 bg-black opacity-10 rounded-full blur-3xl"></div>

                <div className="relative z-10 max-w-2xl">
                    <h1 className="text-4xl md:text-5xl font-bold mb-4 leading-tight">
                        Master Your Java Full Stack Interview
                    </h1>
                    <p className="text-primary-100 text-lg mb-8 opacity-90">
                        Comprehensive preparation guide covering Java, Spring Boot, React, SQL, and more.
                    </p>
                    <button
                        onClick={() => navigate('/mock')}
                        className="bg-white text-primary font-bold py-3 px-8 rounded-full shadow-lg hover:shadow-xl hover:scale-105 transition-all active:scale-95"
                    >
                        Start Mock Test
                    </button>
                </div>
            </div>

            {/* Stats Grid */}
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                {[
                    { label: 'Total Questions', value: stats.totalQuestions, icon: 'Database', color: 'text-blue-400' },
                    { label: 'Completed', value: stats.completedQuestions, icon: 'CheckCircle', color: 'text-green-400' },
                    { label: 'Topics', value: stats.topicsCovered, icon: 'Layers', color: 'text-purple-400' },
                    { label: 'Day Streak', value: stats.streak, icon: 'Activity', color: 'text-orange-400' },
                ].map((stat, i) => {
                    const Icon = Icons[stat.icon];
                    return (
                        <div key={i} className="glass-card flex items-center gap-4">
                            <div className={`p-3 rounded-xl bg-white/5 ${stat.color}`}>
                                <Icon size={24} />
                            </div>
                            <div>
                                <p className="text-2xl font-bold">{stat.value}</p>
                                <p className="text-xs text-gray-400">{stat.label}</p>
                            </div>
                        </div>
                    );
                })}
            </div>

            {/* Topics Grid */}
            <div>
                <h2 className="text-2xl font-bold mb-6 flex items-center gap-2">
                    <Icons.BookOpen className="text-primary" />
                    <span>Study Topics</span>
                </h2>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {topics.map((topic) => (
                        <TopicCard key={topic.id} topic={topic} />
                    ))}
                </div>
            </div>
        </div>
    );
};

export default Home;
