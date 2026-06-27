import Navbar from "@/components/Navbar";
import FileUpload from "@/components/FileUpload";
import ChatBox from "@/components/ChatBox";

export default function Home() {
  return (
    <div>
      <Navbar />

      <div className="grid grid-cols-2 gap-6 p-6">
        <FileUpload />
        <ChatBox />
      </div>
    </div>
  );
}