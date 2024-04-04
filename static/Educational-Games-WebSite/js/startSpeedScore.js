const COUNT = 1;
let started = false;

function start() {
    if (started) {return}
    document.getElementById("ans").style.display = 'block';
    document.getElementById("answer").innerHTML = 0;
    document.getElementById('example').innerHTML = generate()
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


function generate() {
    return Math.floor(Math.random() * 10) + ' + ' + Math.floor(Math.random() * 10);
}