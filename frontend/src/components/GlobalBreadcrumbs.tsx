import { useLocation } from '@tanstack/react-router'
import { Breadcrumb } from './Breadcrumb'

export function GlobalBreadcrumbs() {
    const { pathname } = useLocation()

    // Generate breadcrumbs from path
    // e.g. /gate/cs -> items: [{label: 'GATE', href: '/gate'}, {label: 'CS'}]
    const segments = pathname.split('/').filter(Boolean)
    const breadcrumbItems = segments.map((segment, index) => {
        let href: string | undefined = '/' + segments.slice(0, index + 1).join('/')
        let label = segment.replace(/-/g, ' ')

        // title case or special handling
        // Capitalize short segments (likely acronyms like GATE, CSE)
        if (segment.length <= 4) {
            label = segment.toUpperCase()
        } else {
            label = label.charAt(0).toUpperCase() + label.slice(1)
        }

        // If we are at the subject level in a topic path (/gate/stream/subject/topic),
        // we want to link back to the stream dashboard with the subject expanded.
        if (segments.length === 4 && index === 2) {
            const examId = segments[0]
            const stream = segments[1]
            href = `/${examId}/${stream}?expanded=${segment}`
        }

        const isLast = index === segments.length - 1
        return { label, href: isLast ? undefined : href }
    })

    if (breadcrumbItems.length === 0) return null

    return (
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-4">
            <Breadcrumb items={breadcrumbItems} />
        </div>
    )
}
