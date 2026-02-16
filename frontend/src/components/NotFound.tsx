import { Link } from '@tanstack/react-router'
import { Home, AlertTriangle } from 'lucide-react'

export function NotFound() {
    return (
        <div className="hero min-h-screen bg-base-200">
            <div className="hero-content text-center">
                <div className="max-w-md">
                    <AlertTriangle className="w-24 h-24 mx-auto text-warning mb-6" />
                    <h1 className="text-5xl font-bold">404</h1>
                    <p className="py-6 text-xl opacity-80">
                        Sorry, we couldn't find the page you're looking for.
                    </p>
                    <Link to="/" className="btn btn-primary gap-2">
                        <Home className="w-5 h-5" />
                        Back to Home
                    </Link>
                </div>
            </div>
        </div>
    )
}
