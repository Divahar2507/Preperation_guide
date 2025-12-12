import { useState } from 'react';
import { ChevronDown, ChevronUp, Copy, Check } from 'lucide-react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';

const QuestionCard = ({ data, index }) => {
    const [isOpen, setIsOpen] = useState(false);
    const [copied, setCopied] = useState(false);

    const handleCopy = (e) => {
        e.stopPropagation();
        navigator.clipboard.writeText(data.answer);
        setCopied(true);
        setTimeout(() => setCopied(false), 2000);
    };

    return (
        <div className="glass-card mb-4 border border-white/5 hover:border-white/10 transition-all">
            <div
                onClick={() => setIsOpen(!isOpen)}
                className="flex items-start justify-between cursor-pointer gap-4"
            >
                <div className="flex-1">
                    <div className="flex items-center gap-3 mb-2">
                        <span className="text-xs font-bold px-2 py-1 rounded bg-primary/10 text-primary border border-primary/20">
                            Q{index + 1}
                        </span>
                        <span className={`text-xs font-bold px-2 py-1 rounded border ${data.difficulty === 'Easy' ? 'bg-green-500/10 text-green-400 border-green-500/20' :
                                data.difficulty === 'Medium' ? 'bg-yellow-500/10 text-yellow-400 border-yellow-500/20' :
                                    'bg-red-500/10 text-red-400 border-red-500/20'
                            }`}>
                            {data.difficulty}
                        </span>
                    </div>
                    <h3 className="text-lg font-semibold text-gray-100 leading-snug">
                        {data.question}
                    </h3>
                </div>
                <button className="p-2 rounded-full hover:bg-white/5 text-gray-400 transition-colors">
                    {isOpen ? <ChevronUp size={20} /> : <ChevronDown size={20} />}
                </button>
            </div>

            <div className={`grid transition-all duration-300 ease-in-out ${isOpen ? 'grid-rows-[1fr] opacity-100 mt-4' : 'grid-rows-[0fr] opacity-0'}`}>
                <div className="overflow-hidden">
                    <div className="relative bg-black/20 rounded-xl p-4 border border-white/5">
                        <button
                            onClick={handleCopy}
                            className="absolute top-2 right-2 p-2 rounded-lg bg-white/5 hover:bg-white/10 text-gray-400 hover:text-white transition-all z-10"
                            title="Copy Answer"
                        >
                            {copied ? <Check size={16} className="text-green-400" /> : <Copy size={16} />}
                        </button>

                        <div className="prose prose-invert prose-sm max-w-none prose-headings:text-primary prose-a:text-blue-400 prose-code:text-secondary prose-pre:bg-black/40 prose-pre:border prose-pre:border-white/10 text-gray-300 leading-relaxed">
                            <ReactMarkdown
                                remarkPlugins={[remarkGfm]}
                                components={{
                                    code({ node, inline, className, children, ...props }) {
                                        return !inline ? (
                                            <code className="block bg-black/40 p-4 rounded-lg my-4 text-sm font-mono overflow-x-auto border border-white/5" {...props}>
                                                {children}
                                            </code>
                                        ) : (
                                            <code className="bg-white/10 px-1 py-0.5 rounded text-secondary font-mono text-xs" {...props}>
                                                {children}
                                            </code>
                                        )
                                    }
                                }}
                            >
                                {data.answer}
                            </ReactMarkdown>
                        </div>

                        <div className="mt-6 flex flex-wrap gap-2 pt-4 border-t border-white/5">
                            {data.tags.map((tag, i) => (
                                <span key={i} className="text-xs px-2 py-1 rounded-full bg-white/5 text-gray-400 border border-white/5">
                                    #{tag}
                                </span>
                            ))}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default QuestionCard;
