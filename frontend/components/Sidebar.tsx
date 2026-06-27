"use client";

export default function Sidebar() {
  return (
    <div className="w-72 h-screen bg-gray-900 text-white p-4">
      <h2 className="text-xl font-bold mb-6">
        Enterprise RAG
      </h2>

      <button className="w-full bg-blue-600 p-2 rounded">
        + New Chat
      </button>

      <div className="mt-6">
        <div className="p-2 hover:bg-gray-800 rounded">
          Leave Policy Discussion
        </div>

        <div className="p-2 hover:bg-gray-800 rounded">
          Security Audit
        </div>
      </div>
    </div>
  );
}