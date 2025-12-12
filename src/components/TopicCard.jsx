import { useNavigate } from 'react-router-dom';
import { Icons } from './Icons';

const TopicCard = ({ topic }) => {
    const navigate = useNavigate();
    const Icon = Icons[topic.icon] || Icons.Code;

    return (
        <div
            onClick={() => navigate(`/topic/${topic.id}`)}
            className="glass-card group cursor-pointer border border-white/5 hover:border-primary/50 relative overflow-hidden"
        >
            <div className="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
                <Icon size={100} />
            </div>

            <div className="relative z-10">
                <div className="w-12 h-12 rounded-xl bg-gradient-to-br from-primary/20 to-secondary/20 flex items-center justify-center mb-4 group-hover:scale-110 transition-transform duration-300">
                    <Icon className="text-primary" size={24} />
                </div>

                <h3 className="text-xl font-bold mb-2 group-hover:text-primary transition-colors">{topic.title}</h3>
                <p className="text-gray-400 text-sm mb-4 line-clamp-2">{topic.description}</p>

                <div className="flex items-center gap-2 text-sm font-medium text-primary/80 group-hover:text-primary group-hover:translate-x-1 transition-all">
                    <span>{topic.questions.length} Questions</span>
                    <Icons.ArrowRight size={16} />
                </div>
            </div>
        </div>
    );
};

export default TopicCard;
