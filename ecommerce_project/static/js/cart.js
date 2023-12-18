const updateBns = document.getElementsByClassName('update-cart')
let navbar = document.querySelector('.navbar.fixed-top')

  
for(let i=0; i<updateBns.length; ++i) {
    updateBns[i].addEventListener('click', function() {
        let productId = this.dataset.product
        let action = this.dataset.action
        // console.log('productId: ', productId, 'action: ', action)

        if(user === 'AnonymousUser') {
            addCookieItem(productId, action);
        } else {
            updateUserOrder(productId, action);
        }
    })
}

function addCookieItem(productId, action) {
    console.log('Cookie was added! ')

    if(action == "add") {
        if(cart[productId] == undefined) {
            cart[productId] = {quantity: 1};
        } else {
            cart[productId]["quantity"] += 1;
        }
    }

    if(action == "remove") {
        cart[productId]["quantity"] -= 1;
        if(cart[productId]["quantity"] <= 0) {
            console.log('Remove Item')
            delete cart[productId]
        }
    }

    console.log('Cart: ', cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"

    location.reload();
    
}

// Update the user order and send request to '/update_item/' URL
function updateUserOrder(productId, action) {
    console.log('User is logged in, sending data...');

    const url = '/update_item/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({productId: productId, action: action})
    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log('data: ', data)
        location.reload()
    })
}