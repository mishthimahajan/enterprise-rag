// "use client";

// import { useState } from "react";
// import api from "@/services/api";

// export default function FileUpload() {
//   const [file, setFile] = useState<File | null>(null);
//   const [loading, setLoading] = useState(false);

//   const uploadFile = async () => {
//     if (!file) {
//       alert("Please select a file");
//       return;
//     }

//     try {
//       setLoading(true);

//       const formData = new FormData();
//       formData.append("file", file);

//       const response = await api.post(
//         "/upload",
//         formData,
//         {
//           headers: {
//             "Content-Type":
//               "multipart/form-data",
//           },
//         }
//       );

//       alert("Upload Successful");

//       console.log(response.data);
//     } catch (error: any) {
//       console.error(error);

//       alert(
//         error?.response?.data?.detail ||
//           "Upload Failed"
//       );
//     } finally {
//       setLoading(false);
//     }
//   };

//   return (
//     <div className="border rounded-xl p-6 shadow">

//       <h2 className="text-xl font-bold mb-4">
//         Upload Document
//       </h2>

//       <input
//         type="file"
//         onChange={(e) =>
//           setFile(
//             e.target.files?.[0] || null
//           )
//         }
//       />

//       <button
//         onClick={uploadFile}
//         disabled={loading}
//         className="bg-blue-600 text-white px-4 py-2 rounded mt-4"
//       >
//         {loading
//           ? "Uploading..."
//           : "Upload"}
//       </button>

//     </div>
//   );
// }

"use client";

import { useState } from "react";
import api from "@/services/api";

export default function FileUpload() {
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);

  const uploadFile = async () => {
    if (!file) {
      alert("Please select a file");
      return;
    }

    try {
      setLoading(true);

      const formData = new FormData();

      // The field name must match FastAPI: file: UploadFile = File(...)
      formData.append("file", file);

      const response = await api.post(
        "/upload",
        formData
      );

      console.log("Upload response:", response.data);

      alert("Upload Successful");

    } catch (error: any) {

      console.error("Upload error:", error);

      if (error.response) {
        alert(
          JSON.stringify(
            error.response.data,
            null,
            2
          )
        );
      } else {
        alert("Upload failed. Check server.");
      }

    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="border rounded-xl p-6 shadow">

      <h2 className="text-xl font-bold mb-4">
        Upload Document
      </h2>

      <input
        type="file"
        onChange={(e) => {
          const selectedFile =
            e.target.files?.[0] || null;

          setFile(selectedFile);

          console.log(
            "Selected file:",
            selectedFile
          );
        }}
      />

      <button
        onClick={uploadFile}
        disabled={loading}
        className="bg-blue-600 text-white px-4 py-2 rounded mt-4"
      >
        {
          loading
            ? "Uploading..."
            : "Upload"
        }
      </button>

    </div>
  );
}