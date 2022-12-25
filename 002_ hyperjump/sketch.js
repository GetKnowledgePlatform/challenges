
const stars = [];

function createStars(numStars) {
  i = 0;
  while(i < numStars) {
    stars[i] = new Star();
    i++;
  }
}

function setup() {
  createCanvas(600, 600);
  createStars(1000);
}

function draw() {
  background(0);
  
  let speed = map(mouseX, 0, width, 0, 20);
  translate(width/2, height/2);
  for(let star of stars) {
    star.show();
    star.update(speed);
  }
}