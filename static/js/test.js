

const quizData = [
    {
        id: "0",
        type:"radio",
        
      question: "Выбери правильное хохо",
      options: ["enginer", "engineer", "eniginer", "ingineer"],
      answer: "o2",
    },
    // {
    //     id: "1",
    //     type:"nes-checkbox",
        
    //   question: "Выбери правильное хохо",
    //   options: ["enginer", "engineer", "eniginer", "ingineer"],
    //   answer: "o2",
    // },
    {
        id: "1",
        type:"radio",
      question: "Какого языка программирования не существует?",
      options: ["CSS", "Cython", "Q#", "F#"],
      answer: "CSS",
    },
    {
        id: "2",
        type:"radio",
      question: "Вложено четное количество кругов, начиная с радиуса 1 и увеличивающегося каждый раз на 1, и все они имеют общую точку. Область между всеми остальными кругами заштрихована, начиная с области внутри круга радиуса 2, но за пределами круга радиуса 1. Какое наименьшее количество кругов нужно, чтобы общая заштрихованная площадь была не меньше 2023π?",
      options: ["56", "64", "48", "46"],
      answer: "64",
    },
    {
        id: "3",
        type:"radio",
        question: "Выбери иероглиф который значит 'дождь'! (фантазия кончилась удачи)",
        options: ["霜", "霰", "霓", "雨"],
        answer: "雨",
      },
  ];
  
  const quizContainer = document.getElementById('quiz');
  const resultContainer = document.getElementById('result');
  const submitButton = document.getElementById('submit');
  const retryButton = document.getElementById('retry');
  const showAnswerButton = document.getElementById('showAnswer');
  
  let currentQuestion = 0;
  let score = 0;
  let incorrectAnswers = [];
  
  function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
  }
  
  function displayQuestion() {
    const questionData = quizData[currentQuestion];
  
    const questionElement = document.createElement('div');
    questionElement.className = 'question';
    questionElement.innerHTML = questionData.question;
  
    const optionsElement = document.createElement('div');
    optionsElement.className = 'options';
  
    const shuffledOptions = [...questionData.options];
    shuffleArray(shuffledOptions);
  
    for (let i = 0; i < shuffledOptions.length; i++) {
      const option = document.createElement('label');
        option.className = 'option';
        if (questionData.type == "radio") {
            console.log(questionData.type)
  
            const radio = document.createElement('input');
            radio.type = 'radio';
            radio.name = 'quiz';
            radio.value = shuffledOptions[i];
            option.appendChild(radio);
        }
        
            if (questionData.type == "button") {
            const button = document.createElement('button');
            button.type = 'button';
            button.name = 'quiz';
            button.value = shuffledOptions[i];
            option.appendChild(button);
            
        }
        if (questionData.type == "nes-checkbox") {
            const button = document.createElement('checkbox');
            button.type = 'checkbox';
            button.name = 'quiz';
            button.value = shuffledOptions[i];
            option.appendChild(button);
            
        }
  
      const optionText = document.createTextNode(shuffledOptions[i]);
  
      
      option.appendChild(optionText);
      optionsElement.appendChild(option);
    }
  
    quizContainer.innerHTML = '';
    quizContainer.appendChild(questionElement);
    quizContainer.appendChild(optionsElement);
  }
  
function checkAnswer() {
    if (currentQuestion == 0){
    const selectedOption = document.querySelector('input[name="quiz"]:checked');
        if (selectedOption) {
            const answer = selectedOption.value;
            if (answer === quizData[currentQuestion].answer) {
                score++;
            } else {
                incorrectAnswers.push({
                    question: quizData[currentQuestion].question,
                    incorrectAnswer: answer,
                    correctAnswer: quizData[currentQuestion].answer,
                });
            }
        }
        if (currentQuestion == 1) {
            const selectedOption = document.querySelector('input[name="quiz"]:checked');
            if (selectedOption) {
                const answer = selectedOption.value;
                if (answer === quizData[currentQuestion].answer) {
                    score++;
                } else {
                    incorrectAnswers.push({
                        question: quizData[currentQuestion].question,
                        incorrectAnswer: answer,
                        correctAnswer: quizData[currentQuestion].answer,
                    });
                }
            }
    }
      currentQuestion++;
      selectedOption.checked = false;
      if (currentQuestion < quizData.length) {
        displayQuestion();
      } else {
        displayResult();
      }
    }
  }
  
  function displayResult() {
    resultContainer.innerHTML = `У тебя ${score} верных из ${quizData.length}!`;
  }
  
  
  submitButton.addEventListener('click', checkAnswer);
  
  displayQuestion();