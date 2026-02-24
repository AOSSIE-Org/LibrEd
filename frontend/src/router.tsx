import { createRouter } from '@tanstack/react-router'
import { NotFound } from './components/NotFound'

// Import the generated route tree
import { routeTree } from './routeTree.gen'

// Create a new router instance
export const getRouter = () => {
  const router = createRouter({
    routeTree,
    context: {},
    defaultNotFoundComponent: NotFound,

    scrollRestoration: true,
    defaultPreloadStaleTime: 0,
  })

  return router
}
