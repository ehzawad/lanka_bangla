// /**
//  * creates horizontally placed cards carousel
//  * @param {Array} cardsData json array
//  */


function createCardsCarousel(cardsData) {
    let cards = "";
    cardsData.map((card_item) => {
        let buttons = "";
        if (card_item.buttons && card_item.buttons.length > 0) {
            // buttons = card_item.buttons.map(btn =>
            //     `<button class="carousel-button" onclick="carouselButtonClick('${btn.payload}', '${btn.title}')">${btn.title}</button>`
            // ).join('');

            buttons = card_item.buttons.map(btn =>
                `<button class="carousel-button ${btn.primary ? 'primary' : ''}" onclick="carouselButtonClick('${btn.payload}', '${btn.title}')">${btn.title}</button>`
            ).join('');
        }
        const item = `
            <div class="carousel-card">
                <img class="carousel-card-image" src="${card_item.image}" alt="${card_item.title}">
                <div class="carousel-card-content">
                    <h3 class="carousel-card-title">${card_item.title}</h3>
                    <p class="carousel-card-subtitle">${card_item.subtitle || ''}</p>
                    <div class="carousel-card-buttons">${buttons}</div>
                </div>
            </div>`;
        cards += item;
    });
    return `<div class="carousel"><div class="carousel-inner">${cards}</div></div>`;
}



function showCardsCarousel(cardsToAdd) {
    const carousel = createCardsCarousel(cardsToAdd);
    $(".chats").append(carousel);
    
    const $carousel = $(".carousel");
    const $inner = $carousel.find(".carousel-inner");
    
    if (cardsToAdd.length > 1) {
        $carousel.append('<button class="carousel-control prev">&lt;</button><button class="carousel-control next">&gt;</button>');
        
        $carousel.on('click', '.carousel-control', function() {
            const direction = $(this).hasClass('next') ? 1 : -1;
            const scrollAmount = $inner.width() * direction;
            $inner.animate({ scrollLeft: '+=' + scrollAmount }, 300);
        });
    }

    scrollToBottomOfResults();
    $(".usrInput").focus();
}

// function carouselButtonClick(payload, title) {
//     setUserResponse(title);
//     send(payload);
// }

function carouselButtonClick(payload, title) {
    const button = event.target;
    button.classList.add('clicked');
    setTimeout(() => {
        button.classList.remove('clicked');
    }, 300);  // Remove the class after 300ms
    setUserResponse(title);
    send(payload);
}