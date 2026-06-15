import { FiMenu } from 'react-icons/fi';

export const SidebarHeader = ({
  collapsed,
  toggle,
}: {
  collapsed: boolean;
  toggle: () => void;
}) => (
  <div
    className={`flex items-center px-4 border-b border-gray-700 dark:border-gray-200 ${
      collapsed ? 'justify-center' : 'justify-between'
    } h-16`}
  >
    {!collapsed && <span className="text-xl font-bold">Analytics</span>}
    <button onClick={toggle}>
      <FiMenu size={24} />
    </button>
  </div>
);