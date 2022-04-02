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

function setInputsForm() {
    inputs = []

    select_endereco = document.getElementById('select_endereco')
    if (select_endereco != null) {
        select_endereco.style.display = 'none'
    }

    cadastro = document.getElementById('cadastro')
    cadastro.value = 'True'

    if (document.getElementById('text_date') == null) {

        div = document.createElement('div')
        div.className = 'controls form-group'

        input = document.createElement('input')
        input.className = 'billing-address-name form-control'
        input.type = 'date'
        input.name = 'date_nascimento'
        input.placeholder = 'Data de nascimento'
        input.id = 'text_date'
        input.required = ""
        div.appendChild(input)

        inputs.push(div)
    }

    if (document.getElementById('text_email') == null) {

        div = document.createElement('div')
        div.className = 'controls form-group'

        input = document.createElement('input')
        input.className = 'billing-address-name form-control'
        input.type = 'email'
        input.name = 'email'
        input.placeholder = 'E-mail'
        input.id = 'text_email'
        input.required = ""
        div.appendChild(input)

        inputs.push(div)
    }

    if (document.getElementById('text_tipo_endereco') == null) {

        div = document.createElement('div')
        div.className = 'controls form-group'

        input = document.createElement('input')
        input.className = 'billing-address-name form-control'
        input.type = 'text'
        input.name = 'tipo_endereco'
        input.placeholder = 'Nome do endereço'
        input.id = 'text_tipo_endereco'
        div.appendChild(input)

        inputs.push(div)
    }
    if (document.getElementById('text_cep') == null) {

        div = document.createElement('div')
        div.className = 'controls form-group'

        input = document.createElement('input')
        input.className = 'billing-address-name form-control'
        input.type = 'text'
        input.name = 'cep'
        input.placeholder = 'CEP'
        input.id = 'text_cep'
        input.required = ""
        div.appendChild(input)

        inputs.push(div)
    }
    if (document.getElementById('text_num') == null) {

        div = document.createElement('div')
        div.className = 'controls form-group'

        input = document.createElement('input')
        input.className = 'billing-address-name form-control'
        input.type = 'text'
        input.name = 'numero_casa'
        input.placeholder = 'Número'
        input.id = 'text_num'
        input.required = ""
        div.appendChild(input)

        inputs.push(div)
    }
    if (document.getElementById('text_complement') == null) {

        div = document.createElement('div')
        div.className = 'controls form-group'

        input = document.createElement('input')
        input.className = 'billing-address-name form-control'
        input.type = 'text'
        input.name = 'complemento'
        input.placeholder = 'Complemento'
        input.id = 'text_complement'
        div.appendChild(input)

        inputs.push(div)
    }


    return inputs
}

function deleteInputsForm() {
    select_endereco = document.getElementById('select_endereco')
    select_endereco.style.display = 'block'

    cadastro = document.getElementById('cadastro')
    cadastro.value = 'False'

    text_dat = document.getElementById('text_date')
    if (text_dat != null) {
        text_dat.parentNode.removeChild(text_dat)
    }

    text_email = document.getElementById('text_email')
    if (text_email != null) {
        text_email.parentNode.removeChild(text_email)
    }

    text_tipo_endereco = document.getElementById('text_tipo_endereco')
    if (text_tipo_endereco != null) {
        text_tipo_endereco.parentNode.removeChild(text_tipo_endereco)
    }

    text_cep = document.getElementById('text_cep')
    if (text_cep != null) {
        text_cep.parentNode.removeChild(text_cep)
    }

    text_num = document.getElementById('text_num')
    if (text_num != null) {
        text_num.parentNode.removeChild(text_num)
    }

    text_complement = document.getElementById('text_complement')
    if (text_complement != null) {
        text_complement.parentNode.removeChild(text_complement)
    }


}

function criarPopulaEndereco(enderecos) {
    var select_endereco = document.getElementById("select_endereco");

    for (index in enderecos) {
        var opt = document.createElement("option");
        opt.value = enderecos[index].tipo
        opt.text = `${enderecos[index].tipo} Número: ${enderecos[index].numero} - CEP: ${enderecos[index].cep} `
        select_endereco.appendChild(opt)
    }

}

async function esconderCampoPesquisa(input) {
    const data = {}
    data.csrfmiddlewaretoken = getCookie('csrftoken')
    const headers = new Headers({
        'X-CSRFToken': data.csrfmiddlewaretoken
    });

    data.cpf = document.getElementById("text_cpf").value

    var handleError = function (err) {
        console.warn(err);
        return new Response(JSON.stringify({
            code: 400,
            message: 'Stupid network Error'
        }));
    };

    await fetch(`${url}/cliente/buscar`, {
        method: 'POST',
        headers,
        body: JSON.stringify(data)

    }).then((response) => {

        if (response.ok) {
            deleteInputsForm()
            return response.json()
        } else if (response.status == 404) {
            form = document.getElementById('form_cliente')
            divInputs = form.querySelectorAll('.controls.form-group')[1]
            inputs = setInputsForm()

            for (let i = (inputs.length - 1); i > 0; i--) {
                divInputs.parentNode.insertBefore(inputs[i], divInputs.nextSibling);
            }

        }

    }).then(data => ({
            data: data,
        })
    ).then(res => {

        let response = JSON.parse(res.data.Cliente)

        console.log(response)
        console.log(JSON.parse(res.data.Endereco))

        document.getElementById("text_nome").value = `${response[0]['fields']['nome']} ${response[0]['fields']['sobrenome']} `
        document.getElementById("text_telefone").value = `${response[0]['fields']['telefone']} `
        criarPopulaEndereco(JSON.parse(res.data.Endereco))

    }).catch((error) => {
        console.error(error)
    });


}

function pagar(element) {


    const inputs = new FormData(element);
    const data = Object.fromEntries(inputs)
    data.csrfmiddlewaretoken = getCookie('csrftoken')
    data.cart = loadProducts().value.items;

    const headers = new Headers({
        'X-CSRFToken': data.csrfmiddlewaretoken
    });

    console.log(data)
    fetch(`${url}/pedido/`, {
        method: 'POST',
        headers,
        body: JSON.stringify(data)
    }).then(res => {
        if (res.status == 200 && res.redirected) {
            paypals.minicarts.reset()
            window.location.href = `${res.url}`
        } else {
            $(".messages").load(location.href + " .messages")
        }
    })


}

document.getElementById("text_cpf").addEventListener("blur", esconderCampoPesquisa);

document.getElementById('form_cliente').addEventListener('submit', (event) => {
    event.preventDefault();
    pagar(event.target)
})

