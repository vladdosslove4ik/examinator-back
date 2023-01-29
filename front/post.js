var button = document.getElementById("b")
button.addEventListener('click', send)

function send(){
    var dics = {"tytul":"Czy", "opis":"xD","owner":"ja","czasTrwania":20,
        "terminOtwarcia": "2006-10-25 14:30:59","terminZamkniecia":"2006-10-25 14:30:59",
        "numerP":[1,2,3], /*Chodzi tutaj o numer pytania*/
        "trescPyt":["a","b","c"], /*Treść pytania*/
        "zamkniete":[true,true,false], /*Czy pytanie zamknięte żeby szukać do niego odp czy nie*/
        "numerPOdp":[1,1,2,3], /*Numer pytania do którego jest to odpowiedź*/
        "trescOdp":["a","a","a","a"]} /*Treść odpowiedzi*/

    let xhr = new XMLHttpRequest();
    let url = "http://127.0.0.1:8002/addTestV/";

    // open a connection
    xhr.open("POST", url, true);

    // Set the request header i.e. which type of content you are sending
    xhr.setRequestHeader("Content-Type", "application/json");

    // Create a state change callback
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {

            // Print received data from server
            result.innerHTML = this.responseText;

        }
    };

    // Converting JSON data to string
    var data = JSON.stringify(dics);

    // Sending data with the request
    xhr.send(data);

}
