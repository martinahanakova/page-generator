let scrollLog = [];

function logCurrentScrollPosition() {
    let from = (document.body.scrollTop / document.body.scrollHeight ) * 100;
    let to   = ((document.body.scrollTop + window.innerHeight) / document.body.scrollHeight ) * 100;

    scrollLog.push({from, to});

    if (scrollLog.length === TIME_LIMIT * 2)
        clearInterval(scrollLogInterval);
}

let scrollLogInterval = setInterval(logCurrentScrollPosition, 500);