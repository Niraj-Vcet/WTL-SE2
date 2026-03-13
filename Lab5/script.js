const questions = [
{
question: "What does JS stand for?",
answers: ["JavaScript", "JavaStyle", "JustScript", "JScript"],
correct: 0
},
{
question: "Which company developed JavaScript?",
answers: ["Microsoft", "Netscape", "Google", "Apple"],
correct: 1
},
{
question: "Which symbol is used for comments in JS?",
answers: ["//", "##", "**", "!!"],
correct: 0
}
];

let currentQuestion = 0;
let score = 0;

const questionElement = document.getElementById("question");
const answerButtons = document.querySelectorAll(".answer");
const nextBtn = document.getElementById("nextBtn");
const scoreDisplay = document.getElementById("score");

nextBtn.style.display = "none";

function loadQuestion(){

let q = questions[currentQuestion];

questionElement.textContent = q.question;

answerButtons.forEach((btn, index)=>{
btn.textContent = q.answers[index];
btn.classList.remove("correct","wrong");
btn.disabled = false;

btn.onclick = () => checkAnswer(index, btn);
});

}

function checkAnswer(index, button){

let correctIndex = questions[currentQuestion].correct;

if(index === correctIndex){
button.classList.add("correct");
score++;
}else{
button.classList.add("wrong");
answerButtons[correctIndex].classList.add("correct");
}

answerButtons.forEach(btn => btn.disabled = true);

nextBtn.style.display = "block";

}

nextBtn.onclick = () => {

currentQuestion++;

if(currentQuestion < questions.length){
loadQuestion();
nextBtn.style.display = "none";
}else{
showScore();
}

};

function showScore(){

document.querySelector("#answers").style.display = "none";
questionElement.textContent = "Quiz Finished!";
nextBtn.style.display = "none";

scoreDisplay.textContent = "Your Score: " + score + "/" + questions.length;

}

loadQuestion();