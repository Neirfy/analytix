import { useState, useEffect } from 'react';

import { Sidebar } from './../../pages/sidebar/ui';
import { Header } from './../../pages/header/ui';
import { Outlet } from "react-router-dom";
export default function Layout() {
  const [darkMode, setDarkMode] = useState(false);

  useEffect(() => {
    document.documentElement.classList.toggle('dark', darkMode);
      console.log('Текущая тема:', darkMode ? 'Тёмная' : 'Светлая');

  }, [darkMode]);
  const toggleTheme = () => setDarkMode(prev => !prev);

  return (

    <div className="flex h-screen transition-colors duration-300
                bg-gray-100 text-black
                dark:bg-gray-900 dark:text-white">
        <Sidebar />

      <div className="flex flex-col flex-1">
        <Header darkMode={darkMode} toggleTheme={toggleTheme} />

        <main className="flex-1 p-6 overflow-auto dark:bg-gray-700">
          <Outlet />
        </main>
      </div>
    </div>
  );
}