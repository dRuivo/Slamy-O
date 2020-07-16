let socket
let color = '#000'
let strokeWidth = 4
let cv
let scale = 0.05
let center
let north = 0.
let map = []

function setup() {
	// Creating canvas
	cv = createCanvas(windowWidth, windowHeight)
	frameRate(30);

	center = {x:width/2, y:height/2}
	//centerCanvas()
	cv.background(255, 255, 255)

	console.log(windowWidth, windowHeight);

	// Start the socket connection
	socket = io();

	socket.on('connect', function() {
        socket.emit('my_event', {data: 'I\'m connected!'});
	});
	socket.on('lidar_data', function(data) {
		//console.log(data);
		map = data
		
	});
}

function draw() {
	cv.background(255, 255, 255)
	fill('blue')
	circle(center.x, center.y, strokeWidth)

	strokeWeight(4)
	stroke('green')
	line(width - 40, 20, width - 40 + 15* sin(north), 20 - 15 * cos(north))

	map.forEach(draw_line);
};

function draw_line(point) {
	strokeWeight(0)
	fill(color)
	x = point.x * cos(north) - point.y * sin(north)
	y = point.x * sin(north) + point.y * cos(north)
	circle(center.x + scale * x, 
		center.y + scale * y,
		strokeWidth)
};

function centerCanvas() {
	const x = (windowWidth - width) / 2
	const y = (windowHeight - height) / 2
	cv.position(x, y)
}

function windowResized() {
	//centerCanvas()
	cv.resizeCanvas(windowWidth, windowHeight, false)
}

function mouseWheel(event) {
	//print(event.delta);
	//move the square according to the vertical scroll amount
	scale += 0.0005 * event.delta;
	//block page scrolling
	return false;
}

function mouseDragged(event) {
	if (event.ctrlKey) {
		north += 0.01*(mouseX - pmouseX)
	} else {
		center.x += mouseX - pmouseX
		center.y += mouseY - pmouseY
	}
	
}