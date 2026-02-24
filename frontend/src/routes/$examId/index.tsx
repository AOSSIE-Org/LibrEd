import { createFileRoute, Link, useParams } from '@tanstack/react-router'
import { useAvailableStreams } from '../../hooks/useData'
import { Layers } from 'lucide-react'

export const Route = createFileRoute('/$examId/')({ component: ExamIndex })

function ExamIndex() {
  const { examId } = useParams({ from: '/$examId/' })
  const { streams, loading } = useAvailableStreams(examId)

  return (
    <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 sm:py-12 min-h-screen">

      <div className="text-center mb-12">
        <h1 className="text-4xl sm:text-5xl font-bold mb-4">Select a Stream</h1>
        <p className="text-lg opacity-70 max-w-2xl mx-auto">
          Choose your stream to start practicing for {examId.toUpperCase()}.
        </p>
      </div>

      {loading ? (
        <div className="text-center py-20">
          <span className="loading loading-spinner loading-lg"></span>
        </div>
      ) : streams.length === 0 ? (
        <div className="hero bg-base-200 rounded-box p-8">
          <div className="hero-content text-center">
            <div className="max-w-md">
              <Layers className="w-16 h-16 mx-auto mb-4 opacity-30" />
              <h2 className="text-2xl font-bold">No Streams Available</h2>
              <p className="py-4">It looks like no content has been generated for this app yet. Please run the generator script.</p>
            </div>
          </div>
        </div>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {streams.map((stream) => (
            <Link
              key={stream.id}
              to={`/${examId}/${stream.id}`}
              className="card bg-base-200 shadow-lg hover:shadow-xl hover:-translate-y-1 transition-all duration-300"
            >
              <div className="card-body">
                <div className="flex items-center gap-4">
                  <div className="p-4 bg-primary/10 rounded-box">
                    <Layers className="w-8 h-8 text-primary" />
                  </div>
                  <div>
                    <h2 className="card-title font-extrabold text-2xl">{stream.id.toUpperCase()}</h2>
                    <p className="opacity-70">{stream.name}</p>
                  </div>
                </div>
              </div>
            </Link>
          ))}
        </div>
      )}
    </main>
  )
}
