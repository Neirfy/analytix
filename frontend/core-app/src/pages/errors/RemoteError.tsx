import React from "react"

type Props = {
  name: string
  fallback?: React.ReactNode
  children?: React.ReactNode
}

type State = {
  hasError: boolean
}

export default class RemoteError extends React.Component<Props, State> {
  constructor(props: Props) {
    super(props)
    this.state = { hasError: false }
  }

  static getDerivedStateFromError(): State {
    return { hasError: true }
  }

  render() {
    if (this.state.hasError) {
      return (
        this.props.fallback || (
          <div style={styles.box}>
            ⚠️ Microfrontend "{this.props.name}" недоступен
          </div>
        )
      )
    }

    return this.props.children
  }
}

const styles: Record<string, React.CSSProperties> = {
  box: {
    padding: 20,
    color: "#fff",
    background: "#ef4444",
    borderRadius: 8,
    margin: 10,
  },
}