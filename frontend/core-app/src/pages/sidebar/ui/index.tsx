import { useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { menuItems } from './menuConfig';
import { SidebarHeader } from './Header';
import { SidebarItem } from './Item';


export const Sidebar = () => {
  const [collapsed, setCollapsed] = useState(false);
  const [openSubMenu, setOpenSubMenu] = useState<string | null>(null);

  const navigate = useNavigate();
  const location = useLocation();

  const toggleSubMenu = (label: string| null, hasSubMenu: boolean) => {
    if (hasSubMenu) {
      setOpenSubMenu(openSubMenu === label ? null : label);
    } else {
      setOpenSubMenu(null);
    }
  };

  return (
    <div
      className={`h-screen transition-all border-r border-l duration-300 bg-gray-200 dark:bg-gray-900 ${
        collapsed ? 'w-20' : 'w-64'
      }`}
    >
      <SidebarHeader collapsed={collapsed} toggle={() => setCollapsed(!collapsed)} />

      <ul className="mt-4">
        {menuItems.map((item) => (
          <SidebarItem
            key={item.label}
            item={item}
            collapsed={collapsed}
            isOpen={openSubMenu === item.label}
            toggleSubMenu={toggleSubMenu}
            navigate={navigate}
            locationPath={location.pathname}
          />
        ))}
      </ul>
    </div>
  );
};