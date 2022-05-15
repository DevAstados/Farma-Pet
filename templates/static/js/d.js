const url = window.location.origin

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function pagar(element) {


    const inputs = new FormData(element);
    const data = Object.fromEntries(inputs)
    data.csrfmiddlewaretoken = getCookie('csrftoken')
    data.cart = loadProducts().value.items;

    const headers = new Headers({
        'X-CSRFToken': data.csrfmiddlewaretoken,
        'Acces-Control-Allow-Origin': '*',
        'content-type': 'application/json',
    });

    console.log(headers)
    fetch(`${url}/pedido/pagar/`, {
        method: 'POST',
        headers,
        mode: 'cors',
        body: JSON.stringify(data)
    }).then(res => {
        if (res.status == 200 ) {
            dat = res.json()
            window.open(res.urle + '/', '_blank').focus();
            console.log(url + '/')
            paypals.minicarts.reset()

            window.location.href = `${res.url}`
        } else {
            $(".messages").load(location.href + " .messages")
        }
    }).then(data=>{ console.log(data); }).catch(error => console.log('Request failed:', error))


}

document.getElementById('form_pagar').addEventListener('submit', (event) => {
    event.preventDefault();
    pagar(event.target)
})

