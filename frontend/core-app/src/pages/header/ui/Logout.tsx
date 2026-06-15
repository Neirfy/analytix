interface ConfirmModalProps {
  open: boolean
  title?: string
  onCancel: () => void
  onConfirm: () => void
}

export const LogoutModal = ({
  open,
  title = 'Подтвердить действие?',
  onCancel,
  onConfirm
}: ConfirmModalProps) => {
  if (!open) return null

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center bg-black/50"
      onClick={onCancel}
    >
      <div
        className="w-80 rounded bg-white dark:bg-gray-800 p-6 shadow-lg"
        onClick={(e) => e.stopPropagation()}
      >
        <h2 className="mb-4 text-lg font-semibold">{title}</h2>

        <div className="flex justify-end gap-3">
          <button
            onClick={onCancel}
            className="px-4 py-2 rounded bg-gray-300 hover:bg-gray-400"
          >
            Отмена
          </button>

          <button
            onClick={onConfirm}
            className="px-4 py-2 rounded bg-red-500 text-white hover:bg-red-600"
          >
            Подтвердить
          </button>
        </div>
      </div>
    </div>
  )
}