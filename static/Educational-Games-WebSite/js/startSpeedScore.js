const COUNT = 1;
let started = false;
function start() {
    if (started) {return}
    document.getElementById("ans").style.display = 'block';
    document.getElementById("answer").innerHTML = 0;
    level = document.getElementById("level").value;
    document.getElementById('example').innerHTML = generate(level);
    let start_time = new Date();
    let stop_time = start_time.setMinutes(start_time.getMinutes() + COUNT)
    let countdown = setInterval(function () {
        let now = new Date().getTime();
        let remain = stop_time - now;
        let min = Math.floor((remain % (1000 * 60 * 60)) / (1000 * 60));
        let sec = Math.floor((remain % (1000 * 60)) / 1000);
        sec = sec < 10 ? "0" + sec : sec
        document.getElementById("timer").innerHTML = min + ":" + sec;
        if (remain < 0) {
            clearInterval(countdown);
            let total = document.getElementById("answer");
            document.getElementById("timer").innerHTML = "Ваш результат: " + total.innerHTML;
            started = false;
            document.getElementById("ans").style.display = 'none';
            let xhr = new XMLHttpRequest();
            xhr.open('POST', 'ajax', true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.send(JSON.stringify({value: total.innerHTML}));
        }
    }, 1000);
    started = true;
}


function generate(level) {
    if (level === '1') {
        return generate_1_lvl()
    }
    else if (level === '2') {
        return generate_2_lvl()
    }
}


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

function generate_2_lvl() {
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
