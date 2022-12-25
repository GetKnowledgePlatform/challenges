class Star {
  constructor() {
    this.x = random(-width, width);
    this.y = random(-height, height);
    this.z = random(width);
  }
  
  update(speed) {
    this.z -= speed;
    if (this.z < 1) {
      this.x = random(-width, width);
      this.y = random(-height, height);
      this.z = random(width);
    }
  }
  
  show() {
    fill(255);
    noStroke();
    
    let sx = map(this.x/this.z, 0, 1, 0, width)
    let sy = map(this.y/this.z, 0, 1, 0, height)
    
    let r = map(this.z, 0, width, 16, 0)
    
    ellipse(sx, sy, r, r);
  }
  
}