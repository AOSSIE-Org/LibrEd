import { createFileRoute, Outlet } from '@tanstack/react-router'
// import { StreamDashboard } from '../../components/StreamDashboard' // Removing unused import

export const Route = createFileRoute('/$examId/$streamId')({
    component: DashboardRoute
})

function DashboardRoute() {
    return (
        <>
            <Outlet />
        </>
    )
}
