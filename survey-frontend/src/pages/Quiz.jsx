import { useEffect, useState } from "react";
import { getNextQuestion, submitAnswer } from "../api";

function Quiz() {
  const [question, setQuestion] = useState(null);
  const [token, setToken] = useState(localStorage.getItem("access"));

  useEffect(() => {
    getNextQuestion(token).then((data) => {
      setQuestion(data.question);
    });
  }, [token]);

  const handleAnswer = async (text, isCorrect) => {
    const res = await submitAnswer(question.id, text, isCorrect, token);
    console.log(res);
  };

  return (
    <div>
      {question && (
        <>
          <h2>{question.text}</h2>
          <button onClick={() => handleAnswer("Париж", true)}>Париж</button>
          <button onClick={() => handleAnswer("Берлин", false)}>Берлин</button>
        </>
      )}
    </div>
  );
}

export default Quiz;
