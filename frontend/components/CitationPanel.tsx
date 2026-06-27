interface Props {
  citations: string[];
}

export default function CitationPanel({
  citations,
}: Props) {

  return (
    <div className="border-l p-4 w-80">

      <h2 className="font-bold mb-4">
        Sources
      </h2>

      {citations.map(
        (
          citation,
          index
        ) => (
          <div
            key={index}
            className="border p-2 mb-2 rounded"
          >
            {citation}
          </div>
        )
      )}

    </div>
  );
}