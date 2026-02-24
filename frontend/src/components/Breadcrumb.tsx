import { Link } from '@tanstack/react-router'
import { Home } from 'lucide-react'

interface BreadcrumbItem {
    label: string
    href?: string
}

interface BreadcrumbProps {
    items: BreadcrumbItem[]
}

export function Breadcrumb({ items }: BreadcrumbProps) {
    return (
        <div className="text-sm breadcrumbs">
            <ul>
                <li>
                    <Link to="/" className="opacity-80 hover:opacity-100">
                        <Home className="w-4 h-4 mr-2" />
                        Home
                    </Link>
                </li>
                {items.map((item, index) => (
                    <li key={index}>
                        {item.href ? (
                            <Link to={item.href} className="opacity-80 hover:opacity-100">
                                {item.label}
                            </Link>
                        ) : (
                            <span>{item.label}</span>
                        )}
                    </li>
                ))}
            </ul>
        </div>
    )
}
