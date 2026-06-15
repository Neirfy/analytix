import type { JSX } from 'react';
import { FiPieChart, FiBarChart2, FiUsers, FiMessageCircle, FiCalendar } from 'react-icons/fi';

export interface SubMenuItem {
  label: string;
  path: string;
}

export interface MenuItem {
  label: string;
  icon: JSX.Element;
  path?: string;
  subMenu?: SubMenuItem[];
}

export const menuItems: MenuItem[] = [
  { label: 'Dashboard', icon: <FiPieChart />, path: '/dashboard' },
  {
    label: 'Reports',
    icon: <FiBarChart2 />,
    subMenu: [
      { label: 'Sales', path: '/reports/sales' },
      { label: 'Revenue', path: '/reports/revenue' },
      { label: 'Expenses', path: '/reports/expenses' },
    ],
  },
  { label: 'Chat', icon: <FiMessageCircle />, path: '/chat' },
  { label: 'Calendar', icon: <FiCalendar />, path: '/calendar' },
  { label: 'Users', icon: <FiUsers />, path: '/users' },
];