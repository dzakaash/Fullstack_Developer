// siapkan canvas
const mycanvas = document.querySelector("#mycanvas");
// atur ukuran canvas
mycanvas.width = window.innerWidth;
mycanvas.height = window.innerHeight;
// Tentukan Context
const c = mycanvas.getContext("2d");

// Canvas API shape bisa membentuk  Rectangle, Arc/Circle, Path, Bezier & Quadratic Curve
// Manipulasi Canvas
// rectangle
c.fillStyle = "pink";
c.strokeStyle = "#999";
c.lineWidth = 5;

c.rect(50, 50, 300, 300);
c.fill();
c.stroke();
// arc, circle
c.fillStyle = "lightgreen";

c.beginPath();
c.arc(550, 200, 150, 0, 2 * Math.PI);
c.fill();
c.stroke();

// path, triangle
c.fillStyle = "lightblue";

c.beginPath();
c.moveTo(900, 50);
c.lineTo(1050, 350);
c.lineTo(750, 350);
c.closePath();
c.fill();
c.stroke();
// Canvas 3rd party library : D3.js, three.js, p5.js, matter.js, Phaser, babylon.js
