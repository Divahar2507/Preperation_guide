import { useState, useRef, useEffect } from 'react';
import { Timer, Play, Check, X, Mic, MicOff, Volume2, Sparkles } from 'lucide-react';
import data from '../data/interviewData.json';

const MockTest = () => {
    const [started, setStarted] = useState(false);
    const [currentQ, setCurrentQ] = useState(0);
    const [score, setScore] = useState(0);
    const [showAnswer, setShowAnswer] = useState(false);
    const [completed, setCompleted] = useState(false);
    const [isRecording, setIsRecording] = useState(false);
    const [transcript, setTranscript] = useState('');
    const [isVerifying, setIsVerifying] = useState(false);
    const [verificationResult, setVerificationResult] = useState(null);
    const [recordingSupported, setRecordingSupported] = useState(true);
    const [thinkingTime, setThinkingTime] = useState(30);
    const [isThinking, setIsThinking] = useState(false);
    const [timerStarted, setTimerStarted] = useState(false);
    const [answerTime, setAnswerTime] = useState(0);
    const [isAnswering, setIsAnswering] = useState(false);
    const [answerStartTime, setAnswerStartTime] = useState(null);

    const recognitionRef = useRef(null);
    const timerRef = useRef(null);
    const answerTimerRef = useRef(null);

    // Get 10 random questions
    const allQuestions = data.topics.flatMap(t => t.questions);
    const mockQuestions = allQuestions.slice(0, 10);

    useEffect(() => {
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        if (!SpeechRecognition) {
            setRecordingSupported(false);
            return;
        }

        const recognition = new SpeechRecognition();
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.lang = 'en-US';

        recognition.onresult = (event) => {
            const transcriptText = event.results[0][0].transcript;
            setTranscript(transcriptText);
            setIsRecording(false);
        };

        recognition.onerror = (event) => {
            console.error('Speech recognition error:', event.error);
            setIsRecording(false);
        };

        recognition.onend = () => {
            setIsRecording(false);
        };

        recognitionRef.current = recognition;

        return () => {
            if (recognitionRef.current) {
                recognitionRef.current.stop();
            }
        };
    }, []);

    const startTest = () => {
        setStarted(true);
        setCurrentQ(0);
        setScore(0);
        setCompleted(false);
        setTranscript('');
        setVerificationResult(null);
        setTimerStarted(false);
        setThinkingTime(30);
        setIsThinking(false);
    };

    const startThinkingTimer = () => {
        setIsThinking(true);
        setTimerStarted(true);
        setThinkingTime(30);

        timerRef.current = setInterval(() => {
            setThinkingTime(prev => {
                if (prev <= 1) {
                    clearInterval(timerRef.current);
                    setIsThinking(false);
                    return 0;
                }
                return prev - 1;
            });
        }, 1000);
    };

    const skipThinking = () => {
        if (timerRef.current) {
            clearInterval(timerRef.current);
        }
        setIsThinking(false);
        setThinkingTime(0);
    };

    const toggleRecording = () => {
        if (isRecording) {
            recognitionRef.current?.stop();
            setIsRecording(false);
            stopAnswerTimer();
        } else {
            setTranscript('');
            setVerificationResult(null);
            recognitionRef.current?.start();
            setIsRecording(true);
            startAnswerTimer();
        }
    };

    const startAnswerTimer = () => {
        setIsAnswering(true);
        setAnswerStartTime(Date.now());
        setAnswerTime(0);

        answerTimerRef.current = setInterval(() => {
            setAnswerTime(prev => prev + 1);
        }, 1000);
    };

    const stopAnswerTimer = () => {
        if (answerTimerRef.current) {
            clearInterval(answerTimerRef.current);
        }
        setIsAnswering(false);
    };

    const extractKeyConcepts = (answer) => {
        const concepts = [];
        const boldMatches = answer.match(/\*\*(.*?)\*\*/g);
        if (boldMatches) {
            boldMatches.forEach(match => concepts.push(match.replace(/\*\*/g, '')));
        }
        const headingMatches = answer.match(/###\s+(.*?)[\n]/g);
        if (headingMatches) {
            headingMatches.forEach(match => concepts.push(match.replace(/###\s+/g, '').trim()));
        }
        return concepts.slice(0, 5);
    };

    const getFeedback = (score) => {
        if (score >= 70) return "Excellent! Covered all key points.";
        if (score >= 50) return "Good! Got most important concepts.";
        if (score >= 25) return "Satisfactory. Mentioned some key points.";
        return "Needs improvement. Review the answer.";
    };

    const verifyAnswer = () => {
        if (!transcript.trim()) return;

        setIsVerifying(true);
        const currentQuestion = mockQuestions[currentQ];
        const correctAnswer = currentQuestion.answer.toLowerCase();
        const userAnswer = transcript.toLowerCase();

        // Enhanced keyword extraction
        const cleanAnswer = correctAnswer
            .replace(/```[\s\S]*?```/g, '')
            .replace(/[#*`\n]/g, ' ')
            .replace(/\b(the|is|are|a|an|and|or|but|in|on|at|to|for|of|with|by)\b/g, '')
            .trim();

        const keywords = cleanAnswer.split(/\W+/).filter(w => w.length > 3).slice(0, 15);
        const matchedKeywords = keywords.filter(keyword => userAnswer.includes(keyword));
        const matchPercentage = (matchedKeywords.length / keywords.length) * 100;

        // Check key concepts
        const keyConcepts = extractKeyConcepts(correctAnswer);
        const conceptMatches = keyConcepts.filter(concept =>
            userAnswer.includes(concept.toLowerCase())
        ).length;
        const conceptScore = keyConcepts.length > 0 ? (conceptMatches / keyConcepts.length) * 100 : 0;

        // Combined score
        const finalScore = (matchPercentage * 0.7) + (conceptScore * 0.3);
        const isCorrect = finalScore >= 25;

        setTimeout(() => {
            setVerificationResult({
                isCorrect,
                matchPercentage: finalScore.toFixed(0),
                matchedKeywords: matchedKeywords.length,
                totalKeywords: keywords.length,
                conceptMatches,
                totalConcepts: keyConcepts.length,
                feedback: getFeedback(finalScore)
            });
            setIsVerifying(false);
        }, 1000);
    };

    const speakCorrectAnswer = () => {
        const currentQuestion = mockQuestions[currentQ];
        const cleanAnswer = currentQuestion.answer
            .replace(/```[\s\S]*?```/g, 'code example omitted')
            .replace(/[#*`]/g, '')
            .replace(/\n+/g, '. ');
        const utterance = new SpeechSynthesisUtterance(cleanAnswer);
        utterance.rate = 0.85;
        utterance.pitch = 1;
        window.speechSynthesis.speak(utterance);
    };

    const handleNext = (correct) => {
        if (correct !== undefined) {
            if (correct) setScore(score + 1);
        } else if (verificationResult?.isCorrect) {
            setScore(score + 1);
        }

        if (currentQ < mockQuestions.length - 1) {
            setCurrentQ(currentQ + 1);
            setShowAnswer(false);
            setTranscript('');
            setVerificationResult(null);
            setTimerStarted(false);
            setThinkingTime(30);
            setIsThinking(false);
            setAnswerTime(0);
            setIsAnswering(false);
            if (timerRef.current) clearInterval(timerRef.current);
            if (answerTimerRef.current) clearInterval(answerTimerRef.current);
        } else {
            setCompleted(true);
            if (timerRef.current) clearInterval(timerRef.current);
        }
    };

    // Cleanup timers on unmount
    useEffect(() => {
        return () => {
            if (timerRef.current) clearInterval(timerRef.current);
            if (answerTimerRef.current) clearInterval(answerTimerRef.current);
        };
    }, []);

    const formatTime = (seconds) => {
        const mins = Math.floor(seconds / 60);
        const secs = seconds % 60;
        return `${mins}:${secs.toString().padStart(2, '0')}`;
    };

    const speakQuestion = () => {
        const utterance = new SpeechSynthesisUtterance(mockQuestions[currentQ].question);
        utterance.rate = 0.9;
        utterance.pitch = 1;
        window.speechSynthesis.speak(utterance);
    };

    if (!started) {
        return (
            <div className="max-w-3xl mx-auto">
                <div className="glass-card text-center p-12">
                    <div className="w-24 h-24 rounded-full bg-gradient-to-br from-primary to-secondary flex items-center justify-center mx-auto mb-6 shadow-lg shadow-primary/30">
                        <Timer className="text-white" size={48} />
                    </div>
                    <h1 className="text-4xl font-bold mb-4">🎤 Voice Mock Interview</h1>
                    <p className="text-gray-400 mb-4 max-w-md mx-auto">
                        Test your knowledge with voice! Record your answers and get instant AI verification.
                    </p>
                    {!recordingSupported && (
                        <div className="bg-red-500/10 border border-red-500/30 rounded-xl p-4 mb-6 mx-auto max-w-md">
                            <p className="text-red-400 text-sm">
                                ⚠️ Voice recording not supported in your browser. Try Chrome or Edge.
                            </p>
                        </div>
                    )}
                    <button onClick={startTest} className="btn-primary inline-flex items-center gap-2">
                        <Play size={20} />
                        Start Voice Test
                    </button>
                </div>
            </div>
        );
    }

    if (completed) {
        const percentage = (score / mockQuestions.length) * 100;
        return (
            <div className="max-w-3xl mx-auto">
                <div className="glass-card text-center p-12">
                    <div className={`w-32 h-32 rounded-full ${percentage >= 70 ? 'bg-green-500/20 border-4 border-green-500' : 'bg-red-500/20 border-4 border-red-500'} flex items-center justify-center mx-auto mb-6`}>
                        <span className="text-5xl font-bold">{percentage.toFixed(0)}%</span>
                    </div>
                    <h1 className="text-4xl font-bold mb-4">Test Completed! 🎉</h1>
                    <p className="text-2xl text-gray-300 mb-8">
                        You scored <span className="text-primary font-bold">{score}</span> out of {mockQuestions.length}
                    </p>
                    <button onClick={startTest} className="btn-primary">
                        Retake Test
                    </button>
                </div>
            </div>
        );
    }

    const currentQuestion = mockQuestions[currentQ];

    return (
        <div className="max-w-4xl mx-auto space-y-6">
            {/* Progress Bar */}
            <div className="glass-card">
                <div className="flex items-center justify-between mb-2">
                    <span className="text-sm font-semibold">Question {currentQ + 1} of {mockQuestions.length}</span>
                    <span className="text-sm text-gray-400">Score: {score}/{currentQ || 1}</span>
                </div>
                <div className="w-full h-2 bg-black/20 rounded-full overflow-hidden">
                    <div
                        className="h-full bg-gradient-to-r from-primary to-secondary transition-all duration-300"
                        style={{ width: `${((currentQ + 1) / mockQuestions.length) * 100}%` }}
                    />
                </div>
            </div>

            {/* Question Card */}
            <div className="glass-card">
                <div className="flex items-center justify-between mb-4">
                    <span className={`text-xs font-bold px-2 py-1 rounded border ${currentQuestion.difficulty === 'Easy' ? 'bg-green-500/10 text-green-400 border-green-500/20' :
                        currentQuestion.difficulty === 'Medium' ? 'bg-yellow-500/10 text-yellow-400 border-yellow-500/20' :
                            'bg-red-500/10 text-red-400 border-red-500/20'
                        }`}>
                        {currentQuestion.difficulty}
                    </span>
                    <button
                        onClick={speakQuestion}
                        className="p-2 rounded-lg bg-white/5 hover:bg-white/10 transition-all text-primary"
                        title="Listen to question"
                    >
                        <Volume2 size={20} />
                    </button>
                </div>

                <h2 className="text-2xl font-bold mb-6 leading-snug">{currentQuestion.question}</h2>

                {/* Thinking Timer */}
                {!timerStarted && !showAnswer && (
                    <div className="mb-6">
                        <button
                            onClick={startThinkingTimer}
                            className="btn-primary inline-flex items-center gap-2"
                        >
                            <Timer size={20} />
                            Start Thinking Timer (30s)
                        </button>
                        <p className="text-sm text-gray-400 mt-2">
                            Take time to think about your answer before recording
                        </p>
                    </div>
                )}

                {isThinking && (
                    <div className="mb-6 p-6 rounded-xl bg-gradient-to-r from-primary/10 to-secondary/10 border border-primary/30">
                        <div className="flex items-center justify-between mb-4">
                            <div className="flex items-center gap-3">
                                <div className="w-16 h-16 rounded-full bg-primary/20 flex items-center justify-center">
                                    <span className="text-3xl font-bold text-primary">{thinkingTime}</span>
                                </div>
                                <div>
                                    <p className="font-bold text-lg">Thinking Time</p>
                                    <p className="text-sm text-gray-400">Prepare your answer...</p>
                                </div>
                            </div>
                            <button
                                onClick={skipThinking}
                                className="px-4 py-2 rounded-lg bg-white/10 hover:bg-white/20 transition-all text-sm"
                            >
                                Skip & Answer Now
                            </button>
                        </div>
                        <div className="w-full h-2 bg-black/20 rounded-full overflow-hidden">
                            <div
                                className="h-full bg-gradient-to-r from-primary to-secondary transition-all duration-1000"
                                style={{ width: `${(thinkingTime / 30) * 100}%` }}
                            />
                        </div>
                    </div>
                )}

                {/* Voice Recording Section */}
                {recordingSupported && !showAnswer && !isThinking && timerStarted && (
                    <div className="space-y-4">
                        <div className="flex items-center justify-center gap-4">
                            <button
                                onClick={toggleRecording}
                                disabled={isVerifying}
                                className={`w-16 h-16 rounded-full flex items-center justify-center transition-all shadow-lg ${isRecording
                                    ? 'bg-red-500 hover:bg-red-600 animate-pulse'
                                    : 'bg-primary hover:bg-primary/80'
                                    }`}
                            >
                                {isRecording ? <MicOff className="text-white" size={28} /> : <Mic className="text-white" size={28} />}
                            </button>
                            {transcript && !isRecording && (
                                <button
                                    onClick={verifyAnswer}
                                    disabled={isVerifying}
                                    className="btn-primary inline-flex items-center gap-2"
                                >
                                    <Sparkles size={20} />
                                    {isVerifying ? 'Verifying...' : 'Verify Answer'}
                                </button>
                            )}
                        </div>

                        {/* Answer Time Display */}
                        {isAnswering && (
                            <div className="text-center">
                                <div className="inline-flex items-center gap-2 px-4 py-2 rounded-lg bg-red-500/10 border border-red-500/30">
                                    <Timer className="text-red-400 animate-pulse" size={16} />
                                    <span className="text-red-400 font-mono font-bold">{formatTime(answerTime)}</span>
                                    <span className="text-gray-400 text-sm">answering...</span>
                                </div>
                            </div>
                        )}

                        {answerTime > 0 && !isAnswering && transcript && (
                            <div className="text-center text-sm text-gray-400">
                                ⏱️ Answered in {formatTime(answerTime)}
                            </div>
                        )}

                        <p className="text-center text-sm text-gray-400">
                            {isRecording ? '🎙️ Recording... Speak your answer' : transcript ? '✅ Recording captured' : 'Click mic to record your answer'}
                        </p>

                        {/* Transcript Display */}
                        {transcript && (
                            <div className="bg-black/20 rounded-xl p-4 border border-white/5">
                                <p className="text-xs text-gray-500 mb-2">Your Answer:</p>
                                <p className="text-gray-300">{transcript}</p>
                            </div>
                        )}

                        {/* Verification Result */}
                        {verificationResult && (
                            <div className={`rounded-xl p-5 border ${verificationResult.isCorrect
                                ? 'bg-green-500/10 border-green-500/30'
                                : 'bg-orange-500/10 border-orange-500/30'
                                }`}>
                                <div className="flex items-center justify-between mb-3">
                                    <div className="flex items-center gap-2">
                                        {verificationResult.isCorrect ? (
                                            <Check className="text-green-400" size={24} />
                                        ) : (
                                            <X className="text-orange-400" size={24} />
                                        )}
                                        <span className={`font-bold text-lg ${verificationResult.isCorrect ? 'text-green-400' : 'text-orange-400'}`}>
                                            {verificationResult.isCorrect ? 'Good Answer!' : 'Needs Improvement'}
                                        </span>
                                    </div>
                                    <button
                                        onClick={speakCorrectAnswer}
                                        className="p-2 rounded-lg bg-white/5 hover:bg-white/10 transition-all flex items-center gap-2 text-sm text-primary"
                                        title="Listen to correct answer"
                                    >
                                        <Volume2 size={18} />
                                        <span>Hear Answer</span>
                                    </button>
                                </div>
                                <p className="text-sm text-gray-300 mb-2">{verificationResult.feedback}</p>
                                <div className="flex gap-4 text-xs text-gray-400">
                                    <span>📝 Keywords: {verificationResult.matchedKeywords}/{verificationResult.totalKeywords}</span>
                                    <span>🎯 Concepts: {verificationResult.conceptMatches}/{verificationResult.totalConcepts}</span>
                                    <span>📊 Score: {verificationResult.matchPercentage}%</span>
                                    {answerTime > 0 && <span>⏱️ Time: {formatTime(answerTime)}</span>}
                                </div>
                            </div>
                        )}
                    </div>
                )}

                {/* Show Answer Button / Manual Evaluation */}
                {!showAnswer ? (
                    <div className="mt-4">
                        <button
                            onClick={() => setShowAnswer(true)}
                            className="text-primary hover:text-primary/80 text-sm underline"
                        >
                            Show correct answer
                        </button>
                    </div>
                ) : (
                    <div className="space-y-4 mt-6">
                        <div className="bg-black/20 rounded-xl p-6 border border-white/5">
                            <p className="text-gray-300 whitespace-pre-line leading-relaxed">{currentQuestion.answer}</p>
                        </div>

                        <div className="flex gap-4">
                            {verificationResult ? (
                                <button
                                    onClick={() => handleNext()}
                                    className="flex-1 py-3 bg-primary hover:bg-primary/80 text-white rounded-xl font-bold transition-all"
                                >
                                    Next Question
                                </button>
                            ) : (
                                <>
                                    <button
                                        onClick={() => handleNext(true)}
                                        className="flex-1 py-3 bg-green-500/20 hover:bg-green-500/30 text-green-400 rounded-xl font-bold border border-green-500/30 transition-all flex items-center justify-center gap-2"
                                    >
                                        <Check size={20} />
                                        I Got It Right
                                    </button>
                                    <button
                                        onClick={() => handleNext(false)}
                                        className="flex-1 py-3 bg-red-500/20 hover:bg-red-500/30 text-red-400 rounded-xl font-bold border border-red-500/30 transition-all flex items-center justify-center gap-2"
                                    >
                                        <X size={20} />
                                        I Got It Wrong
                                    </button>
                                </>
                            )}
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default MockTest;
