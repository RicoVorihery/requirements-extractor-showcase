import { useState } from "react";
import Section from "../components/Section";
import { MOCK_EXTRACTION_RESULT } from "../mock/extractionResult";

export default function Demo() {
  const [showResult, setShowResult] = useState(false);

  return (
    <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 24 }}>
      <div>
        <Section title="Extraction Configuration">
          <p>Configure where requirement information is located.</p>

          <label>
            Identifier position
            <select style={{ display: "block", marginTop: 4 }}>
              <option>On its own line</option>
              <option>Inline with text</option>
            </select>
          </label>

          <label style={{ marginTop: 12, display: "block" }}>
            Coverage information
            <select style={{ display: "block", marginTop: 4 }}>
              <option>Not present</option>
              <option>After requirement text</option>
            </select>
          </label>

          <button style={{ marginTop: 16 }} onClick={() => setShowResult(true)}>
            Run extraction
          </button>
        </Section>
      </div>

      <div>
        <Section title="Extraction Result">
          {!showResult && <p>No extraction run yet.</p>}

          {showResult && (
            <pre style={{ background: "#f5f5f5", padding: 12 }}>
              {JSON.stringify(MOCK_EXTRACTION_RESULT, null, 2)}
            </pre>
          )}
        </Section>
      </div>
    </div>
  );
}
