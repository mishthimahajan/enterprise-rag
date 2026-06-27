// "use client";

// import { useState } from "react";
// import api from "@/services/api";


// interface Message {
//   role: "user" | "assistant";
//   content: string;
//   sources?: string[];
// }


// export default function ChatBox() {
//   const [question, setQuestion] = useState("");
//   const [loading, setLoading] = useState(false);

//   const [messages, setMessages] = useState<Message[]>([]);


//   const askQuestion = async () => {

//     if (!question.trim()) return;


//     const userMessage: Message = {
//       role: "user",
//       content: question,
//     };


//     setMessages((prev) => [
//       ...prev,
//       userMessage
//     ]);


//     setQuestion("");


//     try {

//       setLoading(true);


//       const response = await api.post(
//         "/query",
//         {
//           question: userMessage.content,
//         }
//       );


//       const assistantMessage: Message = {
//         role: "assistant",
//         content:
//           response.data.answer ||
//           "No answer generated.",

//         sources:
//           response.data.sources || [],
//       };


//       setMessages((prev) => [
//         ...prev,
//         assistantMessage
//       ]);

//     } catch (error) {

//       console.error(error);


//       setMessages((prev) => [
//         ...prev,
//         {
//           role: "assistant",
//           content:
//             "❌ Unable to get response from server.",
//         },
//       ]);

//     } finally {

//       setLoading(false);

//     }

//   };


//   return (
//     <div className="border rounded-xl p-6 shadow-lg h-full bg-black">

//       <h2 className="text-2xl font-bold mb-4 text-white">
//         Enterprise RAG Assistant
//       </h2>


//       {/* Chat Messages */}
//       <div className="h-87.5 overflow-y-auto border rounded-lg p-4 mb-4 bg-gray-900">

//         {
//           messages.length === 0 &&
//           (
//             <p className="text-gray-400">
//               Upload documents and ask questions...
//             </p>
//           )
//         }


//         {
//           messages.map((msg, index) => (

//             <div
//               key={index}
//               className={`mb-4 flex ${
//                 msg.role === "user"
//                   ? "justify-end"
//                   : "justify-start"
//               }`}
//             >

//               <div
//                 className={`max-w-[85%] p-4 rounded-xl shadow-md ${
//                   msg.role === "user"
//                     ? "bg-blue-600 text-white"
//                     : "bg-green-200 text-black"
//                 }`}
//               >

//                 {/* Role */}
//                 <div className="font-bold mb-2">

//                   {
//                     msg.role === "user"
//                     ? "You"
//                     : "AI Assistant"
//                   }

//                 </div>


//                 {/* Answer */}
//                 <div className="whitespace-pre-wrap">

//                   {msg.content}

//                 </div>


//                 {/* Citations */}
//                 {
//                   msg.role === "assistant" &&
//                   msg.sources &&
//                   msg.sources.length > 0 && (

//                     <div className="mt-4 border-t pt-3">

//                       <h3 className="text-sm font-bold text-gray-700 mb-2">
//                         📚 Sources
//                       </h3>


//                       {
//                         msg.sources.map(
//                           (source, i) => (

//                             <div
//                               key={i}
//                               className="
//                                 text-xs
//                                 bg-white
//                                 p-3
//                                 rounded-lg
//                                 mb-2
//                                 border
//                                 text-gray-800
//                               "
//                             >

//                               {source}

//                             </div>

//                           )
//                         )
//                       }


//                     </div>

//                   )
//                 }


//               </div>


//             </div>

//           ))
//         }


//         {/* Loading */}
//         {
//           loading && (
//             <div className="flex justify-start">

//               <div className="bg-gray-700 text-white p-3 rounded-lg">

//                 Thinking...

//               </div>

//             </div>
//           )
//         }


//       </div>


//       {/* Input */}
//       <textarea

//         rows={4}

//         value={question}

//         onChange={(e) =>
//           setQuestion(e.target.value)
//         }

//         placeholder="Ask your question about the documents..."

//         className="
//           w-full
//           border
//           rounded-lg
//           p-3
//           text-white
//           bg-gray-800
//           focus:outline-none
//         "

//       />


//       {/* Send button */}
//       <button

//         onClick={askQuestion}

//         disabled={loading}

//         className="
//           mt-4
//           bg-green-600
//           hover:bg-green-700
//           text-white
//           px-6
//           py-2
//           rounded-lg
//         "

//       >

//         {
//           loading
//             ? "Thinking..."
//             : "Send"
//         }

//       </button>


//     </div>
//   );
// }

"use client";

import { useState } from "react";
import api from "@/services/api";


interface Source {
  text: string;
  filename: string;
  page: number;
  score: number;
}


interface Message {
  role: "user" | "assistant";
  content: string;
  sources?: Source[];
}


export default function ChatBox() {

  const [question, setQuestion] = useState("");
  const [loading, setLoading] = useState(false);

  const sessionId = "user-001";

  const [messages, setMessages] =
    useState<Message[]>([]);


  const askQuestion = async () => {

    if (!question.trim()) return;


    const userMessage: Message = {
      role: "user",
      content: question,
    };


    setMessages(prev => [
      ...prev,
      userMessage,
    ]);


    setQuestion("");


    try {

      setLoading(true);


      const response = await api.post(
        "/query",
        {
  question: userMessage.content,
  session_id: sessionId
}
      );


      const assistantMessage: Message = {
        role: "assistant",
        content:
          response.data.answer ||
          "No answer generated",

        sources:
          response.data.sources || [],
      };


      setMessages(prev => [
        ...prev,
        assistantMessage,
      ]);

    }
    catch (error) {

      console.error(error);


      setMessages(prev => [
        ...prev,
        {
          role: "assistant",
          content:
            "❌ Unable to get response from server",
        },
      ]);

    }
    finally {

      setLoading(false);

    }

  };


  return (

    <div className="border rounded-xl p-6 shadow-lg h-full bg-black">

      <h2 className="text-2xl font-bold text-white mb-4">
        Enterprise RAG Assistant
      </h2>


      {/* Messages */}
      <div className="h-87.5 overflow-y-auto border rounded-lg p-4 bg-gray-900 mb-4">


        {
          messages.length === 0 &&
          (
            <p className="text-gray-400">
              Upload documents and ask questions...
            </p>
          )
        }


        {
          messages.map((msg, index) => (

            <div
              key={index}
              className={`mb-4 flex ${
                msg.role === "user"
                ? "justify-end"
                : "justify-start"
              }`}
            >

              <div
                className={`max-w-[85%] p-4 rounded-xl ${
                  msg.role === "user"
                  ? "bg-blue-600 text-white"
                  : "bg-green-200 text-black"
                }`}
              >


                {/* Role */}
                <div className="font-bold mb-2">

                  {
                    msg.role === "user"
                    ? "You"
                    : "AI Assistant"
                  }

                </div>


                {/* Answer */}
                <div className="whitespace-pre-wrap">

                  {msg.content}

                </div>


                {/* Sources */}
                {
                  msg.role === "assistant" &&
                  msg.sources &&
                  msg.sources.length > 0 && (

                    <div className="mt-4 border-t pt-3">

                      <h3 className="font-bold text-sm mb-2">
                        📚 Sources
                      </h3>


                      {
                        msg.sources.map((source, i) => (

                          <div
                            key={i}
                            className="
                              bg-white
                              text-black
                              rounded-lg
                              p-3
                              mb-2
                              text-xs
                            "
                          >

                            <p>
                              <b>File:</b>
                              {" "}
                              {source.filename}
                            </p>


                            <p>
                              <b>Page:</b>
                              {" "}
                              {source.page}
                            </p>


                            <p>
                              <b>Similarity:</b>
                              {" "}
                              {
                                (
                                  source.score * 100
                                ).toFixed(2)
                              }
                              %
                            </p>


                            <hr className="my-2" />


                            <p>
                              {source.text}
                            </p>

                          </div>

                        ))
                      }


                    </div>

                  )
                }


              </div>


            </div>

          ))
        }


        {/* Loading */}
        {
          loading && (

            <div className="text-white">
              Thinking...
            </div>

          )
        }


      </div>


      {/* Input */}
      <textarea

        rows={4}

        value={question}

        onChange={
          (e) => setQuestion(e.target.value)
        }

        placeholder="Ask your question about documents..."

        className="
          w-full
          p-3
          rounded-lg
          bg-gray-800
          text-white
          border
        "

      />


      <button

        onClick={askQuestion}

        disabled={loading}

        className="
          mt-4
          px-6
          py-2
          bg-green-600
          text-white
          rounded-lg
        "

      >

        {
          loading
          ? "Thinking..."
          : "Send"
        }

      </button>


    </div>

  );

}