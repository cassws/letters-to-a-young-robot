// var namespace = '/events'; // change to an empty string to use the global namespace
// var socket = io.connect('http://' + document.domain + ':' + location.port + namespace);
// socket.on('connect', function() {
//     // we emit a connected message to let knwo the client that we are connected.
//     socket.emit('client_connected', {data: 'New client!'});
// });

// socket.on('my response', function(msg) { 
//     console.log(msg);
//     socket.emit('NLP finished', {data: 'finished!'});
// });
//     //     //example of triggering an event on click of a form submit button
//     //     $('form#emit').submit(function(event) {
//     //         socket.emit('my event', {data: $('#emit_data').val()});
//     //         return false;
//     //     });
//     // });