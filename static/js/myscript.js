$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

$('.plus-cart').click(function(){
    const id = $(this).attr("pid").toString();
    const eml = this.parentNode.children[2]
    console.log(id);

    $.ajax({
        type: 'GET',
        url: "/pluscart",
        data: {
            prod_id: id
        },
        success: function(data){
           eml.innerText = data.quantity
           document.getElementById('amount').innerHTML = data.amount
           document.getElementById('total_amount').innerHTML = data.total_amount

        },
        
    });
});



$('.minus-cart').click(function(){
    const id = $(this).attr("pid").toString();
    const eml = this.parentNode.children[2]
    console.log(id);

    $.ajax({
        type: 'GET',
        url: "/minuscart",
        data: {
            prod_id: id
        },
        success: function(data){
           eml.innerText = data.quantity
           document.getElementById('amount').innerHTML = data.amount
           document.getElementById('total_amount').innerHTML = data.total_amount

        },
        
    });
});


$('.remove_cart').click(function(){
    const id = $(this).attr("pid").toString();
    const eml = this;

    $.ajax({
        type: 'GET',
        url: "/removecart",
        data: {
            prod_id: id
        },
        success: function(data){
            eml.innerText = data.quantity;
            document.getElementById('amount').innerHTML = data.amount;
            document.getElementById('total_amount').innerHTML = data.total_amount;
            eml.parentNode.parentNode.parentNode.parentNode
        },
    });
});



