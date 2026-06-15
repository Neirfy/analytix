export async function isRemoteAlive(url: string) {
  try {
    await fetch(url, { method: "HEAD" })
    return true
  } catch {
    return false
  }
}