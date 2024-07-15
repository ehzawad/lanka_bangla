/**
 *  adds vertically stacked buttons as a bot response
 * @param {Array} suggestions buttons json array
 */
function addSuggestion(suggestions) {
    // setTimeout(() => {
        
    // }, 1000);
    const suggLength = suggestions.length;
    $(
        ' <div class="singleCard"> <div class="suggestions"><div class="menu"></div></div></diV>',
    )
        .appendTo(".chats")
        .hide()
        .fadeIn(100);
    // Loop through suggestions
    for (let i = 0; i < suggLength; i += 1) {
        $(
            `<div class="menuChips" data-payload='${suggestions[i].payload}'>${suggestions[i].title}</div>`,
        ).appendTo(".menu");
    }
    scrollToBottomOfResults();
}


// Add the new function here
function showUrlLink(urlLinkData) {
    const urlLength = urlLinkData.length;
    $(
        '<div class="singleCard"><div class="suggestions"><div class="menu"></div></div></div>'
    )
        .appendTo(".chats")
        .hide()
        .fadeIn(100);

    for (let i = 0; i < urlLength; i += 1) {
        $(`<div class="menuChips">
            <a href="${urlLinkData[i].url}" target="_blank" rel="noopener noreferrer">
                ${urlLinkData[i].title}
            </a>
        </div>`).appendTo(".menu");
    }
    scrollToBottomOfResults();
}


// // on click of suggestion's button, get the title value and send it to rasa
// $(document).on("click", ".menu .menuChips", function () {
//     const text = this.innerText;
//     const payload = this.getAttribute("data-payload");
//     console.log("payload: ", this.getAttribute("data-payload"));
//     setUserResponse(text);
//     send(payload);

//     // delete the suggestions once user click on it.
//     $(".suggestions").remove();
// });


// on click of suggestion's button, get the title value and send it to rasa
// $(document).on("click", ".menu .menuChips", function (e) {
//     const $this = $(this);
//     const text = this.innerText;
//     const payload = this.getAttribute("data-payload");
    
//     // Check if it's a URL link (contains an anchor tag)
//     if ($this.find('a').length > 0) {
//         // It's a URL link, so we don't need to send anything to Rasa
//         // The link will open in a new tab due to the target="_blank" attribute
//         // We also don't want to remove the suggestions in this case
//         return;
//     }
    
//     console.log("payload: ", payload);
//     setUserResponse(text);
//     send(payload);

//     // delete the suggestions once user clicks on it (only for non-URL suggestions)
//     $(".suggestions").remove();
// });


// $(document).on("click", ".menu .menuChips", function (e) {
//     const $this = $(this);
//     const text = this.innerText;
//     const payload = this.getAttribute("data-payload");
    
//     console.log("payload: ", payload);
//     setUserResponse(text);
//     send(payload);
    
//     // Don't remove the suggestions
// });

// function showButtons(buttonsData) {
//     const { text, buttons } = buttonsData;

//     // Clear existing suggestions first
//     $(".suggestions").remove();

//     // Add the text message
//     const botResponse = `<div class="botAvatar"><div class="botAvatar-image"><img src="./static/img/disha.svg"/></div><p class="botMsg">${text}</p></div><div class="clearfix"></div>`;
//     $(botResponse).appendTo(".chats").hide().fadeIn(500);

//     // Add buttons
//     const buttonsHtml = '<div class="singleCard"><div class="suggestions"><div class="menu"></div></div></div>';
//     $(buttonsHtml).appendTo(".chats").hide().fadeIn(500);

//     for (let i = 0; i < buttons.length; i += 1) {
//         $(`<div class="menuChips" data-payload='${buttons[i].payload}'>${buttons[i].title}</div>`)
//             .appendTo(".menu");
//     }
//     scrollToBottomOfResults();
// }

// function showButtons(buttonsData) {
//     const { text, buttons } = buttonsData;

//     // Clear existing suggestions first
//     $(".suggestions").remove();

//     // Add the text message
//     const botResponse = `<div class="botAvatar"><div class="botAvatar-image"><img src="./static/img/disha.svg"/></div><p class="botMsg">${text}</p></div><div class="clearfix"></div>`;
//     $(botResponse).appendTo(".chats").hide().fadeIn(500);

//     // Add buttons
//     const buttonsHtml = '<div class="singleCard"><div class="suggestions"><div class="menu"></div></div></div>';
//     $(buttonsHtml).appendTo(".chats").hide().fadeIn(500);

//     for (let i = 0; i < buttons.length; i += 1) {
//         let buttonHtml = `<div class="menuChips" data-payload='${buttons[i].payload}'`;
//         if (buttons[i].type === 'urlLink') {
//             buttonHtml += ` data-type="urlLink"`;
//         }
//         buttonHtml += `>${buttons[i].title}</div>`;
//         $(buttonHtml).appendTo(".menu");
//     }
//     scrollToBottomOfResults();
// }


function showButtons(buttonsData) {
    const { text, buttons } = buttonsData;

    // Clear existing suggestions first
    $(".suggestions").remove();

    // Add the text message
    const botResponse = `<div class="botAvatar"><div class="botAvatar-image"><img src="./static/img/disha.svg"/></div><p class="botMsg">${text}</p></div><div class="clearfix"></div>`;
    $(botResponse).appendTo(".chats").hide().fadeIn(500);

    // Add buttons
    const buttonsHtml = '<div class="singleCard"><div class="suggestions"><div class="menu"></div></div></div>';
    $(buttonsHtml).appendTo(".chats").hide().fadeIn(500);

    for (let i = 0; i < buttons.length; i += 1) {
        let buttonHtml;
        if (buttons[i].type === 'urlLink') {
            buttonHtml = `<div class="menuChips urlLink" data-url="${buttons[i].url}">${buttons[i].title}</div>`;
        } else {
            buttonHtml = `<div class="menuChips" data-payload='${buttons[i].payload}'>${buttons[i].title}</div>`;
        }
        $(buttonHtml).appendTo(".menu");
    }
    scrollToBottomOfResults();
}

$(document).on("click", ".menu .menuChips", function (e) {
    const $this = $(this);
    const text = this.innerText;
    
    if ($this.hasClass('urlLink')) {
        // It's a URL link button
        const url = $this.data('url');
        window.open(url, '_blank');
        // Don't remove suggestions or send anything to Rasa
        return;
    }
    
    // For non-URL buttons
    const payload = this.getAttribute("data-payload");
    console.log("payload: ", payload);
    setUserResponse(text);
    send(payload);
    $(".suggestions").remove();
});