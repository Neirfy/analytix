import { useState } from 'react';

type User = {
  id: number;
  name: string;
  email: string;
  role: 'admin' | 'user';
  status: 'active' | 'blocked';
  createdAt: string;
};

const mockUsers: User[] = [
  {
    id: 1,
    name: 'Anton',
    email: 'anton@mail.com',
    role: 'admin',
    status: 'active',
    createdAt: '2026-04-01',
  },
  {
    id: 2,
    name: 'John',
    email: 'john@mail.com',
    role: 'user',
    status: 'active',
    createdAt: '2026-04-02',
  },
  {
    id: 3,
    name: 'Kate',
    email: 'kate@mail.com',
    role: 'user',
    status: 'blocked',
    createdAt: '2026-04-03',
  },
];

export const UsersPage = () => {
  const [search, setSearch] = useState('');

  const filteredUsers = mockUsers.filter((u) =>
    u.name.toLowerCase().includes(search.toLowerCase())
  );

  // const total = mockUsers.length;
  // const active = mockUsers.filter((u) => u.status === 'active').length;
  // const admins = mockUsers.filter((u) => u.role === 'admin').length;

  return (
    <div className="">
      {/* Заголовок */}
      <h1 className="text-2xl font-bold">Users</h1>

      {/* Поиск */}
      <div className="bg-white dark:bg-gray-800 p-4 rounded-2xl shadow flex gap-4">
        <input
          type="text"
          placeholder="Search user..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="w-full border rounded-xl p-2 dark:bg-gray-900"
        />

        <button className="bg-blue-600 text-white px-4 rounded-xl hover:bg-blue-700">
          Add User
        </button>
      </div>

      {/* Метрики */}
      {/* <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="p-4 rounded-2xl shadow bg-white dark:bg-gray-800">
          <p className="text-sm text-gray-500">Total Users</p>
          <p className="text-xl font-bold">{total}</p>
        </div>

        <div className="p-4 rounded-2xl shadow bg-white dark:bg-gray-800">
          <p className="text-sm text-gray-500">Active</p>
          <p className="text-xl font-bold">{active}</p>
        </div>

        <div className="p-4 rounded-2xl shadow bg-white dark:bg-gray-800">
          <p className="text-sm text-gray-500">Admins</p>
          <p className="text-xl font-bold">{admins}</p>
        </div>
      </div> */}

      {/* Таблица */}
      <div className="mt-2 p-4 rounded-2xl shadow bg-white dark:bg-gray-800 overflow-x-auto">
        <table className="w-full text-left">
          <thead>
            <tr className="text-gray-500 text-sm border-b">
              <th className="p-2">Name</th>
              <th className="p-2">Email</th>
              <th className="p-2">Role</th>
              <th className="p-2">Status</th>
              <th className="p-2">Created</th>
              <th className="p-2 text-right">Actions</th>
            </tr>
          </thead>

          <tbody>
            {filteredUsers.map((u) => (
              <tr key={u.id} className="border-b last:border-none">
                <td className="p-2">{u.name}</td>
                <td className="p-2">{u.email}</td>

                <td className="p-2">
                  <span
                    className={`p-2 p-1 rounded-lg text-xs ${
                      u.role === 'admin'
                        ? 'bg-purple-100 text-purple-700'
                        : 'bg-gray-100 text-gray-700'
                    }`}
                  >
                    {u.role}
                  </span>
                </td>

                <td className="p-2">
                  <span
                    className={`p-2 p-1 rounded-lg text-xs ${
                      u.status === 'active'
                        ? 'bg-green-100 text-green-700'
                        : 'bg-red-100 text-red-700'
                    }`}
                  >
                    {u.status}
                  </span>
                </td>

                <td className="p-2">{u.createdAt}</td>

                <td className="p-2 text-right">
                  <button className="text-blue-600 hover:underline mr-3">
                    Edit/
                  </button>
                  <button className="text-red-600 hover:underline">
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};