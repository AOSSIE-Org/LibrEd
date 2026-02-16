import { createFileRoute, Link, useParams, useNavigate } from '@tanstack/react-router'
import { useStreamStructure, useTheory } from '../../hooks/useData'
import Markdown from '../../components/mdx-content'
import { BookOpen, ArrowRight, Play, CheckCircle, XCircle, Timer, Github } from 'lucide-react'
import { useState, useEffect } from 'react'
import { APP_CONFIG } from '../../config'

export const Route = createFileRoute('/$examId/$streamId/$subjectSlug/$topicSlug')({
    component: TopicView
})

interface QuestionData {
    question_text: string
    answer_text: string
    explanation_text: string
    type: 'MCQ' | 'MSQ' | 'NAT'
    year: string
}

function TopicView() {
    const navigate = useNavigate()
    const { examId, streamId, subjectSlug, topicSlug } = useParams({
        from: '/$examId/$streamId/$subjectSlug/$topicSlug'
    })

    const { data: structure, loading: structureLoading } = useStreamStructure(examId, streamId)
    const [mdPath, setMdPath] = useState<string | undefined>()
    const [topicName, setTopicName] = useState<string>('')
    const [subjectName, setSubjectName] = useState<string>('')
    const [questionPaths, setQuestionPaths] = useState<string[]>([])

    const { content: theory, loading: theoryLoading } = useTheory(examId, streamId, mdPath)

    // Assessment state
    const [isAssessmentActive, setIsAssessmentActive] = useState(false)
    const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0)
    const [timeRemaining, setTimeRemaining] = useState(APP_CONFIG.ASSESSMENT_TIMER_SECONDS)
    const [userAnswer, setUserAnswer] = useState('')
    const [showExplanation, setShowExplanation] = useState(false)
    const [isCorrect, setIsCorrect] = useState<boolean | null>(null)

    useEffect(() => {
        if (structure) {
            const subject = structure.subjects.find(s => s.slug === subjectSlug)
            if (subject) {
                setSubjectName(subject.name)
                const topic = subject.topics.find(t => t.slug === topicSlug)
                if (topic) {
                    setTopicName(topic.name)
                    setMdPath(topic.md_path)
                    setQuestionPaths(topic.questions)
                }
            }
        }
    }, [structure, subjectSlug, topicSlug])

    // Timer countdown
    useEffect(() => {
        if (!isAssessmentActive || showExplanation) return

        const timer = setInterval(() => {
            setTimeRemaining((prev) => {
                if (prev <= 1) {
                    handleSubmit()
                    return 0
                }
                return prev - 1
            })
        }, 1000)

        return () => clearInterval(timer)
    }, [isAssessmentActive, showExplanation])

    const startAssessment = () => {
        setIsAssessmentActive(true)
        setCurrentQuestionIndex(0)
        setTimeRemaining(APP_CONFIG.ASSESSMENT_TIMER_SECONDS)
        setShowExplanation(false)
        setUserAnswer('')
    }

    const handleSubmit = async () => {
        if (!userAnswer.trim()) return

        const currentPath = questionPaths[currentQuestionIndex]
        if (!currentPath) return

        try {
            const dataPath = `/assets/${examId}/${streamId}/${currentPath}data.json` // Use examId here too? Actually structure uses /assets/gate, we should probably check if assets layout changed.
            // Wait, previous code: `/assets/gate/${streamId}/${currentPath}data.json`
            // If we are dynamic, we should use examId.
            // Assumption: The assets are at /assets/<examId>/<streamId>/...
            const response = await fetch(dataPath)
            if (!response.ok) throw new Error('Failed to fetch data')
            const data: QuestionData = await response.json()

            let correct = false
            const uAns = userAnswer.trim().toLowerCase()
            let cAnsRaw = data.answer_text.replace(/^Ans\.\s*/i, '')
            const splitMatch = cAnsRaw.split(/[\n\r]|Sol\.|Solution/i)
            if (splitMatch && splitMatch.length > 0) {
                cAnsRaw = splitMatch[0].trim()
            }
            cAnsRaw = cAnsRaw.trim()

            const optionMatch = cAnsRaw.match(/^[\(]?([A-Da-d])[\)\.](\s+|$)/)
            let cOption = ''
            let cText = cAnsRaw

            if (optionMatch) {
                cOption = optionMatch[1].toLowerCase()
                cText = cAnsRaw.substring(optionMatch[0].length).trim().toLowerCase()
            } else {
                cText = cAnsRaw.toLowerCase()
            }

            if (data.type === 'MSQ') {
                const splitRegex = /[, ]+/
                const uParts = uAns.split(splitRegex).filter(Boolean).sort().join(',')
                const possibleKey = data.key || cAnsRaw
                const cleanKey = possibleKey.split(/[\n\r]|Sol\.|Solution/i)[0].trim()
                const cParts = cleanKey.toLowerCase().split(splitRegex).filter(Boolean).sort().join(',')
                correct = uParts.length > 0 && cParts.length > 0 && uParts === cParts
            } else if (data.type === 'NAT') {
                const uNumStr = uAns.replace(/\s/g, '')
                const cNumStr = cAnsRaw.replace(/\s/g, '')
                correct = !isNaN(Number(uNumStr)) && !isNaN(Number(cNumStr)) ? Number(uNumStr) === Number(cNumStr) : uNumStr === cNumStr.toLowerCase()
            } else {
                correct = (cOption && uAns === cOption) || uAns === cText || uAns === cAnsRaw.toLowerCase()
            }

            setIsCorrect(correct)
            setShowExplanation(true)
        } catch (error) {
            console.error('Failed to load question data:', error)
        }
    }

    const nextQuestion = () => {
        if (currentQuestionIndex < questionPaths.length - 1) {
            setCurrentQuestionIndex(prev => prev + 1)
            setTimeRemaining(APP_CONFIG.ASSESSMENT_TIMER_SECONDS)
            setShowExplanation(false)
            setIsCorrect(null)
            setUserAnswer('')
        } else {
            setIsAssessmentActive(false)
            navigate({
                to: '/$examId/$streamId',
                params: { examId, streamId },
                search: { expanded: subjectSlug } as any
            })
        }
    }

    const formatTime = (seconds: number) => {
        const mins = Math.floor(seconds / 60)
        const secs = seconds % 60
        return `${mins}:${secs.toString().padStart(2, '0')}`
    }

    const getContributeUrl = () => {
        if (!mdPath || !APP_CONFIG.REPO_URL) return '#'
        return `${APP_CONFIG.REPO_URL}/blob/HEAD/frontend/public/assets/${examId}/${streamId}/${mdPath}`
    }

    if (structureLoading || theoryLoading) {
        return (
            <div className="min-h-screen flex justify-center items-center">
                <span className="loading loading-spinner loading-lg"></span>
            </div>
        )
    }

    const currentQuestionPath = questionPaths[currentQuestionIndex]

    return (
        <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 sm:py-12 min-h-screen">

            <div className="mb-8">
                <h1 className="text-3xl sm:text-4xl font-bold mb-2">{topicName}</h1>
                <p className="opacity-60">{subjectName}</p>
            </div>

            {!isAssessmentActive ? (
                <div className="space-y-8">
                    <div className="card bg-base-200 shadow-sm">
                        <div className="card-body">
                            <div className="card-title">
                                <BookOpen className="w-6 h-6" />
                                <h3 className="text-2xl font-bold">Theory</h3>
                            </div>
                            <a href={getContributeUrl()} target="_blank" rel="noopener noreferrer" className="btn btn-ghost btn-sm absolute top-4 right-4 gap-2">
                                <Github className="w-4 h-4" />
                                <span className="hidden sm:inline">Contribute</span>
                            </a>
                            {theory ? (
                                <div className="prose max-w-none">
                                    <Markdown
                                        source={theory}
                                        baseUrl={mdPath ? `/assets/${examId}/${streamId}/${mdPath.substring(0, mdPath.lastIndexOf('/') + 1)}` : undefined}
                                    />
                                </div>
                            ) : (
                                <p className="opacity-60">No theory content available yet.</p>
                            )}
                        </div>
                    </div>

                    <div className="card bg-base-200 shadow-sm">
                        <div className="card-body">
                            <h3 className="card-title text-2xl font-bold">Practice Questions</h3>
                            <p className="opacity-60">
                                {questionPaths.length} question{questionPaths.length !== 1 ? 's' : ''} available.
                                You'll have {Math.floor(APP_CONFIG.ASSESSMENT_TIMER_SECONDS / 60)} minutes per question.
                            </p>
                            <div className="card-actions">
                                <button onClick={startAssessment} disabled={questionPaths.length === 0} className="btn btn-primary">
                                    <Play className="w-5 h-5 mr-2" />
                                    Start Assessment
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            ) : (
                <div className="space-y-6">
                    <div className="card bg-base-200 shadow-sm">
                        <div className="card-body flex-row items-center justify-between">
                            <div className="flex items-center gap-3">
                                <Timer className="w-5 h-5 text-primary" />
                                <span className="countdown font-mono text-lg">
                                    <span style={{ "--value": Math.floor(timeRemaining / 60) } as React.CSSProperties}></span>:
                                    <span style={{ "--value": timeRemaining % 60 } as React.CSSProperties}></span>
                                </span>
                            </div>
                            <div className="opacity-60">
                                Question {currentQuestionIndex + 1} of {Math.min(questionPaths.length, 20)}
                            </div>
                        </div>
                    </div>

                    <div className="card bg-base-200 shadow-sm">
                        <div className="card-body">
                            <h3 className="card-title text-xl font-bold">Question</h3>
                            {currentQuestionPath && (
                                <figure className="bg-base-100 p-4 rounded-lg">
                                    <img src={`/assets/${examId}/${streamId}/${currentQuestionPath}q.webp`} alt="Question" />
                                </figure>
                            )}

                            {!showExplanation ? (
                                <div className="form-control gap-4">
                                    <input
                                        type="text"
                                        value={userAnswer}
                                        onChange={(e) => setUserAnswer(e.target.value)}
                                        placeholder="Enter your answer..."
                                        className="input input-bordered w-full"
                                        onKeyPress={(e) => e.key === 'Enter' && handleSubmit()}
                                    />
                                    <div className="card-actions mt-4">
                                        <button onClick={handleSubmit} disabled={!userAnswer.trim()} className="btn btn-primary">
                                            Submit
                                        </button>
                                    </div>
                                </div>
                            ) : (
                                <div className="space-y-4">
                                    <div role="alert" className={`alert ${isCorrect ? 'alert-success' : 'alert-error'}`}>
                                        {isCorrect ? <CheckCircle /> : <XCircle />}
                                        <span>{isCorrect ? 'Correct!' : 'Incorrect. Review the explanation below.'}</span>
                                    </div>

                                    {!isCorrect && currentQuestionPath && (
                                        <div>
                                            <h4 className="text-lg font-bold mb-2">Explanation</h4>
                                            <figure className="bg-base-100 p-4 rounded-lg">
                                                <img src={`/assets/${examId}/${streamId}/${currentQuestionPath}exp.webp`} alt="Explanation" />
                                            </figure>
                                        </div>
                                    )}
                                    <div className="card-actions">
                                        <button onClick={nextQuestion} className="btn btn-primary">
                                            {currentQuestionIndex < questionPaths.length - 1 ? 'Next Question' : 'Finish Assessment'}
                                            <ArrowRight className="w-5 h-5 ml-2" />
                                        </button>
                                    </div>
                                </div>
                            )}
                        </div>
                    </div>
                </div>
            )}
        </main>
    )
}
