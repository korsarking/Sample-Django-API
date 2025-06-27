import React, { useEffect, useState } from "react";

export default function Summary({ token }) {
  const [summary, setSummary] = useState(null);

  useEffect(() => {
    fetch("http://localhost:8000/api/survey/quiz/summary/", {
      headers: { Authorization: `Bearer ${token}` }
    })
      .then(res => res.json())
      .then(setSummary);
  }, []);

  if (!summary) return <p>Загрузка результатов...</p>;

  return (
    <div>
      <h2>Результат</h2>
      <p>Правильных ответов: {summary.correct_answers}</p>
      <p>Неправильных ответов: {summary.incorrect_answers}</p>
      <p>Точность: {summary.accuracy_percent}%</p>

      <h3>Ответы:</h3>
      <ul>
        {summary.results.map((item, i) => (
          <li key={i}>
            <strong>{item.question_text}</strong>: {item.text} — {item.is_correct ? "✔️" : "❌"}
          </li>
        ))}
      </ul>
    </div>
  );
}
