// function start_task() {
//     console.log('started!')
//     // send ajax POST request to start background job
//     $.ajax({
//         type: 'POST',
//         url: '/addtask',
//         success: function(data, status, request) {
//             status_url = request.getResponseHeader('Location');
//             update_progress(status_url);
//         },
//         error: function() {
//             alert('Unexpected error');
//         }
//     });
// } 
// function update_progress(status_url, nanobar, status_div) {

function update_progress(status_url) {
    // send GET request to status URL
    $.getJSON(status_url, function(data) {
        // update UI
        percent = parseInt(data['current'] * 100 / data['total']);
        percent_string = percent.toString();
        var prog_bar = document.getElementById("prog_bar");
        prog_bar.innerHTML = "NLP subroutines running, " + percent_string +"% complete"
        // nanobar.go(percent);
        // $(status_div.childNodes[1]).text(percent + '%');
        // $(status_div.childNodes[2]).text(data['status']);
        console.log(percent);
        if (data['state'] != 'PENDING' && data['state'] != 'PROGRESS') {
            if ('result' in data) {
                prog_bar.innerHTML = "Task " + percent_string +"% complete!"

                // show result
                // $(status_div.childNodes[3]).text('Result: ' + data['result']);
            }
            else {
                // something unexpected happened
                // $(status_div.childNodes[3]).text('Result: ' + data['state']);
            }
        }
        else {
            // rerun in 2 seconds
            setTimeout(function() {
                update_progress(status_url);
            }, 1000);
        }
    });
}

