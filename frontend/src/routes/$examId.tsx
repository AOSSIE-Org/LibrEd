import { createFileRoute, Outlet } from '@tanstack/react-router'

export const Route = createFileRoute('/$examId')({ component: ExamLayout })

function ExamLayout() {
    return (
        <div className="min-h-screen bg-base-100 text-base-content transition-colors duration-200">
            {/* This outlet will render child routes */}
            <Outlet />
        </div>
    )
}
