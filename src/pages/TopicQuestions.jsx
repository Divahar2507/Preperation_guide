import { useParams, useNavigate } from 'react-router-dom';
import { ArrowLeft } from 'lucide-react';
import QuestionCard from '../components/QuestionCard';
import data from '../data/interviewData.json';
import { Icons } from '../components/Icons';

const TopicQuestions = () => {
    const { id } = useParams();
    const navigate = useNavigate();
    const topic = data.topics.find(t => t.id === id);

    if (!topic) return <div className="p-8 text-center">Topic not found</div>;

    const Icon = Icons[topic.icon] || Icons.Code;

    return (
        <div className="max-w-4xl mx-auto space-y-6">
            <button
                onClick={() => navigate('/')}
                className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors mb-4 group"
            >
                <ArrowLeft size={20} className="group-hover:-translate-x-1 transition-transform" />
                <span>Back to Topics</span>
            </button>

            <div className="flex items-center gap-6 mb-8">
                <div className="w-20 h-20 rounded-2xl bg-gradient-to-br from-primary to-secondary flex items-center justify-center shadow-lg shadow-primary/20">
                    <Icon className="text-white" size={40} />
                </div>
                <div>
                    <h1 className="text-4xl font-bold mb-2">{topic.title}</h1>
                    <p className="text-gray-400">{topic.description}</p>
                </div>
            </div>

            <div className="space-y-4">
                {topic.questions.map((q, index) => (
                    <QuestionCard key={q.id} data={q} index={index} />
                ))}
            </div>

            {topic.questions.length === 0 && (
                <div className="text-center py-20 bg-white/5 rounded-2xl border border-dashed border-white/10">
                    <Icons.Coffee size={48} className="mx-auto text-gray-600 mb-4" />
                    <p className="text-gray-400">No questions added yet for this topic.</p>
                </div>
            )}
        </div>
    );
};

export default TopicQuestions;
