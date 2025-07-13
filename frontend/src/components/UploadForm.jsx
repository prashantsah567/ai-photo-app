'use client'
import { useState } from 'react'

export default function UploadForm() {
  const [image, setImage] = useState(null)
  const [previewUrl, setPreviewUrl] = useState(null)
  const [prompt, setPrompt] = useState('')
  const [loading, setLoading] = useState(false)
  const [resultUrl, setResultUrl] = useState(null)

  const handleImageChange = (e) => {
    const file = e.target.files[0]
    setImage(file)
    setPreviewUrl(URL.createObjectURL(file))
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!image || !prompt) return alert('Please select an image and enter a prompt.')

    setLoading(true)
    const formData = new FormData()
    formData.append('image', image)
    formData.append('prompt', prompt)

    console.log("Constructed URL ==========", `${process.env.NEXT_PUBLIC_API_URL}/api/process`)

    try {
      const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/process`, {
        method: 'POST',
        body: formData,
      })
      console.log("Response status:", res)
      const data = await res.json()
      console.log('Success:', data)
      // Show result (output image)
      setResultUrl(data.image)
    } catch (err) {
      console.error('Error:', err)
    } finally {
      setLoading(false)
    }
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4 max-w-md mx-auto p-4 border rounded-xl shadow">
      <h2 className="text-xl font-semibold">Enhance Your Photo</h2>

      <input
        type="file"
        accept="image/*"
        onChange={handleImageChange}
        className="block w-full border rounded p-2"
      />

      {previewUrl && (
        <img src={previewUrl} alt="Preview" className="w-full h-auto rounded shadow" />
      )}

      <input
        type="text"
        placeholder="e.g. make me look more muscular"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        className="block w-full border rounded p-2"
      />

      <button
        type="submit"
        className="w-full bg-blue-600 text-white p-2 rounded disabled:opacity-50"
        disabled={loading}
      >
        {loading ? 'Processing...' : 'Enhance Image'}
      </button>

      {/*output image*/}

      {resultUrl && (
        <div className="mt-6">
          <h3 className="text-lg font-medium mb-2">Enhanced Image</h3>
          <img src={resultUrl} alt="AI result" className="rounded shadow" />
        </div>
      )}
    </form>
  )
}
