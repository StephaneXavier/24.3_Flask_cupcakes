

function generate_cupcake(cupcake) {

    const $col = $(`<div class='col-4 ' id = ${cupcake.id}></div>`)
    const $card = $(`<div class = 'card text-center' style="width: 18rem">
                    <img src="${cupcake.image}"  alt="Cupcake image" class="card-img-top">
                        <div class="card-body">
                            <h3 class="card-title">
                            ${cupcake.flavor}
                            </h3>
                            <p class="card-text">
                            Cupcake size: ${cupcake.size}
                            Cupcake rating: ${cupcake.rating}
                            </p>
                        </div>

                    </div>`)

    $col.append($card)
    $('#cupcakes').append($col)
}



async function get_cupcakes() {

    let resp = await axios.get('http://127.0.0.1:5000/api/cupcakes')
    const cupcakes = resp.data.cupcakes


    for (cupcake of cupcakes) {
        $new_card = generate_cupcake(cupcake)
    }
}



async function new_cupcake_to_db(flavor, size, rating, image) {
    let resp = await axios.post('/api/cupcakes', {
        flavor: flavor,
        size: size,
        rating: rating,
        image: image
    })
    return resp

}



$('button').on('click', async function (e) {
    e.preventDefault()
    const flavor = $('#flavor').val()
    const size = $('#size').val()
    const rating = $('#rating').val()
    const image = $('#image').val()

    resp = await new_cupcake_to_db(flavor, size, rating, image)

    cupcake = resp.data.cupcake

    generate_cupcake(cupcake)

})



get_cupcakes()