import type { MenuItem, SubMenuItem } from './menuConfig';
import { FiChevronDown } from 'react-icons/fi';

export const SidebarItem = ({
  item,
  collapsed,
  isOpen,
  toggleSubMenu,
  navigate,
  locationPath,
}: {
  item: MenuItem;
  collapsed: boolean;
  isOpen: boolean;
  toggleSubMenu: (label: string, hasSubMenu: boolean) => void;
  navigate: (path: string) => void;
  locationPath: string;
}) => {
  const isActive =
    item.path === locationPath ||
    item.subMenu?.some((sub) => sub.path === locationPath);

  const iconSize = collapsed ? 24 : 20;

  return (
    <li className="relative p-2">
      <div
        onClick={() => {
            toggleSubMenu(item.label, !!item.subMenu);
            if (!item.subMenu && item.path) navigate(item.path);
        }}

        className={`flex items-center justify-between p-3 cursor-pointer hover:bg-gray-400 dark:hover:bg-gray-700 transition-colors ${
          isActive ? 'bg-gray-300 dark:bg-gray-800 font-semibold' : ''
        } rounded`}
      >
        <div className={`flex items-center ${collapsed ? 'justify-center w-full' : 'gap-4'}`}>
          {item.icon && <item.icon.type size={iconSize} />}
          {!collapsed && <span>{item.label}</span>}
        </div>
        {!collapsed && item.subMenu && (
          <FiChevronDown className={`transition-transform duration-200 ${isOpen ? 'rotate-180' : ''}`} />
        )}
      </div>

      {/* Submenu */}
      {item.subMenu && isOpen && (
        <ul
          className={`${
            collapsed
              ? 'absolute left-full top-0 ml-2 bg-gray-100 dark:bg-gray-900 p-2 rounded shadow-lg w-48 z-50'
              : 'ml-12 mt-1'
          }`}
        >
          {item.subMenu.map((sub: SubMenuItem) => (
            <li
              key={sub.label}
              onClick={
                () => {
                  navigate(sub.path);
                  toggleSubMenu(item.label, true);
                } 
              }
              className={`p-2 mt-2 mb-2 cursor-pointer hover:bg-gray-400 dark:hover:bg-gray-700 rounded ${
                locationPath === sub.path ? 'bg-gray-300 dark:bg-gray-800 font-semibold ' : ''
              }`}
            //   className={`p-2 cursor-pointer rounded
            // ${locationPath === sub.path
            //   ? 'bg-gray-300 dark:bg-gray-800 font-semibold '
            //   : 'hover:bg-gray-200 dark:hover:bg-gray-700'}`}
            >
              {sub.label}
            </li>
          ))}
        </ul>
      )}
    </li>
  );
};
