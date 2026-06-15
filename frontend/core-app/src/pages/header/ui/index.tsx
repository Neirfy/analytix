import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import {
  FiUser,
  FiSearch,
  FiSun,
  FiSettings,
  FiMoon,
  FiLogOut
} from 'react-icons/fi'
import { LogoutModal } from './Logout'

interface HeaderProps {
  darkMode: boolean
  toggleTheme: () => void
}

export const Header = ({ darkMode, toggleTheme }: HeaderProps) => {
  const [search, setSearch] = useState('')
  const [menuOpen, setMenuOpen] = useState(false)
  const [confirmOpen, setConfirmOpen] = useState(false)

  const navigate = useNavigate()

  const handleMenuClick = (label: string) => {
    if (label === 'Logout') {
      setConfirmOpen(true)
      // setMenuOpen(false)

      // return
    }

    if (label === 'Profile') {
      navigate('/profile')
    }

    setMenuOpen(false)
  }

  const handleLogout = () => {
    setConfirmOpen(false)
    setMenuOpen(false)

    console.log('logout')
  }

  const menuItems = [
    { label: 'Profile', icon: <FiSettings /> },
    { label: 'Logout', icon: <FiLogOut /> }
  ]

  return (
    <>
      <header className="flex items-center justify-between bg-gray-200 dark:bg-gray-900 p-5 h-16 border-b border-gray-700 dark:border-gray-200">
        {/* Поиск */}
        <div className="flex items-center relative w-1/3">
          <FiSearch className="absolute left-3 dark:text-gray-400" />
          <input
            type="text"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder="Search..."
            className="w-full pl-10 pr-3 py-2 rounded bg-gray-100 dark:bg-gray-800 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-gray-500"
          />
        </div>

        {/* Правая часть */}
        <div className="relative flex items-center gap-4">
          <button
            onClick={toggleTheme}
            className="p-2 rounded hover:bg-gray-300 dark:hover:bg-gray-700"
          >
            {darkMode ? <FiSun size={20} /> : <FiMoon size={20} />}
          </button>

          <button
            onClick={() => setMenuOpen((prev) => !prev)}
            className="flex items-center gap-2 p-2 rounded hover:bg-gray-300 dark:hover:bg-gray-700"
          >
            <FiUser size={20} />
            <span>User</span>
          </button>

          {menuOpen && (
            <ul className="absolute top-10 right-0 mt-2 w-40 bg-gray-500 rounded shadow-lg z-50">
              {menuItems.map((item) => (
                <li
                  key={item.label}
                  onClick={() => handleMenuClick(item.label)}
                  className="px-4 py-2 m-2 rounded cursor-pointer hover:bg-gray-300 dark:hover:bg-gray-700"
                >
                  <div className="flex items-center gap-2">
                    {item.icon}
                    <span>{item.label}</span>
                  </div>
                </li>
              ))}
            </ul>
          )}
        </div>
      </header>

      <LogoutModal
        open={confirmOpen}
        title="Выйти из аккаунта?"
        onCancel={() => setConfirmOpen(false)}
        onConfirm={handleLogout}
      />
    </>
  )
}