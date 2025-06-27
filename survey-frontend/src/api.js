export async function getNextQuestion(token) {
  const res = await fetch("http://localhost:8000/api/survey/quiz/", {
    method: "GET",
    headers: {
      Authorization: `Bearer ${token}`
    }
  });
  return res.json();
}

export async function submitAnswer(questionId, text, isCorrect, token) {
  const res = await fetch("http://localhost:8000/api/survey/quiz/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`
    },
    body: JSON.stringify({
      question: questionId,
      text,
      is_correct: isCorrect
    })
  });
  return res.json();
}
