var getJSON = function(url, callback) {

    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.responseType = 'json';

    xhr.onload = function() {

        var status = xhr.status;

        if (status == 200) {
            callback(null, xhr.response);
        } else {
            callback(status);
        }
    };

    xhr.send();
};

getJSON('http://127.0.0.1:8002/getTest/1',  function(err, data) {

    if (err != null) {
        console.error(err);
    } else {
        console.log(data)
        console.log(data.test.tytul)
    }
});