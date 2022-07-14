var i = 0;
var txt = 'Photos from Mexico';
var speed = 50;

function typeWriter() {
    if (i < txt.length) {
        document.getElementById("demo").innerHTML += txt.charAt(i);
        i++;
        setTimeout(typeWriter, speed);
    }
}


var i = 0;
var txt1 = 'call us - 04-9832761';
var speed = 50;

function typeWriter1() {
    if (i < txt.length) {
        document.getElementById("demo").innerHTML += txt1.charAt(i);
        i++;
        setTimeout(typeWriter1, speed);
    }
}






