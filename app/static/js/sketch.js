let socket
let color = '#000'
let strokeWidth = 4
let cv

function setup() {
	// Creating canvas
	cv = createCanvas(windowWidth / 2, windowHeight / 2)
	centerCanvas()
	cv.background(0, 0, 0)

	console.log(window.location);

	// Start the socket connection
	socket = io();

	socket.on('connect', function() {
        socket.emit('my_event', {data: 'I\'m connected!'});
    });
}

function centerCanvas() {
	const x = (windowWidth - width) / 2
	const y = (windowHeight - height) / 2
	cv.position(x, y)
}