export default function NotFound() {
  return (
    <div className="flex h-screen items-center justify-center bg-gray-100 dark:bg-gray-900">
      <div className="text-center">
        <h1 className="text-6xl font-bold text-gray-800 dark:text-white">
          404
        </h1>

        <p className="mt-4 text-gray-600 dark:text-gray-300">
          Страница не найдена
        </p>

        <a
          href="/"
          className="mt-6 inline-block rounded bg-blue-600 px-4 py-2 text-white hover:bg-blue-700 transition"
        >
          На главную
        </a>
      </div>
    </div>
  );
}