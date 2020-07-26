let socket

let cv
let gui
let j, c

let strokeWidth = 4

let scale = 0.05
let center
let north = 0.

let current_map = []

let counter = 0

function setup() {
	// Creating canvas
	cv = createCanvas(windowWidth - 20, windowHeight - 20)
	gui = createGui()
	frameRate(30);

	j = createJoystick("Joystick", width - 20 - 175, height - 20 - 175 - 10 - 30, 175, 175, -150, 150, 150, -150);
	c = createCrossfader("Crossfader", width - 20 - 175, height - 20 - 175 - 10 - 30 - 10 - 30, 175, 30, -100, 100)
	t = createToggle("Manual Control", width - 20 - 175, height - 20 - 30, 175, 30)

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
		current_map = data
		
	});
}

function draw() {
	cv.background(255, 255, 255)
	fill('blue')
	circle(center.x, center.y, strokeWidth)

	strokeWeight(4)
	stroke('green')
	line(width - 40, 20, width - 40 + 15* sin(north), 20 - 15 * cos(north))

	current_map.forEach(draw_line)

	if (t.val) {
		j.visible = true
		c.visible = true
	} else {
		j.visible = false
		c.visible = false
	}

	if (j._active) {
		socket.emit('velocity_cmd', {x: -j.valY, y:j.valX, theta: 0.})
	}

	if (c._active) {
		socket.emit('velocity_cmd', {x: 0, y:0, theta: c.val})
	} else {
		c.val = 0.
	}

	drawGui()
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
	resizeCanvas(windowWidth-20, windowHeight-20, false)
	j.x = width - 20 - 175 
	j.y = height - 20 - 175 - 10 - 30

	c.x = width - 20 - 175 
	c.y = height - 20 - 175 - 10 - 30 - 10 - 30

	t.x = width - 20 - 175 
	t.y = height - 20 - 30 
	drawGui()
}

function mouseWheel(event) {
	//print(event.delta);
	//move the square according to the vertical scroll amount
	scale += 0.0005 * event.delta;
	//block page scrolling
	return false;
}

function mouseDragged(event) {
	if (!(j._active || c._active)) {
		if (event.ctrlKey) {
			north += 0.01*(mouseX - pmouseX)
		} else {
			center.x += mouseX - pmouseX
			center.y += mouseY - pmouseY
		}
	}
	return false
	
}