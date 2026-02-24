"use client"

import mermaid from "mermaid"
import { useEffect } from "react"
import ReactMarkdown from "react-markdown"
import rehypeKatex from "rehype-katex"
import rehypeRaw from "rehype-raw"
import remarkGfm from "remark-gfm"
import remarkMath from "remark-math"
import "katex/dist/katex.min.css"
import type { ComponentProps } from "react"

export function Code({
  className,
  children,
  ...props
}: ComponentProps<"code">) {
  const lang = className?.replace("language-", "")

  useEffect(() => {
    if (lang === "mermaid") {
      mermaid.initialize({ startOnLoad: true, theme: "default" })
      mermaid.run()
    }
  }, [lang])

  if (lang === "mermaid") {
    return <div className="mermaid justify-self-center">{String(children)}</div>
  }

  // fallback: let ReactMarkdown handle normal code blocks
  return (
    <code className={className} {...props}>
      {children}
    </code>
  )
}

const Img = ({ src, alt, baseUrl, ...props }: React.ImgHTMLAttributes<HTMLImageElement> & { baseUrl?: string }) => {
  let resolvedSrc = src
  if (src && !src.startsWith('http') && !src.startsWith('/') && baseUrl) {
    // Basic relative path resolution
    try {
      // Use URL constructor with a dummy base to resolve relative paths
      // baseUrl should end with /
      const dummyBase = 'http://dummy.com' + (baseUrl.endsWith('/') ? baseUrl : baseUrl + '/')
      const url = new URL(src, dummyBase)
      resolvedSrc = url.pathname
    } catch (e) {
      console.error('Failed to resolve relative path:', src, e)
    }
  }
  return <img src={resolvedSrc} alt={alt} {...props} />
}

export default function Markdown({ source, baseUrl }: { source: string; baseUrl?: string }) {
  return (
    <ReactMarkdown
      remarkPlugins={[remarkGfm, remarkMath]}
      rehypePlugins={[rehypeKatex, rehypeRaw]}
      components={{
        code: Code,
        img: (props) => <Img {...props} baseUrl={baseUrl} />
      }}
    >
      {source}
    </ReactMarkdown>
  )
}