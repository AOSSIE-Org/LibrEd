import { createFileRoute } from '@tanstack/react-router'
import { StreamDashboard } from '../../../components/StreamDashboard'

export const Route = createFileRoute('/$examId/$streamId/')({
  component: StreamDashboard
})
