import { useState } from 'react';
import { Calendar, Clock, CheckCircle2, Target } from 'lucide-react';
import data from '../data/interviewData.json';

const StudyPlan = () => {
    const [selectedWeek, setSelectedWeek] = useState(1);

    const studyPlan = [
        { week: 1, topic: 'Core Java', days: 7, questionsPerDay: 5 },
        { week: 2, topic: 'Spring Boot', days: 7, questionsPerDay: 4 },
        { week: 3, topic: 'Database (SQL)', days: 5, questionsPerDay: 5 },
        { week: 4, topic: 'React.js', days: 5, questionsPerDay: 4 },
        { week: 5, topic: 'Data Structures', days: 7, questionsPerDay: 5 },
        { week: 6, topic: 'HR & Mock Tests', days: 7, questionsPerDay: 3 },
    ];

    return (
        <div className="max-w-5xl mx-auto space-y-8">
            <div className="flex items-center gap-4 mb-8">
                <div className="w-16 h-16 rounded-2xl bg-gradient-to-br from-primary to-secondary flex items-center justify-center shadow-lg shadow-primary/20">
                    <Calendar className="text-white" size={32} />
                </div>
                <div>
                    <h1 className="text-4xl font-bold">Study Plan</h1>
                    <p className="text-gray-400">6-week structured interview preparation roadmap</p>
                </div>
            </div>

            {/* Progress Overview */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div className="glass-card">
                    <Target className="text-primary mb-2" size={24} />
                    <p className="text-2xl font-bold">42 Days</p>
                    <p className="text-sm text-gray-400">Total Duration</p>
                </div>
                <div className="glass-card">
                    <Clock className="text-secondary mb-2" size={24} />
                    <p className="text-2xl font-bold">2-3 hrs/day</p>
                    <p className="text-sm text-gray-400">Recommended Time</p>
                </div>
                <div className="glass-card">
                    <CheckCircle2 className="text-green-400 mb-2" size={24} />
                    <p className="text-2xl font-bold">0%</p>
                    <p className="text-sm text-gray-400">Completed</p>
                </div>
            </div>

            {/* Weekly Plan */}
            <div className="space-y-4">
                {studyPlan.map((plan) => (
                    <div
                        key={plan.week}
                        className={`glass-card cursor-pointer border transition-all ${selectedWeek === plan.week ? 'border-primary/50 bg-primary/5' : 'border-white/5'
                            }`}
                        onClick={() => setSelectedWeek(plan.week)}
                    >
                        <div className="flex items-center justify-between">
                            <div className="flex items-center gap-4">
                                <div className="w-12 h-12 rounded-xl bg-gradient-to-br from-primary/20 to-secondary/20 flex items-center justify-center font-bold text-lg">
                                    W{plan.week}
                                </div>
                                <div>
                                    <h3 className="text-xl font-bold">{plan.topic}</h3>
                                    <p className="text-sm text-gray-400">{plan.days} days • {plan.questionsPerDay} questions/day</p>
                                </div>
                            </div>
                            <div className="text-right">
                                <div className="w-16 h-16 rounded-full border-4 border-gray-700 flex items-center justify-center">
                                    <span className="text-sm font-bold">0%</span>
                                </div>
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default StudyPlan;
