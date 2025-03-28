let perceptron;
let points = new Array(100);
let isTraining = true;
let guessRatio = true;
let ger = 0;

function setup() {
  createCanvas(550, 550);
  perceptron = new Perceptron(3);
  for (let i = 0; i < points.length; i++) {
    points[i] = new Point(random(-1, 1), random(-1, 1));
    //points[i].debug();
  }
}

function draw() {
  background(255);
  for (let i = 0; i < points.length; i++) {
    points[i].show();
  }
  for (let i = 0; i < points.length; i++) {
    const pt = points[i];
    //antigo método de train
    //perceptron.train(inputs, pt.label);
    //input com o bias
    const inputs = [pt.x, pt.y, pt.bias];
    const target = pt.label;
    const guess = perceptron.guess(inputs);
    if (guess == target) {
      fill(0, 255, 0);
    } else {
      fill(255, 0, 0);
    }
    noStroke();
    ellipse(pt.getPixelX(), pt.getPixelY(), 15, 15);
  }
  drawLine();
  isTraining && trainSinglePoint() && ger++;

  if (ger == 100) {
    isTraining = false;
    guessRatio && calcGuessRatio();
  }
}

function calcGuessRatio() {
  let testPoints = new Array(100);
  let correctGuess = 0;
  for (let i = 0; i < points.length; i++) {
    testPoints[i] = new Point(random(-1, 1), random(-1, 1));
    const inputs = [testPoints[i].x, testPoints[i].y, testPoints[i].bias];
    const guess = perceptron.guess(inputs);

    if (guess == testPoints[i].label) {
      correctGuess += 1;
    }

    console.log(`Taxa de acertos: ${correctGuess}%`);
    guessRatio = false;
  }
}

function drawLine() {
  stroke(0);
  //line(0, height, width, 0);
  const p1 = new Point(-1, f(-1));
  const p2 = new Point(1, f(1));
  line(p1.getPixelX(), p1.getPixelY(), p2.getPixelX(), p2.getPixelY());
  const guessP1 = new Point(-1, perceptron.guessY(-1));
  const guessP2 = new Point(1, perceptron.guessY(1));
  line(
    guessP1.getPixelX(),
    guessP1.getPixelY(),
    guessP2.getPixelX(),
    guessP2.getPixelY()
  );
}

let trainningIndex = 0;
function trainSinglePoint() {
  const pt = points[trainningIndex];
  const inputs = [pt.x, pt.y, pt.bias];
  perceptron.train(inputs, pt.label);
  trainningIndex++;

  if (trainningIndex == points.length) {
    trainningIndex = 0;
  }
}
