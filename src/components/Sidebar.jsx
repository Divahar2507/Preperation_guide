import { Link, useLocation } from 'react-router-dom';
import { Icons } from './Icons';

const Sidebar = () => {
    const location = useLocation();
    const isActive = (path) => location.pathname === path;

    const navItems = [
        { name: 'Dashboard', path: '/', icon: 'Layers' },
        { name: 'Study Plan', path: '/plan', icon: 'Clock' },
        { name: 'Mock Test', path: '/mock', icon: 'Activity' },
        { name: 'Resources', path: '/resources', icon: 'BookOpen' },
    ];

    return (
        <aside className="fixed left-0 top-0 h-screen w-64 bg-surface/50 backdrop-blur-xl border-r border-white/10 hidden md:flex flex-col z-50">
            <div className="p-6">
                <div className="flex items-center gap-3 mb-8">
                    <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-primary to-secondary flex items-center justify-center shadow-lg shadow-primary/20">
                        <Icons.GraduationCap className="text-white" size={24} />
                    </div>
                    <div>
                        <h1 className="font-bold text-lg tracking-tight">PrepMaster</h1>
                        <p className="text-xs text-gray-400">Java FS Edition</p>
                    </div>
                </div>

                <nav className="space-y-2">
                    {navItems.map((item) => {
                        const Icon = Icons[item.icon];
                        return (
                            <Link
                                key={item.path}
                                to={item.path}
                                className={`nav-item ${isActive(item.path) ? 'active' : ''}`}
                            >
                                <Icon size={20} />
                                <span>{item.name}</span>
                            </Link>
                        );
                    })}
                </nav>
            </div>

            <div className="mt-auto p-6">
                <div className="glass-card bg-gradient-to-br from-primary/10 to-secondary/10 border-primary/20 p-4">
                    <div className="flex items-center justify-between mb-2">
                        <span className="text-xs font-semibold text-primary">Daily Goal</span>
                        <span className="text-xs text-secondary">3/5</span>
                    </div>
                    <div className="w-full h-2 bg-black/20 rounded-full overflow-hidden">
                        <div className="h-full w-3/5 bg-gradient-to-r from-primary to-secondary rounded-full" />
                    </div>
                    <p className="text-[10px] text-gray-400 mt-2">Keep going! You're doing great.</p>
                </div>
            </div>
        </aside>
    );
};

export default Sidebar;
