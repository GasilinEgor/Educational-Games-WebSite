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
    example.innerHTML = generate();
})
function is_right(example, answer) {
    return (Number(example.at(0)) + Number(example.at(-1))) === Number(answer);
}