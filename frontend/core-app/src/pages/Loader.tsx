export default function Loader() {
  return (
    <div className="h-screen w-full flex flex-col items-center justify-center bg-white text-slate-900 dark:bg-slate-900 dark:text-white">
      <div className="w-12 h-12 rounded-full border-4 border-slate-300 dark:border-slate-700 border-t-blue-500 animate-spin" />

      <div className="mt-3 text-sm opacity-70">
        Loading...
      </div>
    </div>
  )
}