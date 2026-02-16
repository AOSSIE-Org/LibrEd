import { Link } from '@tanstack/react-router'
import { Brain } from 'lucide-react'
import { APP_CONFIG } from '../config'
import { ThemeToggle } from './ThemeToggle'

export function Header() {
    return (
        <div className="navbar bg-base-100">
            <div className="navbar-start">
                <Link to="/" className="btn btn-ghost text-xl">
                    <Brain />
                    {APP_CONFIG.SITE_NAME}
                </Link>
            </div>
            <div className="navbar-end">
                <ThemeToggle />
            </div>
        </div>
    )
}
