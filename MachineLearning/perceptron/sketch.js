let perceptron;
let points = new Array(100);
function setup() {
  createCanvas(550, 550);
  for (let index = 0; index < points.length; index++) {
    points[index] = new Point(random(-1, 1), random(-1, 1));
  }

  perceptron = new Perceptron();
  const inputs = [-1, 0.5];
  const guess = perceptron.guess(inputs);
  console.log(`resultado ${guess}`);
}

function draw() {
  background(255);
  points.forEach((point) => {
    point.show();
  });
}
