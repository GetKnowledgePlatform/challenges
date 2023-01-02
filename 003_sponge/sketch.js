let angle = 0.0;
let sponge = [];

function setup() {
  createCanvas(400, 400, WEBGL);
  my_box = new Box(0, 0, 0, 200);
  sponge.push(my_box);
}

function mousePressed() {
  let nextGeneration = [];
  for (let b of sponge) {
    let boxes = b.generate();
    nextGeneration = nextGeneration.concat(boxes);
  }
  sponge = nextGeneration;
}

function draw() {
  background(0);
  noStroke();
  lights();
  
  rotateX(millis()/1000);
  rotateY(millis()/1000);
  angle += 0.01;
  for (let b of sponge) {
    b.show();
  }
  
}