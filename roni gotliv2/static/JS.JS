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


//print date to log
const d = Date();
console.log(d);

//pull the pathname from window location
const activePage = window.location.pathname;
console.log(window);
console.log(window.location);
console.log(activePage);

/*create an arey of the links in nav, 
compare each to pathname and mark the one that is active
*/ 
const navLinks = document.querySelectorAll('nav a').forEach(link => {    
  if(link.href.includes(`${activePage}`)){
    link.classList.add('active');
  }
});





