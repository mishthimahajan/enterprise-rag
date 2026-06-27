interface Props {
  text: string;
  role: "user" | "assistant";
}

export default function MessageBubble({
  text,
  role,
}: Props) {
  return (
    <div
      className={`p-3 rounded-lg mb-2 ${
        role === "user"
          ? "bg-blue-100"
          : "bg-green-100"
      }`}
    >
      {text}
    </div>
  );
}