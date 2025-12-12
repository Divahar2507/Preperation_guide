import { ExternalLink, BookOpen, Video, FileText, Code2 } from 'lucide-react';

const Resources = () => {
    const resources = [
        {
            category: 'Java Core',
            items: [
                { name: 'Official Java Documentation', url: 'https://docs.oracle.com/javase/', type: 'docs' },
                { name: 'Java Tutorial - w3schools', url: 'https://www.w3schools.com/java/', type: 'tutorial' },
                { name: 'Effective Java by Joshua Bloch', url: '#', type: 'book' },
            ]
        },
        {
            category: 'Spring Boot',
            items: [
                { name: 'Spring Official Guides', url: 'https://spring.io/guides', type: 'docs' },
                { name: 'Baeldung Spring Tutorials', url: 'https://www.baeldung.com/spring-boot', type: 'tutorial' },
                { name: 'Spring Boot in Action', url: '#', type: 'book' },
            ]
        },
        {
            category: 'React.js',
            items: [
                { name: 'React Official Docs', url: 'https://react.dev/', type: 'docs' },
                { name: 'React Tutorial - freeCodeCamp', url: 'https://www.freecodecamp.org/news/tag/react/', type: 'tutorial' },
                { name: 'JavaScript.info', url: 'https://javascript.info/', type: 'tutorial' },
            ]
        },
        {
            category: 'SQL & Databases',
            items: [
                { name: 'SQL Tutorial - Mode Analytics', url: 'https://mode.com/sql-tutorial/', type: 'tutorial' },
                { name: 'PostgreSQL Documentation', url: 'https://www.postgresql.org/docs/', type: 'docs' },
                { name: 'SQL Practice - LeetCode', url: 'https://leetcode.com/problemset/database/', type: 'practice' },
            ]
        },
        {
            category: 'DSA',
            items: [
                { name: 'LeetCode', url: 'https://leetcode.com/', type: 'practice' },
                { name: 'GeeksforGeeks', url: 'https://www.geeksforgeeks.org/', type: 'tutorial' },
                { name: 'Cracking the Coding Interview', url: '#', type: 'book' },
            ]
        },
    ];

    const getIcon = (type) => {
        switch (type) {
            case 'docs': return <FileText size={20} />;
            case 'tutorial': return <BookOpen size={20} />;
            case 'book': return <BookOpen size={20} />;
            case 'practice': return <Code2 size={20} />;
            default: return <ExternalLink size={20} />;
        }
    };

    return (
        <div className="max-w-6xl mx-auto space-y-8">
            <div className="flex items-center gap-4 mb-8">
                <div className="w-16 h-16 rounded-2xl bg-gradient-to-br from-primary to-secondary flex items-center justify-center shadow-lg shadow-primary/20">
                    <BookOpen className="text-white" size={32} />
                </div>
                <div>
                    <h1 className="text-4xl font-bold">Learning Resources</h1>
                    <p className="text-gray-400">Curated links to boost your interview preparation</p>
                </div>
            </div>

            <div className="space-y-6">
                {resources.map((section, idx) => (
                    <div key={idx}>
                        <h2 className="text-2xl font-bold mb-4 flex items-center gap-2">
                            <span className="text-primary">{section.category}</span>
                        </h2>
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                            {section.items.map((item, i) => (
                                <a
                                    key={i}
                                    href={item.url}
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    className="glass-card group hover:border-primary/50 flex items-center justify-between transition-all"
                                >
                                    <div className="flex items-center gap-3">
                                        <div className="p-2 rounded-lg bg-white/5 text-primary group-hover:bg-primary/10 transition-colors">
                                            {getIcon(item.type)}
                                        </div>
                                        <span className="font-medium group-hover:text-primary transition-colors">{item.name}</span>
                                    </div>
                                    <ExternalLink size={16} className="text-gray-500 group-hover:text-primary transition-colors" />
                                </a>
                            ))}
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Resources;
