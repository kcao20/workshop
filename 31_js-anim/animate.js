// Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon
// SoftDev pd2
// K31 -- canvas based JS animation
// 2022-02-15t

// model for HTML5 canvas-based animation

// SKEELTON

//access canvas and buttons via DOM
var c = document.getElementById("playground"); // GET CANVAS
var dotButton = document.getElementById("buttonCircle"); // GET DOT BUTTON
var stopButton = document.getElementById("buttonStop"); // GET STOP BUTTON

//prepare to interact with canvas in 2D
var ctx = c.getContext("2d"); // YOUR CODE HERE

//set fill color to team color
ctx.fillStyle = "blue"; // YOUR CODE HERE

var requestID; //init global var for use with animation frames

//var clear = function(e) {
var clear = (e) => {
  ctx.clearRect(0, 0, 500, 500);
  // YOUR CODE HERE
}

var radius = 0;
var growing = true;

//var drawDot = function() {
var drawDot = () => {
  if (requestID) {
    stopIt();
  }
  console.log("drawDot invoked...");
  clear();
  if (radius >= 250) {
    growing = false;
  } else if (radius <= 0) {
    growing = true;
  }
  if (growing === true) {
    radius += 1;
  } else {
    radius -= 1;
  }
  ctx.beginPath();
  ctx.arc(250, 250, radius, 0, 2 * Math.PI);
  ctx.stroke();
  ctx.fill();
  requestID = window.requestAnimationFrame(drawDot);
}

//var stopIt = function() {
var stopIt = () => {
  cancelAnimationFrame(requestID);
}

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);
