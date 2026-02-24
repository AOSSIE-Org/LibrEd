import { Link, useParams } from '@tanstack/react-router'
import { useStreamStructure } from '../hooks/useData'
import { BookOpen, ArrowRight } from 'lucide-react'
import { useState, useEffect } from 'react'

export function StreamDashboard() {
    const { examId, streamId } = useParams({ from: '/$examId/$streamId/' })
    const { data: structure, loading, error } = useStreamStructure(examId, streamId)
    const search = typeof window !== 'undefined' ? window.location.search : ''
    const params = new URLSearchParams(search)
    const expandedSlug = params.get('expanded')

    const [openSubjects, setOpenSubjects] = useState<Set<string>>(new Set())

    useEffect(() => {
        if (structure) {
            if (expandedSlug) {
                setOpenSubjects(prev => new Set(prev).add(expandedSlug))
            } else {
                // Default: collapse all subjects
                setOpenSubjects(new Set())
            }
        }
    }, [expandedSlug, structure])

    const toggleSubject = (subjectSlug: string) => {
        const newOpen = new Set(openSubjects)
        if (newOpen.has(subjectSlug)) {
            newOpen.delete(subjectSlug)
        } else {
            newOpen.add(subjectSlug)
        }
        setOpenSubjects(newOpen)
    }

    if (loading) {
        return (
            <div className="min-h-screen flex flex-col justify-center items-center">
                <span className="loading loading-spinner loading-lg"></span>
            </div>
        )
    }

    if (error || !structure) {
        return (
            <div className="min-h-screen flex flex-col justify-center items-center p-4">
                <div role="alert" className="alert alert-error max-w-lg">
                    <svg xmlns="http://www.w3.org/2000/svg" className="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                    <div>
                        <h3 className="font-bold">Error Loading Stream</h3>
                        <div className="text-xs">{error?.message || 'Stream structure not found'}</div>
                    </div>
                    <Link to="/" className="btn btn-sm btn-outline">
                        Return Home
                    </Link>
                </div>
            </div>
        )
    }

    const sortedSubjects = [...structure.subjects].sort((a, b) =>
        a.name.localeCompare(b.name)
    )

    return (
        <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 sm:py-12 min-h-screen">
            <div className="mb-8">
                <h1 className="text-4xl sm:text-5xl font-black mb-2">
                    {structure.name}
                </h1>
                <p className="text-lg opacity-70">
                    Select a subject to start practicing
                </p>
            </div>

            <div className="space-y-4">
                {sortedSubjects.map((subject) => {
                    const totalQuestions = subject.topics.reduce((acc, topic) => acc + topic.questions.length, 0)

                    return (
                        <div key={subject.slug} className="collapse collapse-arrow bg-base-200">
                            <input
                                type="checkbox"
                                checked={openSubjects.has(subject.slug)}
                                onChange={() => toggleSubject(subject.slug)}
                            />
                            <div className="collapse-title text-xl font-medium">
                                <div className="flex items-center gap-4">
                                    <BookOpen className="w-6 h-6" />
                                    <div>
                                        {subject.name}
                                        <div className="text-sm font-normal opacity-60">
                                            {subject.topics.length} Topics - {totalQuestions} Questions
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div className="collapse-content">
                                <div className="p-4 bg-base-100 rounded-box mt-2">
                                    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
                                        {subject.topics.map((topic) => (
                                            <Link
                                                key={topic.slug}
                                                to="/$examId/$streamId/$subjectSlug/$topicSlug"
                                                params={{
                                                    examId: examId,
                                                    streamId: streamId,
                                                    subjectSlug: subject.slug,
                                                    topicSlug: topic.slug
                                                }}
                                                className="btn btn-ghost justify-between h-auto py-2"
                                            >
                                                <div className="text-left">
                                                    <div className="font-medium">
                                                        {topic.name}
                                                    </div>
                                                    <div className="text-xs opacity-50 font-normal">
                                                        {topic.questions.length} questions
                                                    </div>
                                                </div>
                                                <ArrowRight className="w-4 h-4" />
                                            </Link>
                                        ))}
                                    </div>
                                </div>
                            </div>
                        </div>
                    )
                })}
            </div>
        </main>
    )
}
