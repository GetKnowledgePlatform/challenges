class Box {
  
  constructor(x,y,z,size) {
    this.x = x;
    this.y = y;
    this.z = z;
    this.size = size;
  }
  
  
  show() {
    push();
    translate(this.x, this.y, this.z);
    fill(255);
    box(this.size);
    pop();
  }
  
  generate() {
    let boxes = [];
    let start_pos = -1;
    let end_pos = 2;
    for (let new_x=start_pos; new_x<end_pos; new_x++) {
      for (let new_y=start_pos; new_y<end_pos; new_y++) {
        for (let new_z=start_pos; new_z<end_pos; new_z++) {
          
          let sum = abs(new_x) + abs(new_y) + abs(new_z);
          
          if (sum > 1) {
            let new_size = this.size/3;
            let b = new Box(
              this.x + new_x*new_size, 
              this.y + new_y*new_size, 
              this.z + new_z*new_size, 
              new_size
            );
            boxes.push(b);
          }
        }
      }
    }
    return boxes;
  }
}