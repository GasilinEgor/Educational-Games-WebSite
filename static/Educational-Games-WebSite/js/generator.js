var totalTrainingTime = parseInt(document.getElementById('trainingTime').value) * 60; // Общее время тренировки (секунды)
var operationType = [];
var startTime;
var timerInterval;
var currentQuestion;
var correctAnswer;
var userInput;
var countdownElement = document.getElementById('countdown');
var timeRemainingElement = document.getElementById('timeRemaining');
var messageElement = document.getElementById('message');
var answerInput = document.getElementById('answer');
var startButton = document.getElementById('startButton');
var variableMode = document.getElementById('variableMode');
var trainingTimeSelect = document.getElementById('trainingTime');
var exampleTime = 10; // Время одного примера (секунды)
var currentExampleTime = 10;
var currentTotalTime = totalTrainingTime;
var totalExamples = 0;
var correctExamples = 0;

function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function check_skobka(a) {  // проверяет скобки в сгенерированном примере, удаляет если их много
    if (a[0] === '(' && a[a.length - 1] === ')') {
        a = a.slice(1, -1);
    }
    let chec = a.split('').filter(i => i === '*' || i === '/');
    if (chec.length === 0) {
        let b = a.split('').filter(i => i !== '(' && i !== ')').join('');
        return b;
    }
    return a;
}


function is_oper(oper) { 
    return oper === '+' || oper === '-' || oper === '*' || oper === '/';
}

function priority(oper) {
    if (oper === '+' || oper === '-') {
        return 2;
    } else if (oper === '*' || oper === '/') {
        return 3;
    } else if (oper === '(') {
        return 1;
    }
    return 0;
}

function convert_to_infix(polish_notation) {
    let ans = [];
    for (let i of polish_notation) {
        if (is_oper(i)) {
            let op1 = ans[0];
            ans.shift();
            let op2 = ans[0];
            ans.shift();
            if (i === '/' || i === '*') {
                ans.unshift(op2 + i + op1);
            } else {
                ans.unshift("(" + op2 + i + op1 + ")");
            }
        } else {
            ans.unshift(i);
        }
    }
    return ans[0];
}

function calculateAnswer(expression) { //функция для вычисления ответа выражения
    expression = expression.replace(/\//g, '*1/');
    let answer = eval(expression);
    answer = Math.round(answer * 100) / 100;
    return answer;
}

  
function generateQuestion() { //функция для генерации 1 примера
    let level;
    if (variableMode.value === '2') {
        level = 2;
    } else if (variableMode.value === '1') {
        level = 1;
    }

    let expr;
    if (level === 1) {
        expr = generate_1_lvl();
    } else if (level === 2) {
        expr = generate_2_lvl();
    }

    currentQuestion = expr;
    correctAnswer = calculateAnswer(expr);
    
    document.querySelector('.question').textContent = currentQuestion;
    answerInput.value = '';
    userInput = null;
    messageElement.textContent = '';
    answerInput.disabled = false;
    answerInput.focus();
    countdownElement.textContent = 'Осталось времени: ' + currentExampleTime + ' сек.';
    timerInterval = setInterval(updateTimer, 1000);
}
function generate_1_lvl() { 
    operationType = ['+', '-', '*', '/'];
    var chosen_sign = operationType[getRandomNumber(0, operationType.length - 1)];
    let expr;
    if (chosen_sign === '/') {
        expr = [Math.floor(Math.random() * 99) + 2, Math.floor(Math.random() * 19) + 2];
        expr = [Math.max(...expr), Math.min(...expr)];
        expr = [expr[0] - expr[0] % expr[1], Math.min(...expr)];
    } else if (chosen_sign === '*') {
        expr = [Math.floor(Math.random() * 20) + 6, Math.floor(Math.random() * 10) + 2];
    } else {
        expr = [Math.floor(Math.random() * 99) + 2, Math.floor(Math.random() * 99) + 2];
    }
    expr.push(chosen_sign);
    for (let i = 0; i < expr.length; i++) {
        expr[i] = expr[i].toString();
    }
    return check_skobka(convert_to_infix(expr));
}

function generate_2_lvl(c) {
    operationType = ['+', '-', '*', '/'];
    var chosen_sign = operationType[getRandomNumber(0, operationType.length - 1)];
    let expr;
    if (chosen_sign === '/') {
        expr = [Math.floor(Math.random() * 99) + 2, Math.floor(Math.random() * 19) + 2];
        expr = [Math.max(...expr), Math.min(...expr)];
        expr = [expr[0] - expr[0] % expr[1], Math.min(...expr)];
    } else if (chosen_sign === '*') {
        expr = [Math.floor(Math.random() * 20) + 6, Math.floor(Math.random() * 10) + 2];
    } else {
        expr = [Math.floor(Math.random() * 49) + 2, Math.floor(Math.random() * 49) + 2];
    }
    expr.push(chosen_sign);
    expr.push(Math.floor(Math.random() * 10) + 2);
    let signs2 = ['+', '-', '*'];
    expr.push(signs2[Math.floor(Math.random() * signs2.length)]);

    for (let i = 0; i < expr.length; i++) {
        expr[i] = expr[i].toString();
    }
    return check_skobka(convert_to_infix(expr));
}


function updateTimer() {
    currentExampleTime--;
    currentTotalTime--;
    countdownElement.textContent = 'Осталось времени: ' + currentExampleTime + ' сек.';
    timeRemainingElement.textContent = 'Осталось: ' + formatTime(currentTotalTime);
    if (currentExampleTime < 0) {
        clearInterval(timerInterval);
        messageElement.textContent = 'Время истекло. Следующий пример:';
        messageElement.style.color = 'red';
        setTimeout(function() {
            totalExamples++;
            generateQuestion();
            currentExampleTime = 10;
        }, 500);
    }

    if (currentTotalTime < 0) {
        showResults();
    }

}

function formatTime(seconds) {
    var minutes = Math.floor(seconds / 60);
    var remainingSeconds = seconds % 60;
    return minutes + ' мин. ' + remainingSeconds + ' сек.';
}

function checkAnswer() {  //функция для проверки для введенного ответа
    if (userInput === correctAnswer) {
        clearInterval(timerInterval);
        messageElement.textContent = 'Правильно!';
        messageElement.style.color = 'green';
        answerInput.disabled = true;
        setTimeout(function() {
            correctExamples++;
            totalExamples++;
            if (currentTotalTime > 0) {
            generateQuestion();
            currentExampleTime = 10;
            } else {
                showResults();
            }
        }, 1000);
    } else {
        messageElement.textContent = 'Неправильно. Попробуйте еще раз.';
        messageElement.style.color = 'red';
        answerInput.value = '';
        answerInput.focus();
    }
}

function showResults() {
    clearInterval(timerInterval);

    countdownElement.textContent = 'Тренировка завершена!';
    messageElement.textContent = 'Примеров задано: ' + totalExamples + '. Правильно решено: ' + correctExamples + '.';
    answerInput.disabled = true;
    startButton.disabled = false;
    variableMode.disabled = false;
    trainingTimeSelect.disabled = false;
}

startButton.addEventListener('click', function() {
    currentTotalTime = parseInt(document.getElementById('trainingTime').value) * 60; // Общее время тренировки (секунды)
    startButton.disabled = true;
    variableMode.disabled = true;
    trainingTimeSelect.disabled = true;
    generateQuestion();
    startTime = new Date().getTime() / 1000;
    totalExamples = 0;
    correctExamples = 0;
});

answerInput.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        userInput = parseFloat(answerInput.value);
        checkAnswer();
    }
});