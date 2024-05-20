let total = 0;
ans = document.getElementById('answer')
const button = document.getElementById('set_answer');
button.addEventListener('click', () => {
    let answer = document.getElementById('player_answer')
    let example = document.getElementById('example')
    if (is_right(example.innerHTML, answer.value)) {
        total++;
        ans.innerHTML = total;
    }
    answer.value = "";
    example.innerHTML = generate(document.getElementById("level").value);
})
function is_right(example, answer) {
    return calculateAnswer(example) === Number(answer);
}


function calculateAnswer(expression) { //функция для вычисления ответа выражения
    expression = expression.replace(/\//g, '*1/');
    let answer = eval(expression);
    answer = Math.round(answer * 100) / 100;
    return answer;
}
