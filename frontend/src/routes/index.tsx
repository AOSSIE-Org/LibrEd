import { createFileRoute, Link } from '@tanstack/react-router'
import { BookOpen, Brain, Target } from 'lucide-react'
import { APP_CONFIG } from '../config'
import { useAvailableExams } from '../hooks/useData'

export const Route = createFileRoute('/')({ component: Home })

function Home() {
  const { exams, loading } = useAvailableExams()

  return (
    <div className="min-h-screen bg-base-100">
      {/* Main Content */}
      <main className="container mx-auto px-4 py-8">

        {/* Hero */}
        <div className="hero py-10">
          <div className="hero-content text-center">
            <div className="max-w-2xl">
              <h1 className="text-5xl font-black mb-6">
                Master Your{' '}
                <span className="text-primary">
                  Exams
                </span>
              </h1>
              <p className="text-xl opacity-70 mb-8">
                {APP_CONFIG.SITE_DESCRIPTION}
              </p>
            </div>
          </div>
        </div>

        {/* Exam Selection */}
        <section className="mb-16">
          <h3 className="text-2xl font-bold mb-8 text-center">
            Select Your Exam
          </h3>
          {loading ? (
            <div className="text-center py-10">
              <span className="loading loading-spinner loading-lg"></span>
            </div>
          ) : exams.length === 0 ? (
            <div className="text-center py-10 opacity-70">
              No exams found. Please run the generator.
            </div>
          ) : (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 max-w-4xl mx-auto">
              {exams.map((exam) => (
                <Link
                  key={exam.id}
                  to={`/${exam.id}`}
                  className="card bg-base-200 shadow-xl hover:bg-base-300 transition-colors">
                  <div className="card-body items-center text-center">
                    <div className="p-4 bg-primary/10 rounded-xl mb-2 text-primary">
                      <Target size={32} />
                    </div>
                    <h2 className="card-title">{exam.name}</h2>
                    <p className="opacity-70 text-sm">
                      {exam.description}
                    </p>
                  </div>
                </Link>
              ))}
            </div>
          )}
        </section>

        {/* Features */}
        <section className="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-6xl mx-auto">
          {[
            {
              icon: <BookOpen className="w-8 h-8 text-primary" />,
              title: 'Comprehensive Theory',
              description: 'In-depth explanations for every topic with diagrams and examples',
            },
            {
              icon: <Target className="w-8 h-8 text-primary" />,
              title: 'PYQ Practice',
              description: 'Thousands of previous year questions organized by topics',
            },
            {
              icon: <Brain className="w-8 h-8 text-primary" />,
              title: 'Smart Learning',
              description: 'Structured learning path with prerequisite tracking',
            },
          ].map((feature, i) => (
            <div key={i} className="card bg-base-200 shadow-lg">
              <div className="card-body items-center text-center">
                <div className="mb-2">{feature.icon}</div>
                <h3 className="card-title">{feature.title}</h3>
                <p className="text-sm opacity-70">{feature.description}</p>
              </div>
            </div>
          ))}
        </section>
      </main>

      {/* Footer */}
      <footer className="footer footer-center p-10 bg-base-200 text-base-content rounded">
        <div>
          <p>
            &copy; {new Date().getFullYear()} {APP_CONFIG.SITE_NAME}. Open source under <a href={APP_CONFIG.REPO_URL} target="_blank" rel="noopener noreferrer" className="link link-hover">Apache 2.0 License</a>.
          </p>
        </div>
      </footer>
    </div>
  )
}
