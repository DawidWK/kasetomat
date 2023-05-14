function addToCard(name) {
    // add name to local storage cart
    let cart = sessionStorage.getItem('cart-kasetomat');
    if (cart == null) {
        cart = [];
    }
    else {
        cart = JSON.parse(cart);
    }
    cart.push(name);
    sessionStorage.setItem('cart-kasetomat', JSON.stringify(cart));
    alert(`Added to cart ${name}`);
}

function fillTable() {
    // fill table .cart-table with 'cart-kasetomat' data from sessionStorage
    let cart = sessionStorage.getItem('cart-kasetomat');
    if (cart == null) {
        cart = [];
    }
    else {
        cart = JSON.parse(cart);
    }
    let table = document.querySelector('.cart-table');
    let tbody = table.querySelector('tbody');
    tbody.innerHTML = '';
    for (let i = 0; i < cart.length; i++) {
        let tr = document.createElement('tr');
        let td = document.createElement('td');
        let td2 = document.createElement('td');
        td.innerHTML = cart[i];
        td2.innerHTML = `<span onclick='removeFromCart("${cart[i]}")'><i class="bi bi-trash-fill"></i></span>`;
        tr.appendChild(td);
        tr.appendChild(td2);
        tbody.appendChild(tr);
    }

    // fill hidden input with cart data 
    let input = document.querySelector('#kasety');
    input.value = sessionStorage.getItem('cart-kasetomat')
}


function removeFromCart(name) {
    // remove name from local storage cart
    let cart = sessionStorage.getItem('cart-kasetomat');
    if (cart == null) {
        cart = [];
    }
    else {
        cart = JSON.parse(cart);
    }
    let index = cart.indexOf(name);
    if (index > -1) {
        cart.splice(index, 1);
    }
    sessionStorage.setItem('cart-kasetomat', JSON.stringify(cart));
    fillTable();
}

function clearCart() {
    sessionStorage.removeItem('cart-kasetomat');
    fillTable();
}

function markOrderAsReturned(orderId) {
    // send xhr reqeuest to mark order as returned
    csrfmiddlewaretoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    let xhr = new XMLHttpRequest();
    xhr.open('POST', `/api/order-returned/${orderId}`, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader("X-CSRFToken", csrfmiddlewaretoken);
    xhr.send(JSON.stringify(
        {
            orderId: orderId 
        }
    ));
    xhr.onload = function () {
        if (xhr.status == 200) {
            alert('Order marked as returned');
            window.location.reload();
        }
        else {
            alert('Error');
        }
    }
}