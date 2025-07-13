'use client'
import { useState } from 'react'

export default function UploadForm() {
  const [prompt, setPrompt] = useState('')
  const [loading, setLoading] = useState(false)
  const [resultUrl, setResultUrl] = useState(null)

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!prompt.trim()) return alert('Please enter a prompt.')

    setLoading(true)
    setResultUrl(null)

    try {
      const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/runpod-generate`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({prompt})
      })
      
      if (!res.ok) throw new Error('Failed to generate image')

      const data = await res.json()

      // Show result (output image)
      setResultUrl(data.file_url || data.file)
    } catch (err) {
      console.error('Error:', err)
      alert('Something went wrong')
    } finally {
      setLoading(false)
    }
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4 max-w-md mx-auto p-4 border rounded-xl shadow">
      <h2 className="text-xl font-semibold">Generate AI Image</h2>

      <input
        type="text"
        placeholder="Descibe your image..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        className="block w-full border rounded p-2"
      />

      <button
        type="submit"
        className="w-full bg-blue-600 text-white p-2 rounded disabled:opacity-50"
        disabled={loading}
      >
        {loading ? 'Generating...' : 'Generate'}
      </button>

      {loading && <p className='text-center text-gray-500'>Please wait, generating image...</p>}

      {resultUrl && (
        <div className="mt-6">
          <h3 className="text-lg font-medium mb-2">Result</h3>
          <img src={resultUrl} alt="Generated" className="rounded shadow" />
        </div>
      )}
    </form>
  )
}
