let img;
let n=5; // poner valor que me pase ruben del numero de computadoras

/*function preload() {
  computer = loadImage('assets/computer.png');
}*/

function computadoras(n1){
  let angulo = TWO_PI / n1;

  for (let a = 0; a < TWO_PI; a += angulo) {
    let cx = 0 + cos(a) * 100;
    let cy = 0 + sin(a) * 100;
    fill(255);
    ellipse(cx,cy, 50);
  }
}
function star(x, y, radius1, radius2, npoints) {
  let angle = TWO_PI / npoints;
  let halfAngle = angle / 2.0;
  

  beginShape();
  for (let a = 0; a < TWO_PI; a += angle) {
    let sx = x + cos(a) * radius2;
    let sy = y + sin(a) * radius2;
    vertex(sx, sy);

    sx = x + cos(a + halfAngle) * radius1;
    sy = y + sin(a + halfAngle) * radius1;
    vertex(sx, sy);

  }
  endShape(CLOSE);
}

function setup() {
  createCanvas(500, 350);
  //Image(computer, width * 2, height * 2);
}

function draw() {
  background(84, 240, 158);
  translate(width * 0.5, height * 0.5);

  star(0, 0, 0, 100, n);

  fill(0, 85, 255);
  ellipse(0,0, 50);

  computadoras(n);


}

