import { useEffect, useState } from 'react'
import { Moon, Sun } from 'lucide-react'
import { APP_CONFIG, THEMES } from '../config'

export function ThemeToggle() {
    const [theme, setTheme] = useState(() => {
        if (typeof window !== 'undefined') {
            return localStorage.getItem(APP_CONFIG.THEME_STORAGE_KEY) || THEMES.DEFAULT || THEMES.DARK
        }
        return THEMES.DARK
    })

    useEffect(() => {
        const savedTheme = localStorage.getItem(APP_CONFIG.THEME_STORAGE_KEY) || THEMES.DEFAULT || THEMES.DARK
        setTheme(savedTheme)
        document.documentElement.setAttribute('data-theme', savedTheme)
    }, [])

    const toggleTheme = () => {
        const newTheme = theme === THEMES.LIGHT ? THEMES.DARK : THEMES.LIGHT
        setTheme(newTheme)
        document.documentElement.setAttribute('data-theme', newTheme)
        localStorage.setItem(APP_CONFIG.THEME_STORAGE_KEY, newTheme)
    }

    return (
        <button
            onClick={toggleTheme}
            className="btn btn-ghost btn-circle"
            aria-label="Toggle theme"
        >
            {theme === THEMES.LIGHT ? (
                <Sun className="w-5 h-5 text-yellow-500" />
            ) : (
                <Moon className="w-5 h-5 text-cyan-400" />
            )}
        </button>
    )
}
